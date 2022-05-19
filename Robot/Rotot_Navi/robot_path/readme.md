# move_base简介  

move_base 功能包提供了基于动作(action)的路径规划实现，move_base 可以根据给定的目标点，控制机器人底盘运动至目标位置，并且在运动过程中会连续反馈机器人自身的姿态与目标点的状态信息。如前所述(7.1)move_base主要由全局路径规划与本地路径规划组成。move_base功能包中的核心节点是:move_base。为了方便调用，需要先了解该节点action、订阅的话题、发布的话题、服务以及相关参数。  
1. 动作  
   (1) 动作订阅  
       move_base/goal(move_base_msgs/MoveBaseActionGoal) move_base 的运动规划目标。  
       move_base/cancel(actionlib_msgs/GoalID) 取消目标。  
   (2) 动作发布  
       move_base/feedback(move_base_msgs/MoveBaseActionFeedback) 连续反馈的信息，包含机器人底盘坐标。  
       move_base/status(actionlib_msgs/GoalStatusArray) 发送到move_base的目标状态信息。  
       move_base/result(move_base_msgs/MoveBaseActionResult) 操作结果(此处为空)。  
2. 订阅的Topic  
   move_base_simple/goal(geometry_msgs/PoseStamped) 运动规划目标(与action相比，没有连续反馈，无法追踪机器人执行状态)。  
3. 发布的Topic  
   cmd_vel(geometry_msgs/Twist) 输出到机器人底盘的运动控制消息。  
4. 服务  
   ~make_plan(nav_msgs/GetPlan) 请求该服务，可以获取给定目标的规划路径，但是并不执行该路径规划。  
   ~clear_unknown_space(std_srvs/Empty) 允许用户直接清除机器人周围的未知空间。  
   ~clear_costmaps(std_srvs/Empty) 允许清除代价地图中的障碍物，可能会导致机器人与障碍物碰撞，请慎用。  


move_base与代价地图  
概念  
机器人导航(尤其是路径规划模块)是依赖于地图的，地图在SLAM时已经有所介绍了，ROS中的地图其实就是一张图片，这张图片有宽度、高度、分辨率等元数据，在图片中使用灰度值来表示障碍物存在的概率。不过SLAM构建的地图在导航中是不可以直接使用的，因为：  
(1) SLAM构建的地图是静态地图，而导航过程中，障碍物信息是可变的，可能障碍物被移走了，也可能添加了新的障碍物，导航中需要时时的获取障碍物信息；  
(2) 在靠近障碍物边缘时，虽然此处是空闲区域，但是机器人在进入该区域后可能由于其他一些因素，比如：惯性、或者不规则形体的机器人转弯时可能会与障碍物产生碰撞，安全起见，最好在地图的障碍物边缘设置警戒区，尽量禁止机器人进入...  
所以，静态地图无法直接应用于导航，其基础之上需要添加一些辅助信息的地图，比如时时获取的障碍物数据，基于静态地图添加的膨胀区等数据。  

组成  
代价地图有两张:global_costmap(全局代价地图) 和 local_costmap(本地代价地图)，前者用于全局路径规划，后者用于本地路径规划。  
两张代价地图都可以多层叠加,一般有以下层级:  
(1) Static Map Layer：静态地图层，SLAM构建的静态地图。  
(2) Obstacle Map Layer：障碍地图层，传感器感知的障碍物信息。  
(3) Inflation Layer：膨胀层，在以上两层地图上进行膨胀（向外扩张），以避免机器人的外壳会撞上障碍物。  
(4) Other Layers：自定义costmap。 

在ROS中，如何计算代价值呢？请看下图:  
![image](https://github.com/wenkaifool/ROS/blob/master/Robot/Rotot_Navi/overall/image/collision.png)


source: http://www.autolabor.com.cn/book/ROSTutorials/di-7-zhang-ji-qi-ren-dao-822a28-fang-771f29/72-dao-hang-shi-xian/724-dao-hang-shi-xian-04-lu-jing-gui-hua.html
