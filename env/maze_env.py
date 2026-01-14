import gymnasium as gym
from gymnasium import spaces
import numpy as np

class MazeEnv(gym.Env):
    """
    Maze Explorer 2D (fără obstacole)
    Stare: (x, y)
    Actiuni: 0=UP, 1=DOWN, 2=LEFT, 3=RIGHT
    """
    metadata = {"render_modes": ["human"]}

    def __init__(self, grid_size=5):
        super().__init__()

        self.grid_size = grid_size
        self.start_pos = np.array([0, 0])
        self.goal_pos = np.array([grid_size - 1, grid_size - 1])
        self.agent_pos = self.start_pos.copy()

        # Actiuni discrete
        self.action_space = spaces.Discrete(4)

        # Observație: poziția agentului
        self.observation_space = spaces.Box(
            low=0,
            high=grid_size - 1,
            shape=(2,),
            dtype=np.int32
        )

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)
        self.agent_pos = self.start_pos.copy()
        return self.agent_pos.copy(), {}

    def step(self, action):
        x, y = self.agent_pos

        if action == 0:   # UP
            x = max(x - 1, 0)
        elif action == 1: # DOWN
            x = min(x + 1, self.grid_size - 1)
        elif action == 2: # LEFT
            y = max(y - 1, 0)
        elif action == 3: # RIGHT
            y = min(y + 1, self.grid_size - 1)

        self.agent_pos = np.array([x, y])

        terminated = np.array_equal(self.agent_pos, self.goal_pos)
        reward = 100 if terminated else -1

        return self.agent_pos.copy(), reward, terminated, False, {}

    def render(self):
        grid = np.full((self.grid_size, self.grid_size), ".")
        x, y = self.agent_pos
        gx, gy = self.goal_pos
        grid[gx, gy] = "G"
        grid[x, y] = "A"
        print("\n".join(" ".join(row) for row in grid))
        print()
