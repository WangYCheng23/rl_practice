'''
Author: WANG CHENG
Date: 2024-05-23 14:59:35
LastEditTime: 2024-05-23 14:59:40
'''

import pybullet as p
import time

# 设置物理引擎
p.connect(p.GUI)
p.setGravity(0,0,-10) # 设置重力
p.setTimeStep(1./240.) # 设置时间步长

# 创建地面
ground_id = p.createCollisionShape(p.GEOM_PLANE)
p.setCollisionShapeUserIndex(ground_id, 0)
p.createMultiBody(0, ground_id)

# 创建曲杆
visual_shape_id = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.05, 0.05, 0.05])
collision_shape_id = p.createCollisionShape(p.GEOM_BOX, halfExtents=[0.05, 0.05, 0.05])
mass = 1
moment = p.getMomentOfInertia(mass, [0,0,0], [0,0,1]) # 转动惯量
flags = p.COLLISION_FLAGS_FIRST_GROUP # 设置碰撞组
index = p.createMultiBody(mass, moment, [visual_shape_id], [collision_shape_id], flags)
p.setPosition(index, [0, 0, 1]) # 设置初始位置

# 模拟运动
for i in range(1000):
    p.stepSimulation()
    time.sleep(1./240.) # 等待物理引擎步进
    p.setPosition(index, [0, 0, 1 + 0.01*i%2]) # 移动曲杆
    p.setEulerZYX(index, [0]*3) # 设置曲杆角度
    p.render() # 渲染画面