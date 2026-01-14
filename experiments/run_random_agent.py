from env.maze_env import MazeEnv
import numpy as np

env = MazeEnv(grid_size=5)

episodes = 3

for ep in range(episodes):
    obs, _ = env.reset()
    done = False
    total_reward = 0

    print(f"Episode {ep + 1}")

    while not done:
        action = env.action_space.sample()
        obs, reward, done, _, _ = env.step(action)
        total_reward += reward
        env.render()

    print("Total reward:", total_reward)
