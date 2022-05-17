#! /usr/bin/env python
# coding:utf-8

import rospy, sys
from srv_demo.srv import AddInts,AddIntsRequest,AddIntsResponse

if __name__ == "__main__":

    #优化实现
    if len(sys.argv) != 3:
        print (len(sys.argv))
        rospy.logerr("请正确提交参数")
        sys.exit(1)

    node_name = "addclient"
    rospy.init_node(node_name)

    service_name = "addints"
    client = rospy.ServiceProxy(service_name, AddInts)
    client.wait_for_service()
    # 4.发送请求,接收并处理响应
    # 方式1
    # resp = client(3,4)
    # 方式2
    # resp = client(AddIntsRequest(1,5))
    # 方式3
    req = AddIntsRequest()
    # req.num1 = 100
    # req.num2 = 200 

    #优化
    req.num1 = int(sys.argv[1])
    req.num2 = int(sys.argv[2])


    try:
        resp = client.call(req)

        if isinstance(resp, AddIntsResponse):
            rospy.loginfo("响应结果:%d",resp.sum)
    except Exception:
        rospy.loginfo('arg error')

    # rospy.spin()


