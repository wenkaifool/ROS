#!/usr/bin/env python
#coding:utf-8

import rospy
import actionlib
from action_demo.msg import *


def done_cb(state,result):
    if state == actionlib.GoalStatus.SUCCEEDED:
        rospy.loginfo("响应结果:%d",result.result)

def active_cb():
    rospy.loginfo("服务被激活....")


def fb_cb(fb):
    rospy.loginfo("当前进度:%.2f",fb.progress_bar)

if __name__ == "__main__":
    node_name = "AddInts_client"
    rospy.init_node(node_name)

    client = actionlib.SimpleActionClient("addInts",AddIntsAction)
    client.wait_for_server()

    goal = AddIntsGoal()
    goal.num = 10
    client.send_goal(goal, done_cb, active_cb, fb_cb)
    
    rospy.spin()