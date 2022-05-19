# gmapping简介  
gmapping 是ROS开源社区中较为常用且比较成熟的SLAM算法之一，gmapping可以根据移动机器人里程计数据和激光雷达数据来绘制二维的栅格地图，对应的，gmapping对硬件也有一定的要求:  
(1) 该移动机器人可以发布里程计消息  
(2) 机器人需要发布雷达消息(该消息可以通过水平固定安装的雷达发布，或者也可以将深度相机消息转换成雷达消息)  

gmapping节点说明  
gmapping 功能包中的核心节点是:slam_gmapping。为了方便调用，需要先了解该节点订阅的话题、发布的话题、服务以及相关参数。  
1. 订阅的Topic: 
   (1) tf (tf/tfMessage) 用于雷达、底盘与里程计之间的坐标变换消息。  
   (2) scan(sensor_msgs/LaserScan) SLAM所需的雷达信息  
2. 发布的Topic:  
   (1) map_metadata(nav_msgs/MapMetaData)  
       地图元数据，包括地图的宽度、高度、分辨率等，该消息会固定更新。  
   (2) map(nav_msgs/OccupancyGrid)  
       地图栅格数据，一般会在rviz中以图形化的方式显示。
   (3) ~entropy(std_msgs/Float64)  
       机器人姿态分布熵估计(值越大，不确定性越大)。  
3. 服务  
   (1) dynamic_map(nav_msgs/GetMap): 用于获取地图数据。  
4. 参数  
   ~base_frame(string, default:"base_link") 机器人基坐标系。  
   ~map_frame(string, default:"map")  地图坐标系。  
   ~odom_frame(string, default:"odom")  里程计坐标系。  
   ~map_update_interval(float, default: 5.0)  地图更新频率，根据指定的值设计更新间隔。   
   ~maxUrange(float, default: 80.0) 激光探测的最大可用范围(超出此阈值，被截断)。  
   ~maxRange(float)  激光探测的最大范围。  
5. 所需的坐标变换:  
   (1) 雷达坐标系→基坐标系  
       一般由 robot_state_publisher 或 static_transform_publisher 发布。  
   (2) 基坐标系→里程计坐标系  
       一般由里程计节点发布。  
6. 发布的坐标变换  
   地图坐标系→里程计坐标系: 地图到里程计坐标系之间的变换。  

执行  
1.先启动 Gazebo 仿真环境(此过程略)  
2.然后再启动地图绘制的 launch 文件   
  launch文件编写可以参考 github 的演示 launch文件：https://github.com/ros-perception/slam_gmapping/blob/melodic-devel/gmapping/launch/slam_gmapping_pr2.launch  
3.启动键盘键盘控制节点，用于控制机器人运动建图  
  rosrun teleop_twist_keyboard teleop_twist_keyboard.py  
4.在 rviz 中添加组件，显示栅格地图  

![image](https://github.com/wenkaifool/ROS/blob/master/Robot/Rotot_Navi/overall/image/gmapping_map.png)
