import torch
from agent.dqn_agent import DQNAgent

STATE_SIZE = 4
ACTION_SIZE = 5

actions = [
    "Which movie would you like to watch?",
    "Please select your preferred theater.",
    "Could you please choose a show time?",
    "Please confirm your booking details.",
    "Your movie ticket has been booked successfully! 🎉"
]


def load_agent():

    model = DQNAgent(
        STATE_SIZE,
        ACTION_SIZE
    )

    model.load_state_dict(
        torch.load(
            "models/dqn_movie_agent.pth",
            map_location=torch.device("cpu")
        )
    )

    model.eval()

    return model


# Load model once
model = load_agent()


def predict_action(state):

    state_tensor = torch.FloatTensor(state)

    with torch.no_grad():
        q_values = model(state_tensor)

    action_index = torch.argmax(q_values).item()

    return (
        actions[action_index],
        q_values.tolist()
    )