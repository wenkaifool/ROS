#!/usr/bin/env python
# coding:utf-8

import rospy
from msg_srv_demo.srv import FindTeam, FindTeamResponse, FindTeamRequest
from msg_demo.msg import *

if __name__ == '__main__':
    node_name = 'client_node'
    rospy.init_node(node_name)

    service_name = '/find/team'

    client = rospy.ServiceProxy(service_name, FindTeam)
    client.wait_for_service()

    request = FindTeamRequest()

    request.stu.name = 'ByeBye'
    request.stu.age = 27

    try:
        response = client.call(request)

        if isinstance(response, FindTeamResponse):
            print (response.team)

    except Exception:
        rospy.loginfo('arg error')

    rospy.spin()