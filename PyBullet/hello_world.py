'''
Author: WANG CHENG
Date: 2024-05-23 10:58:27
LastEditTime: 2024-05-23 11:12:19
'''
import pybullet as p
import time
import pybullet_data

# 连接物理引擎
physicsCilent = p.connect(p.GUI) # p.connect(p.DIRECT) 

p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 0)

# 添加资源路径
p.setAdditionalSearchPath(pybullet_data.getDataPath())

# 设置环境重力加速度
p.setGravity(0, 0, -10)

# 加载URDF模型，此处是加载蓝白相间的陆地
planeId = p.loadURDF("plane.urdf")

# 加载机器人，并设置加载的机器人的位姿
startPos = [0, 0, 1]
startOrientation = p.getQuaternionFromEuler([0, 0, 0])
boxId = p.loadURDF("r2d2.urdf", startPos, startOrientation)

# 按照位置和朝向重置机器人的位姿，由于我们之前已经初始化了机器人，所以此处加不加这句话没什么影响
p.resetBasePositionAndOrientation(boxId, startPos, startOrientation)

p.configureDebugVisualizer(p.COV_ENABLE_TINY_RENDERER, 0)   # 禁用tinyrenderer，也就是不让CPU上的集成显卡来参与渲染工作。
p.configureDebugVisualizer(p.COV_ENABLE_GUI, 0) # 禁用GUI，也就是不显示物理引擎的GUI界面。
p.configureDebugVisualizer(p.COV_ENABLE_RENDERING, 1)     # 启用渲染功能。

# p.setRealTimeSimulation(1)
# 开始一千次迭代，也就是一千次交互，每次交互后停顿1/240
for i in range(1000):
    p.stepSimulation()
    time.sleep(1 / 240)

# 获取位置与方向四元数
cubePos, cubeOrn = p.getBasePositionAndOrientation(boxId)
print("-" * 20)
print(f"机器人的位置坐标为:{cubePos}\n机器人的朝向四元数为:{cubeOrn}")
print("-" * 20)

# 断开连接
p.disconnect()