from training.replay_buffer import ReplayBuffer

buffer = ReplayBuffer()

buffer.push(
    [0, 0, 0, 0],
    0,
    10,
    [1, 0, 0, 0],
    False
)

buffer.push(
    [1, 0, 0, 0],
    1,
    10,
    [1, 1, 0, 0],
    False
)

print("Buffer Size:")
print(len(buffer))

print("\nSample:")

sample = buffer.sample(2)

for item in sample:
    print(item)