TF坐标变换，实现不同类型的坐标系之间的转换.  
1. Necessary packages when create the package:  
   tf2、tf2_ros、tf2_geometry_msgs、roscpp rospy std_msgs geometry_msgs
2. Package introduction:  
   (1) tf2_geometry_msgs:可以将ROS消息转换成tf2消息。  
   (2) tf2: 封装了坐标变换的常用消息。 
   (3) tf2_ros:为tf2提供了roscpp和rospy绑定，封装了坐标变换常用的API。 

订阅发布模型中数据载体 msg 是一个重要实现，首先需要了解一下，在坐标转换实现中常用的 msg:geometry_msgs/TransformStamped和geometry_msgs/PointStamped. 前者用于传输坐标系相关位置信息，后者用于传输某个坐标系内坐标点的信息。在坐标变换中，频繁的需要使用到坐标系的相对关系以及坐标点信息。  

静态坐标转换---两个坐标系之间的相对位置是固定的  
1. 需求描述:  
   现有一机器人模型，核心构成包含主体与雷达，各对应一坐标系，坐标系的原点分别位于主体与雷达的物理中心，已知雷达原点相对于主体原点位移关系如下: x 0.2 y0.0 z0.5。当前雷达检测到一障碍物，在雷达坐标系中障碍物的坐标为 (2.0 3.0 5.0),请问，该障碍物相对于主体的坐标是多少？ 
2. 实现分析:  
   (1) 坐标系相对关系，可以通过发布方发布;  
   (2) 订阅方，订阅到发布的坐标系相对关系，再传入坐标点信息(可以写死)，然后借助于 tf 实现坐标变换，并将结果输出.  
![image](https://github.com/wenkaifool/ROS_turtleplay/blob/master/Qt_turtle_service/demo/ROS_demo/tf_demo/image/static_tf_in_rviz.png)  
动态坐标变换  
1. 需求描述:  
   启动 turtlesim_node,该节点中窗体有一个世界坐标系(左下角为坐标系原点)，乌龟是另一个坐标系，键盘控制乌龟运动，将两个坐标系的相对位置动态发布。 
2. 实现分析:  
   (1) 乌龟本身不但可以看作坐标系，也是世界坐标系中的一个坐标点  
   (2) 订阅 turtle1/pose,可以获取乌龟在世界坐标系的 x坐标、y坐标、偏移量以及线速度和角速度  
   (3) 将 pose 信息转换成 坐标系相对信息并发布  
![image](https://github.com/wenkaifool/ROS_turtleplay/blob/master/Qt_turtle_service/demo/ROS_demo/tf_demo/image/dynamic_tf_in_rviz.png)  
多坐标变换  
1. 需求描述:  
   现有坐标系统，父级坐标系统 world,下有两子级系统 son1，son2，son1 相对于 world，以及 son2 相对于 world 的关系是已知的，求 son1原点在 son2中的坐标，又已知在 son1中一点的坐标，要求求出该点在 son2 中的坐标.  
2. 实现分析:  
   (1) 首先，需要发布 son1 相对于 world，以及 son2 相对于 world 的坐标消息  
   (2) 然后，需要订阅坐标发布消息，并取出订阅的消息，借助于 tf2 实现 son1 和 son2 的转换  
   (3) 最后，还要实现坐标点的转换  
3. 对于发布方，为了方便，使用launch文件静态坐标变换发布。
![image](https://github.com/wenkaifool/ROS_turtleplay/blob/master/Qt_turtle_service/demo/ROS_demo/tf_demo/image/multi_tf_in_rviz.png)  
