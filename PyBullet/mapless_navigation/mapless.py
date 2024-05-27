import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from env import MaplessNavEnv
env = MaplessNavEnv(render=False)
from stable_baselines3.common.env_checker import check_env

check_env(env)