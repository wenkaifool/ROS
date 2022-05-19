#!/usr/bin/env python
# coding:utf-8

import rospy
from rospy_tutorials.srv import AddTwoInts, AddTwoIntsRequest, AddTwoIntsResponse

if __name__ == '__main__':
    # 创建节点
    nodeName = "my_client_node"
    rospy.init_node(nodeName)

    # 创建Service Client
    serviceName = "my_service"
    client = rospy.ServiceProxy(serviceName, AddTwoInts)

    # 等待服务开启
    rospy.wait_for_service(serviceName)

    # 创建请求数据
    request = AddTwoIntsRequest()
    request.a = 4
    request.b = 5
    # 调用服务并且获得响应结果
    response = client.call(request)

    if isinstance(response, AddTwoIntsResponse):
        rospy.loginfo("响应结果: %d" % response.sum)

    # 阻塞线程
    rospy.spin() 