#!/usr/bin/env python
# coding:utf-8

import rospy
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsRequest,AddTwoIntsResponse

def server_callback(request):
    if not isinstance(request, AddTwoIntsRequest):
        return

    # 获取请求数据
    a = request.a
    b = request.b

    # 返回响应结果
    response = AddTwoIntsResponse()
    response.sum = a + b

    return response

if __name__ == '__main__':
    # 创建节点
    nodeName = "my_server_node"
    rospy.init_node(nodeName)

    # 创建Service Server
    serviceName = "my_service"
    rospy.Service(serviceName, AddTwoInts, server_callback)

    # 阻塞线程
    rospy.spin()