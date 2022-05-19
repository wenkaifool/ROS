 URDF 用于创建机器人模型、Rviz 可以显示机器人感知到的环境信息，Gazebo 用于仿真，可以模拟外界环境，以及机器人的一些传感器。  

1. 编辑Gazebo的URDF文件好之后，利用launch就可以将机器人模型显示在 Gazebo之中，在当前默认情况下是在 empty world 中，并没有类似于房间、家具、道路、树木... 之类的仿真物，如何在 Gazebo 中创建仿真环境呢？Gazebo 中创建仿真实现方式有两种:  
   (1) 方式1: 直接添加内置组件创建仿真环境  
       添加完毕后，选择 file ---> Save World as 选择保存路径(功能包下: worlds 目录)，文件名自定义，后缀名设置为 .world。再次登陆的时候可以利用如下参数：  
       arg name="world_name" value="$(find pkg_name)/worlds/hello.world"  
   (2) 方式2: 手动绘制仿真环境(更为灵活)  

2. 运动控制以及里程计信息显示  
   (1) ros_conntrol  
       场景:同一套 ROS 程序，如何部署在不同的机器人系统上，比如：开发阶段为了提高效率是在仿真平台上测试的，部署时又有不同的实体机器人平台，不同平台的实现是有差异的，如何保证 ROS 程序的可移植性？ROS 内置的解决方式是 ros_control。  
       ros_control:是一组软件包，它包含了控制器接口，控制器管理器，传输和硬件接口。ros_control 是一套机器人控制的中间件，是一套规范，不同的机器人平台只要按照这套规范实现，那么就可以保证 与ROS 程序兼容，通过这套规范，实现了一种可插拔的架构设计，大大提高了程序设计的效率与灵活性。  
       gazebo 已经实现了 ros_control 的相关接口，如果需要在 gazebo 中控制机器人运动，直接调用相关接口即可。  
   (2) 运动控制实现流程(Gazebo)  
       (a) 已经创建完毕的机器人模型，编写一个单独的 xacro 文件，为机器人模型添加传动装置以及控制器  
       (b) 将此文件集成进xacro文件
       (c) 启动 Gazebo 并发布 /cmd_vel 消息控制机器人运动  
![image](https://github.com/wenkaifool/ROS/tree/master/Robot/Robot_System_Simulation/Robot_Env_Modelling/image/odom.png)  
3. 雷达信息仿真以及显示  
   通过 Gazebo 模拟激光雷达传感器，并在 Rviz 中显示激光数据。  
![image](https://github.com/wenkaifool/ROS/tree/master/Robot/Robot_System_Simulation/Robot_Env_Modelling/image/laser.png)  
4. 摄像头信息仿真以及显示  
   通过 Gazebo 模拟摄像头传感器，并在 Rviz 中显示摄像头数据。  
![image](https://github.com/wenkaifool/ROS/tree/master/Robot/Robot_System_Simulation/Robot_Env_Modelling/image/rgb_cam.png)  
5. kinect 信息仿真以及显示  
![image](https://github.com/wenkaifool/ROS/tree/master/Robot/Robot_System_Simulation/Robot_Env_Modelling/image/kinect.png)  

6. files introduction:  
(0) assemble_car.xarco: It contains all xarco files for describing cars.  
(1) car_headfiles.xacro: It defines three macro functions for calculating the inertial of box, sphere and cylinder.  
(2) car_base.xacro: It designs the car base, including 4 wheels, in term of their shape, size, location, color, inertial.  
(3) car_camera.xacro: It designs the camera, in term of its shape, size, location, color, inertial.   
(4) car_radar.xacro: It designs the laser, in term of its shape, size, location, color, inertial.   
(5) car_move.xacro: It contains differiential configuration of two wheels based on ros_control, inclduing joints, actuator as well as controller.  
(6) car_radar_info.xacro:  It configurates the laser info.  
(7) car_camera_info.xacro: It configurates the camera info.    
(8) car_kinect_info.xacro:  It configurates the kinect info.   
(9) worlds/box_house.world: It is the saved env in gazebo.  

Following two images show how the designed car looks like in the gazebo as well as rviz:  
![image](https://github.com/wenkaifool/ROS/tree/master/Robot/Robot_System_Simulation/Robot_Env_Modelling/image/gazebo.png)  
![image](https://github.com/wenkaifool/ROS/tree/master/Robot/Robot_System_Simulation/Robot_Env_Modelling/image/rviz.png)  
