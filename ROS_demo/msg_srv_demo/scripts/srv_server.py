#!/usr/bin/env python
# coding:utf-8

import rospy
from msg_demo.msg import *
from msg_srv_demo.srv import FindTeam, FindTeamResponse, FindTeamRequest

def service_callback(request):
    if not isinstance(request, FindTeamRequest):
        return

    name = request.stu.name
    age = request.stu.age

    response = FindTeamResponse()

    team = Team()
    response.team = team
    response.team.name = 'Qiao' + name + 'age = {}'.format(age)

    return response


if __name__ == '__main__':

    node_name = 'team_service_node'
    rospy.init_node(node_name)

    service_name = '/find/team'
    rospy.Service(service_name, FindTeam, service_callback)

    rospy.spin()