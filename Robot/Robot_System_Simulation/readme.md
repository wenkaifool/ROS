# System Simulation of Robots in ROS  

This project is mainly composed of three parts:  
1. how to model the robot based on URDF and visulize it in RVIZ and Gazebo, repsectively;  
2. how to design a simulated enviroment using Gazebo;  
3. How to get the env info from the sensor, such as laser, camera, encoder, etc..  

Here are detailed introdcution about these components.  
1. URDF  
   URDF是 Unified Robot Description Format 的首字母缩写，直译为统一(标准化)机器人描述格式，可以以一种 XML 的方式描述机器人的部分结构，比如底盘、摄像头、激光雷达、机械臂以及不同关节的自由度。该文件可以被 C++ 内置的解释器转换成可视化的机器人模型，是 ROS 中实现机器人仿真的重要组件。  

2. RVIZ  
   RViz 是 ROS Visualization Tool 的首字母缩写，直译为ROS的三维可视化工具。它的主要目的是以三维方式显示ROS消息，可以将 数据进行可视化表达。例如:可以显示机器人模型，可以无需编程就能表达激光测距仪（LRF）传感器中的传感 器到障碍物的距离，RealSense、Kinect或Xtion等三维距离传感器的点云数据（PCD， Point Cloud Data），从相机获取的图像值等。   

3. Gazebo  
   Gazebo是一款3D动态模拟器，用于显示机器人模型并创建仿真环境,能够在复杂的室内和室外环境中准确有效地模拟机器人。与游戏引擎提供高保真度的视觉模拟类似，Gazebo提供高保真度的物理模拟，其提供一整套传感器模型，以及对用户和程序非常友好的交互方式。  

总结  
机器人的系统仿真是一种集成实现，主要包含三部分:  
(1) URDF 用于创建机器人模型  
(2) Gzebo 用于搭建仿真环境
(3) Rviz 图形化的显示机器人各种传感器感知到的环境信息  
三者应用中，只是创建 URDF 意义不大，一般需要结合 Gazebo 或 Rviz 使用，在 Gazebo 或 Rviz 中可以将 URDF 文件解析为图形化的机器人模型，一般的使用组合为:  
(1) 如果非仿真环境，那么使用 URDF 结合 Rviz 直接显示感知的真实环境信息  
(2) 如果是仿真环境，那么需要使用 URDF 结合 Gazebo 搭建仿真环境，并结合 Rviz 显示感知的虚拟环境信息

Source : http://www.autolabor.com.cn/book/ROSTutorials/di-6-zhang-ji-qi-ren-xi-tong-fang-zhen/61-gai-shu.html