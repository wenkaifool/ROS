#! /usr/bin/env python
# coding: utf-8

from ast import Expression
from cmd import IDENTCHARS
from logging.config import IDENTIFIER
import rospy
from turtlesim.srv import Spawn, SpawnRequest, SetPenResponse


if __name__ == "__main__":

    node_name = "turtle_service"

    rospy.init_node(node_name)

    service_name = "/spawn"
    client = rospy.ServiceProxy(service_name, Spawn)

    client.wait_for_service()

    spawn = SpawnRequest()
    spawn.x = 2.0
    spawn.y = 2.0
    spawn.theta = -1.57
    spawn.name = "my_turtle_p"

    try:
        response = client.call(spawn)
        rospy.loginfo("乌龟创建成功!，叫:%s",response.name)
    except:
        rospy.loginfo("服务调用失败")
