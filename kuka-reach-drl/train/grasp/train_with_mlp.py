#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
@File    :   train.py
@Time    :   2021/03/20 14:30:42
@Author  :   Yan Wen 
@Version :   1.0
@Contact :   z19040042@s.upc.edu.cn
@Desc    :   None
'''

# here put the import lib

import os,inspect
current_dir=os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
os.chdir(current_dir)
import sys
sys.path.append('../../')

from env.kuka_grasp_env import KukaGraspEnv
from ppo.ppo import ppo
from spinup.utils.mpi_tools import mpi_fork
import ppo.core as core

import argparse

parser = argparse.ArgumentParser()
# parser.add_argument('--env', type=str, default='HalfCheetah-v2')

#modified this to satisfy the custom env
#parser.add_argument('--env', type=str, default=env)
parser.add_argument('--render',action="store_true")
parser.add_argument('--good_view',action="store_true")

parser.add_argument('--hid', type=int, default=64)
parser.add_argument('--l', type=int, default=3)
parser.add_argument('--gamma', type=float, default=0.99)
parser.add_argument('--seed', '-s', type=int, default=0)
parser.add_argument('--cpu', type=int, default=5)
parser.add_argument('--steps', type=int, default=4000)
parser.add_argument('--epochs', type=int, default=500)
parser.add_argument('--exp_name', type=str, default='ppo-kuka-grasp-with-mlp')
parser.add_argument('--log_dir', type=str, default="../../logs")
args = parser.parse_args()



env=KukaGraspEnv(is_render=args.render,is_good_view=args.good_view)

mpi_fork(args.cpu)  # run parallel code with mpi

from spinup.utils.run_utils import setup_logger_kwargs

logger_kwargs = setup_logger_kwargs(args.exp_name, args.seed,data_dir=args.log_dir)

ppo(env,
    actor_critic=core.MLPActorCritic,
    ac_kwargs=dict(hidden_sizes=[args.hid] * args.l),
    gamma=args.gamma,
    seed=args.seed,
    steps_per_epoch=env.max_steps_one_episode*args.cpu,
    epochs=args.epochs,
    logger_kwargs=logger_kwargs)