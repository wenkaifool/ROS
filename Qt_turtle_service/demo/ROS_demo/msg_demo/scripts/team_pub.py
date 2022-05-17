#!/usr/bin/env python
# coding: utf-8

import rospy
from msg_demo.msg import Team, Student

if __name__ == '__main__':
    node_name = 'team_publisher'
    rospy.init_node(node_name)

    topic_name = '/team'

    publisher = rospy.Publisher(topic_name, Team, queue_size=1000)

    rate = rospy.Rate(2)
    index = 0

    while not rospy.is_shutdown():
        msg = Team()
        msg.name = 'Ciao Ciao {}'.format(index)
        msg.leader.age = index
        msg.intro.data = 'ByeBye'
        msg.leader.name = 'Rain'
        msg.location.position.x = 1.

        # member is list
        for i in range(3):
            stu = Student()
            stu.name = 'member {}'.format(i)
            stu.age = 2 * i
            msg.members.append(stu)

        publisher.publish(msg)
        index += 1
        rate.sleep()
