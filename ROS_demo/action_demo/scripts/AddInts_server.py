#!/usr/bin/env python
#coding:utf-8

import rospy
import actionlib
from action_demo.msg import *

class MyActionServer(object):

    def __init__(self):
        self.server = actionlib.SimpleActionServer("addInts", AddIntsAction, self.execute_cb, False)
        self.server.start()
        rospy.loginfo("服务端启动")

    def execute_cb(self, goal):
        if not isinstance (goal, AddIntsGoal):
            return

        rospy.loginfo("服务端处理请求:")
        num = goal.num
        rate = rospy.Rate(10)
        sum = 0

        for i in range(1, num+1):
            sum = sum + i
            num = num + 1.0 -1.0
            # 计算进度并连续反馈
            feedBack = i / num
            rospy.loginfo("当前进度:{}".format(feedBack))

            feedBack_obj = AddIntsFeedback()
            feedBack_obj.progress_bar = feedBack
            self.server.publish_feedback(feedBack_obj)
            rate.sleep()
        
        result = AddIntsResult()
        result.result = sum
        self.server.set_succeeded(result)
        rospy.loginfo("响应结果:%d",sum)


if __name__ == "__main__":
    node_name = "AddInts_server"
    rospy.init_node(node_name)

    server = MyActionServer()
    rospy.spin()