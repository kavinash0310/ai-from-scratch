"""Lab 16: tabular Q-learning in a small grid world.

An agent repeatedly acts, observes a reward, and updates an estimate of future
return for a state/action pair. Epsilon-greedy behavior explores occasionally
and otherwise uses the best current action. This works here because the state
and action spaces are small and discrete.
"""

import numpy as np

height, width = 4, 4
start, goal = (0, 0), (3, 3)
walls = {(1, 1), (2, 1)}
actions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
Q = np.zeros((height, width, len(actions)))
rng = np.random.default_rng(12)
alpha, gamma = 0.15, 0.95


def move(state, action_index):
    row, col = state
    dr, dc = actions[action_index]
    candidate = (row + dr, col + dc)
    r, c = candidate
    if not (0 <= r < height and 0 <= c < width) or candidate in walls:
        return state
    return candidate


for episode in range(2500):
    state = start
    epsilon = max(0.03, 0.8 * (0.997 ** episode))
    for step in range(60):
        if rng.random() < epsilon:
            action = int(rng.integers(len(actions)))
        else:
            action = int(np.argmax(Q[state[0], state[1]]))
        next_state = move(state, action)
        done = next_state == goal
        reward = 10.0 if done else -0.1
        future = 0.0 if done else gamma * np.max(Q[next_state[0], next_state[1]])
        old = Q[state[0], state[1], action]
        Q[state[0], state[1], action] = old + alpha * (reward + future - old)
        state = next_state
        if done:
            break

# Follow the learned greedy policy. The seen-set prevents an infinite display
# if the learner changes the world or stops training before finding a route.
state = start
route = [state]
seen = {state}
for _ in range(20):
    action = int(np.argmax(Q[state[0], state[1]]))
    state = move(state, action)
    route.append(state)
    if state == goal or state in seen:
        break
    seen.add(state)

print("Greedy route:", route)
print("Reached goal:", state == goal)
print("Episodes use reward +10 at the goal and a small step penalty.")

# Change the reward or add a wall. Discuss reward design, exploration, and
# why simulation success does not guarantee safe real-world behavior.
