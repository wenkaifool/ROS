This project shows how to achieve a communication between the turtle game of ROS and the QT GUI via service, i.e. the turtle game is a "server" while the QT GUI is a "client".  
Here are required packages:  
(1) Language: python 2.7  
(2) ROS: Melodic  
(3) Qt.  
Here are some installation commands:  
(1) ROS installation  
    sudo apt install ros-melodic-desktop-full  
(2) Qt installtion:  
    pip install pyqt  
Once the environmet is completed, then run following commands:  
(1) open the turtle game  
    rosrun turtlesim turtlesim_node  
(2) open the Qt window  
    python Qt_ROSturtle.py  
The result would be shown as the image below, if everything is fine:  

The more dedailed tutorial could be found here:https://robot.czxy.com/car/pyqt/env/



