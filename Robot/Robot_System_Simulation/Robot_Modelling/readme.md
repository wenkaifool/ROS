# Arbotix

Arbotix 是一款控制电机、舵机的控制板，并提供相应的 ros 功能包，这个功能包的功能不仅可以驱动真实的 Arbotix 控制板，它还提供一个差速控制器，通过接受速度控制指令更新机器人的 joint 状态，从而帮助我们实现机器人在 rviz 中的运动。这个差速控制器在 arbotix_python 程序包中，完整的 arbotix 程序包还包括多种控制器，分别对应 dynamixel 电机、多关节机械臂以及不同形状的夹持器。  

需求描述:  
控制机器人模型在 rviz 中做圆周运动。  

实现流程:  
(1) 添加 Arbotix 配置文件，格式为yaml。 
    另请参考: http://wiki.ros.org/arbotix_python/diff_controller   
(2) 编写 launch 文件配置 Arbotix  
    代码解释:  
    node:调用了 arbotix_python 功能包下的 arbotix_driver 节点  
    rosparam: arbotix 驱动机器人运行时，需要获取机器人信息，可以通过 file 加载配置文件  
    param: 在仿真环境下，需要配置 sim 为 true
(3) 启动 launch 文件并控制机器人模型运动  
    启动之后，此时调用 rostopic list 会发现一个熟悉的话题: /cmd_vel，则以通过如下命令来控制小车运动：  
    rostopic pub -r 10 /cmd_vel geometry_msgs/Twist '{linear: {x: 0.2, y: 0, z: 0}, angular: {x: 0, y: 0, z: 0.5}}'
