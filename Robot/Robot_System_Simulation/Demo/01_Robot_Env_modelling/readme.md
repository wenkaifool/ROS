当 URDF 需要与 Gazebo 集成时，和 Rviz 有明显区别:  
1.必须使用 collision 标签，因为既然是仿真环境，那么必然涉及到碰撞检测，collision 提供碰撞检测的依据。  
2.必须使用 inertial 标签，此标签标注了当前机器人某个刚体部分的惯性矩阵，用于一些力学相关的仿真计算。  
3.颜色设置，也需要重新使用 gazebo 标签标注，因为之前的颜色设置为了方便调试包含透明度，仿真环境下没有此选项。  
4.此外还需要使用运行文件打开gazebo及其环境：  
  (1) 启动 Gazebo 的仿真环境，当前环境为空环境  
      include file="$(find gazebo_ros)/launch/empty_world.launch"  
  (2) 在 Gazebo 中加载一个机器人模型，该功能由 gazebo_ros 下的 spawn_model 提供:  
      node pkg="gazebo_ros" type="spawn_model" name="model" args="-urdf -model mycar -param robot_description"  
      -urdf 加载的是 urdf 文件  
      -model mycar 模型名称是 mycar  
      -param robot_description 从参数 robot_description 中载入模型  
      -x 模型载入的 x 坐标  
      -y 模型载入的 y 坐标  
      -z 模型载入的 z 坐标  
5. 最后是他的依赖包： urdf、xacro、gazebo_ros、gazebo_ros_control、gazebo_plugins  
需要注意的是：每次运行前先rosnode cleanup来保证gazebo节点不会重复运行。  

  
