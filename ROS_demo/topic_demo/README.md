This demo is show a basic topic communicaiton beween the publisher node and the subscriber node.  
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
