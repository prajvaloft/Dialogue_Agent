import torch

from agent.dqn_agent import DQNAgent

state_size = 4
action_size = 5

agent = DQNAgent(
    state_size,
    action_size
)

state = torch.FloatTensor(
    [1, 1, 0, 0]
)

q_values = agent(state)

print("Q Values:")
print(q_values)