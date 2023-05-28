import gymnasium as gym
import sys

sys.path.insert(0, '../')

def make_env(env_key, seed=None, render_mode=None, **kwargs):
    env = gym.make(f"my_minigrid:{env_key}", render_mode=render_mode, **kwargs)
    env.reset(seed=seed)
    return env
