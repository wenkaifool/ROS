#! /usr/bin/env python
# coding:utf-8

import rospy

if __name__ == "__main__":
    node_name = "turtle_param"
    rospy.init_node(node_name)

    # rospy.set_param("/turtlesim/background_r",255)
    # rospy.set_param("/turtlesim/background_g",255)
    # rospy.set_param("/turtlesim/background_b",255)
    rospy.set_param("background_r",0)
    rospy.set_param("background_g",0)
    rospy.set_param("background_b",0)  # 调用时，在命令窗口需要传入arg: __ns:=/turtlesim