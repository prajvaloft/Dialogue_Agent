from agent.inference import predict_action


state = [1, 0, 0, 0]

action, q_values = predict_action(
    state
)

print("State:")
print(state)

print("\nRecommended Action:")
print(action)

print("\nQ Values:")
print(q_values)