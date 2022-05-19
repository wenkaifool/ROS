pluginlib是一个c++库， 用来从一个ROS功能包中加载和卸载插件(plugin)。所谓插件字面意思就是可插拔的组件，比如:以计算机为例，可以通过USB接口自由插拔的键盘、鼠标、U盘...都可以看作是插件实现，其基本原理就是通过规范化的USB接口协议实现计算机与USB设备的自由组合。同理，在软件编程中，插件是一种遵循一定规范的应用程序接口编写出来的程序，插件程序依赖于某个应用程序，且应用程序可以与不同的插件程序自由组合。在ROS中，也会经常使用到插件，场景如下:  
(1) 导航插件:在导航中，涉及到路径规划模块，路径规划算法有多种，也可以自实现，导航应用时，可能需要测试不同算法的优劣以选择更合适的实现，这种场景下，ROS中就是通过插件的方式来实现不同算法的灵活切换的。 
(2) rviz插件:在rviz中已经提供了丰富的功能实现，但是即便如此，特定场景下，开发者可能需要实现某些定制化功能并集成到rviz中，这一集成过程也是基于插件的。 

需求: 以插件的方式实现正多边形的相关计算。  
实现流程:  
1. 创建功能包xxx导入依赖: roscpp pluginlib   
2. 创建基类: 在 xxx/include/xxx下新建C++头文件: polygon_base.h，所有的插件类都需要继承此基类。  
   需要注意的是，基类必须提供无参构造函数，所以关于多边形的边长没有通过构造函数而是通过单独编写的initialize函数传参。 
3. 创建插件类: 在 xxx/include/xxx下新建C++头文件:polygon_plugins.h
4. 注册插件: 在 src 目录下新建 polygon_plugins.cpp 文件  
5. 构建插件库:  
   include_directories(include)  
   add_library(polygon_plugins src/polygon_plugins.cpp)  
至此，可以调用 catkin_make 编译，编译完成后，在工作空间/devel/lib目录下，会生成相关的 .so 文件。  
6. 使插件可用于ROS工具链;  
(1) 配置xml: 插件类+基类  
(2) 导出插件：packkage.xml   
    标签<xxx />的名称应与基类所属的功能包名称一致，plugin属性值为上一步中创建的xml文件。 
7. 使用插件;  

source: http://www.autolabor.com.cn/book/ROSTutorials/di-7-zhang-ji-qi-ren-dao-822a28-fang-771f29/104-pluginlib.html