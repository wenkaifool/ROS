#! /usr/bin/env python
# coding:utf-8

import rospy
from msg_demo.msg import Student


def subs_callback(msg):
    print ("姓名:{}, 年龄:{}, 身高:{}".format(msg.name, msg.age, msg.height))


if __name__ == "__main__":

    subscriber_node = 'person_sub'
    rospy.init_node(subscriber_node)

    topic_name = 'person_msgs'
    subs = rospy.Subscriber(topic_name, Student, subs_callback)

    rospy.spin()
    
    