#! /usr/bin/env python

import rospy
from msg_demo.msg import Student

if __name__ == "__main__":

    publisher_node = 'person_pub'
    rospy.init_node(publisher_node)

    topic_name = 'person_msgs'
    pubs = rospy.Publisher(topic_name, Student, queue_size=1000)

    rate = rospy.Rate(2)

    count = 0
    while not rospy.is_shutdown():

        person = Student()
        person.name = 'Qiao'
        person.age = 27
        person.height = 1.72

        pubs.publish(person)

        count += 1
        rate.sleep()
    
    