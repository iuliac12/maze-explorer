from setuptools import setup, find_packages

setup(
    name="maze_rl_project",
    version="0.1",
    packages=find_packages(),
    install_requires=[
        "gymnasium",
        "numpy",
        "torch",
        "stable-baselines3",
        "matplotlib"
    ],
)
