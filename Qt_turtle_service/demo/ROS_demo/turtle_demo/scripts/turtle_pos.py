#! /usr/bin/env python
# coding: utf-8

import rospy
from turtlesim.msg import Pose

def subs_callback(data):
    if not isinstance(data, Pose):
        return

    rospy.loginfo("乌龟坐标:x=%.2f, y=%.2f,theta=%.2f",data.x,data.y,data.theta)

if __name__ == "__main__":

    node_name = "turtle_pos"

    rospy.init_node(node_name)

    topic_name = "/turtle1/pose"
    sub = rospy.Subscriber(topic_name, Pose, subs_callback)

    rospy.spin()