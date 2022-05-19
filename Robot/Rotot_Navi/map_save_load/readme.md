# map_server简介  
map_server功能包中提供了两个节点: map_saver 和 map_server，前者用于将栅格地图保存到磁盘，后者读取磁盘的栅格地图并以服务的方式提供出去。  

1. map_saver  
   订阅的topic:map(nav_msgs/OccupancyGrid) 订阅此话题用于生成地图文件.  
   首先，参考上一节，依次启动仿真环境，键盘控制节点与SLAM节点；  
   然后，通过键盘控制机器人运动并绘图；  
   最后，通过上述地图保存方式保存地图。  
   结果：在指定路径下会生成两个文件，xxx.pgm 与 xxx.yaml  
   (1) xxx.pgm 本质是一张图片，直接使用图片查看程序即可打开。  
   (2) xxx.yaml 保存的是地图的元数据信息，用于描述图片，内容格式如下:  
       image:被描述的图片资源路径，可以是绝对路径也可以是相对路径。  
       resolution: 图片分片率(单位: m/像素)。  
       origin: 地图中左下像素的二维姿势，为（x，y，偏航），偏航为逆时针旋转（偏航= 0表示无旋转）。  
       occupied_thresh: 占用概率大于此阈值的像素被视为完全占用。  
       free_thresh: 占用率小于此阈值的像素被视为完全空闲。   
       negate: 是否应该颠倒白色/黑色自由/占用的语义。  
       map_server 中障碍物计算规则:  
       地图中的每一个像素取值在 [0,255] 之间，白色为 255，黑色为 0，该值设为 x； map_server 会将像素值作为判断是否是障碍物的依据，首先计算比例: p = (255 - x) / 255.0，白色为0，黑色为1(negate为true，则p = x / 255.0)； 根据步骤2计算的比例判断是否是障碍物，如果 p > occupied_thresh 那么视为障碍物，如果 p < free_thresh 那么视为无物。  

2. map_server  
   (1) 发布的话题  
       map_metadata（nav_msgs / MapMetaData） 发布地图元数据。  
       map（nav_msgs / OccupancyGrid）地图数据。  
   (2) 服务  
       static_map（nav_msgs / GetMap） 通过此服务获取地图。  
   (3) 参数   
       〜frame_id（字符串，默认值：“map”） 地图坐标系  

