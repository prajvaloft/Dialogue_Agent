class RewardShaper:

    def __init__(self):
        pass

    def get_shaped_reward(
        self,
        previous_state,
        current_state,
        base_reward,
        done
    ):

        shaped_reward = base_reward

        # Reward if a new slot is filled
        if sum(current_state) > sum(previous_state):
            shaped_reward += 5

        # Penalize if no progress is made
        elif sum(current_state) == sum(previous_state):
            shaped_reward -= 2

        # Extra bonus for successful completion
        if done and current_state[-1] == 1:
            shaped_reward += 20

        return shaped_reward