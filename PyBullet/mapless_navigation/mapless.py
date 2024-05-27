import os, sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
os.environ['TF_ENABLE_ONEDNN_OPTS'] = '0'
from env import MaplessNavEnv
env = MaplessNavEnv(render=True)
sys.path.append(os.path.join(os.getcwd(),"stable_baselines3"))
# from stable_baselines3.common.env_checker import check_env

# check_env(env)
import pybullet as p 
import numpy as np
# env = CircleDrive(render=True)
obs, _ = env.reset()
p.setRealTimeSimulation(1)
while True:
    action = np.random.uniform(-10, 10, size=(2,))
    obs, reward, done, _, _ = env.step(action)
    if done:
        break

    print(f"state : {obs}, reward : {reward}")