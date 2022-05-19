#! /usr/bin/env python
# coding:utf-8
"""
    需求: 
        编写两个节点实现服务通信，客户端节点需要提交两个整数到服务器
        服务器需要解析客户端提交的数据，相加后，将结果响应回客户端，
        客户端再解析

    服务器端实现:
        1.导包
        2.初始化 ROS 节点
        3.创建服务对象
        4.回调函数处理请求并产生响应
        5.spin 函数

"""
# 1.导包
import rospy
from srv_demo.srv import AddInts,AddIntsRequest,AddIntsResponse
# 回调函数的参数是请求对象，返回值是响应对象

def service_callback(req):
    if not isinstance(req, AddIntsRequest):
        return
    sum = req.num1 + req.num2

    resp = AddIntsResponse()
    resp.sum = sum

    return resp


if __name__ == "__main__":
    node_name = "addserver"
    rospy.init_node(node_name)

    service_name = "addints"
    server = rospy.Service(service_name, AddInts, service_callback)

    rospy.spin()