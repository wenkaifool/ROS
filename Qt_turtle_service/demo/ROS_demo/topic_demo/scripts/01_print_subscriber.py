#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def subscirber_callback(msg):
    print (msg)


if __name__ == "__main__":

    node_name = 'print_subscriber'
    rospy.init_node(node_name)

    topic_name = 'basic_print' 
    subscirber = rospy.Subscriber(topic_name, String, callback=subscirber_callback)

    rospy.spin()
