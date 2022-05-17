#!/usr/bin/env python

import rospy
from std_msgs.msg import String


if __name__ == "__main__":

    node_name = 'print_publisher'
    rospy.init_node(node_name)

    # 创建发布者
    # 第一个参数为topic名称
    # 第二个参数为发布的消息类型
    # 第三个参数为topic中消息队列最多的数量。
    topic_name = 'basic_print' 
    publisher = rospy.Publisher(topic_name, String, queue_size=10)

    rate = rospy.Rate(10)

    count = 0

    # rospy.sleep(3)

    while not rospy.is_shutdown():
        
        msg = String()
        msg.data = 'hello {}'.format(count)
        publisher.publish(msg)
        count += 1
        rate.sleep()

