'''
Author: WANG CHENG
Date: 2024-05-23 15:23:38
LastEditTime: 2024-05-27 16:24:24
'''
from pybullet_envs.bullet import CartPoleBulletEnv
# from stable_baselines.deepq import DQN
from baselines.deepq import DEEPQ
from time import sleep
import pybullet as p

env = CartPoleBulletEnv(renders=True, discrete_actions=True)
model = DEEPQ(policy="MlpPolicy", env=env)
model.load(
    load_path="./model",
    env=env
)

obs = env.reset()
while True:
    sleep(1 / 60)
    action, state = model.predict(observation=obs)
    print(action)
    obs, reward, done, info = env.step(action)
    if done:
        break

# import pybullet as p
# import pybullet_envs
# from time import sleep
# import gym

# cid = p.connect(p.DIRECT)
# env = gym.make("CartPoleContinuousBulletEnv-v0")
# env.render()
# env.reset()

# for _ in range(10000):
#     sleep(1 / 60)
#     action = env.action_space.sample()
#     obs, reward, done, _ = env.step(action)

# p.disconnect(cid)