import sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT))
import random
import torch

from environment.movie_booking_env import MovieBookingEnv
from agent.dqn_agent import DQNAgent
from training.replay_buffer import ReplayBuffer


# Environment
env = MovieBookingEnv()

# State and Action Sizes
state_size = 4
action_size = 5

# Agent
agent = DQNAgent(state_size, action_size)

# Replay Buffer
buffer = ReplayBuffer()

# Optimizer and Loss
optimizer = torch.optim.Adam(
    agent.parameters(),
    lr=0.001
)

loss_fn = torch.nn.MSELoss()

# Hyperparameters
EPISODES = 1000

GAMMA = 0.99

EPSILON = 1.0
EPSILON_MIN = 0.01
EPSILON_DECAY = 0.995

BATCH_SIZE = 16


for episode in range(EPISODES):

    state = env.reset()
    done = False
    total_reward = 0

    while not done:

        # Epsilon-Greedy Action Selection
        if random.random() < EPSILON:

            action = random.randint(
                0,
                action_size - 1
            )

        else:

            state_tensor = torch.FloatTensor(state)

            with torch.no_grad():
                q_values = agent(state_tensor)

            action = torch.argmax(q_values).item()

        # Environment Step
        next_state, reward, done = env.step(action)

        # Store Experience
        buffer.push(
            state,
            action,
            reward,
            next_state,
            done
        )

        # Train if enough samples exist
        if len(buffer) >= BATCH_SIZE:

            batch = buffer.sample(BATCH_SIZE)

            for experience in batch:

                s, a, r, ns, d = experience

                s = torch.FloatTensor(s)
                ns = torch.FloatTensor(ns)

                current_q = agent(s)[a]

                with torch.no_grad():

                    max_next_q = torch.max(
                        agent(ns)
                    ).item()

                    target_q = r

                    if not d:
                        target_q += (
                            GAMMA * max_next_q
                        )

                loss = loss_fn(
                    current_q,
                    torch.tensor(
                        target_q,
                        dtype=torch.float32
                    )
                )

                optimizer.zero_grad()
                loss.backward()
                optimizer.step()

        state = next_state
        total_reward += reward

    if (episode + 1) % 50 == 0:

        print(
            f"Episode {episode + 1}"
            f" | Reward: {total_reward}"
            f" | Buffer Size: {len(buffer)}"
            f" | Epsilon: {EPSILON:.3f}"
        )

    EPSILON = max(
        EPSILON_MIN,
        EPSILON * EPSILON_DECAY
    )
    torch.save(
    agent.state_dict(),
    "models/dqn_movie_agent.pth"
)

print("\nModel Saved!")