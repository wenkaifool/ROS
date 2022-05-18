#! /usr/bin/env python
#coding:utf-8
import rospy
import rosbag
from std_msgs.msg import String

if __name__ == "__main__":
    #初始化节点 
    rospy.init_node("w_bag_p")

    # 创建 rosbag 对象
    bag = rosbag.Bag("hello_p.bag",'w')

    # 写数据
    s = String()
    s.data= "hahahaha"

    bag.write("chatter",s)
    bag.write("chatter",s)
    bag.write("chatter",s)
    # 关闭流
    bag.close()
