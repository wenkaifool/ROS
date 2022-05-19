#!/usr/bin/env python
# coding: utf-8

import rospy
from msg_demo.msg import Team, Student


def topic_callback(msg):
    if not isinstance(msg, Team):
        return
    print ('name:', msg.name, 'age=', msg.leader.age, 'name = ', msg.leader.name)
    print (msg)


if __name__ == '__main__':
    node_name = 'team_subscriber'
    rospy.init_node(node_name)

    topic_name = '/team'

    subscriber = rospy.Subscriber(topic_name, Team, topic_callback)

    rospy.spin()