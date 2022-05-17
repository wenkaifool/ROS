This demo is show a basic topic communicaiton beween the publisher node and the subscriber node based on a customized messages.  
First of all, there is a new folder called "msg" containing .msg files.  
1. Then the package.xml is supposed to be added with:  
   <build_depend>message_generation</build_depend>  
   <exec_depend>message_runtime</exec_depend>  
2. Then the CMakeList also should be modified:  
   find_package(catkin REQUIRED COMPONENTS  
   roscpp  
   rosmsg  
   rospy  
   message_generation)  
   add_message_files(  
         FILES  
         Student.msg)  
 generate_messages(  
         DEPENDENCIES  
         std_msgs)  
 catkin_package(  
 #  INCLUDE_DIRS include  
 #  LIBRARIES demo_msg  
    CATKIN_DEPENDS roscpp rosmsg rospy message_runtime  
 #  DEPENDS system_lib
 )    
3. If the IDE is vscode, then add the include path in c_cpp_properties.json:  
   "includePath": [  
        "/opt/ros/melodic/include/**",  
        "/usr/include/**",  
        "/home/wenkai/Desktop/ROSws/basic_ws/devel/include/**"  
      ]  
    as well as the settings.json:  
    "python.autoComplete.extraPaths": [  
        "/opt/ros/melodic/lib/python2.7/dist-packages",  
        "/home/wenkai/Desktop/ROSws/basic_ws/devel/lib/python2.7/dist-packages"  
    ]

For python files: make sure:  
(1) Env: python2.7 + ros:melodic.  
(2) Execute permission should be enabled for every python scripts.  
For cpp files:  
(1) packages needs following libraries:  
    roscpp rospy rosmsg std_msgs  
(2) Cmake lists should be modified by following sentences:  
    add_executable(01_print_publisher src/01_print_publisher.cpp)  
    add_dependencies(01_print_publisher ${${PROJECT_NAME}_EXPORTED_TARGETS} ${catkin_EXPORTED_TARGETS})  
    target_link_libraries(01_print_subscriber  
  	${catkin_LIBRARIES}  
    )  
