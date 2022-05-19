# amcl简介  
AMCL(adaptive Monte Carlo Localization) 是用于2D移动机器人的概率定位系统，它实现了自适应（或KLD采样）蒙特卡洛定位方法，可以根据已有地图使用粒子滤波器推算机器人位置.  

amcl节点说明  
amcl 功能包中的核心节点是:amcl。为了方便调用，需要先了解该节点订阅的话题、发布的话题、服务以及相关参数。  
1. 订阅的Topic  
   (1) scan(sensor_msgs/LaserScan) 激光雷达数据。  
   (2) tf(tf/tfMessage) 坐标变换消息。  
   (3) initialpose(geometry_msgs/PoseWithCovarianceStamped) 用来初始化粒子滤波器的均值和协方差。  
   (4) map(nav_msgs/OccupancyGrid) 获取地图数据。  

2. 发布的Topic
   (1) amcl_pose(geometry_msgs/PoseWithCovarianceStamped) 机器人在地图中的位姿估计。  
   (2) particlecloud(geometry_msgs/PoseArray) 位姿估计集合，rviz中可以被 PoseArray 订阅然后图形化显示机器人的位姿估计集合。  
   (3) tf(tf/tfMessage) 发布从 odom 到 map 的转换。  
3. 服务
   (1) global_localization(std_srvs/Empty) 初始化全局定位的服务。  
   (2) request_nomotion_update(std_srvs/Empty) 手动执行更新和发布更新的粒子的服务。  
   (3) set_map(nav_msgs/SetMap) 手动设置新地图和姿态的服务。  
4. 调用的服务  
   static_map(nav_msgs/GetMap)  调用此服务获取地图数据。  

5. 参数  
   (1) ~odom_model_type(string, default:"diff")  
       里程计模型选择: "diff","omni","diff-corrected","omni-corrected" (diff 差速、omni 全向轮)  
   (2) ~odom_frame_id(string, default:"odom") 里程计坐标系。  
   (3) ~base_frame_id(string, default:"base_link") 机器人极坐标系。  
   (4) ~global_frame_id(string, default:"map") 地图坐标系。  

