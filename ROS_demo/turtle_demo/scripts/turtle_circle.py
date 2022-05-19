#! /usr/bin/env python
# coding: utf-8

import rospy
from geometry_msgs.msg import Twist

if __name__ == "__main__":

    node_name = "turtle_circle_py"

    rospy.init_node(node_name)

    topic_name = "/turtle1/cmd_vel"
    pub = rospy.Publisher(topic_name, Twist, queue_size=1000)

    rate = rospy.Rate(10)

    msg = Twist()
    msg.linear.x = 1.0
    msg.linear.y = 0.0
    msg.linear.z = 0.0
    msg.angular.x = 0.0
    msg.angular.y = 0.0
    msg.angular.z = 0.5

    while not rospy.is_shutdown():
        pub.publish(msg)
        rate.sleep()