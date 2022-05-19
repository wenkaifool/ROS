#!/usr/bin/env python
# coding:utf-8

import tf.transformations
import rospy
from turtlesim.msg import Pose
import tf2_ros
from geometry_msgs.msg import TransformStamped


def subs_callback(pose):
    if not isinstance(pose, Pose):
        return

    broadcaster = tf2_ros.TransformBroadcaster()
    turtle_points = TransformStamped()

    turtle_points.header.frame_id = "world"
    turtle_points.header.stamp = rospy.Time.now()
    turtle_points.child_frame_id = "turtle1"
    turtle_points.transform.translation.x = pose.x
    turtle_points.transform.translation.y = pose.y
    turtle_points.transform.translation.z = 0.0

    qtn = tf.transformations.quaternion_from_euler(0,0,pose.theta)
    turtle_points.transform.rotation.x = qtn[0]
    turtle_points.transform.rotation.y = qtn[1]
    turtle_points.transform.rotation.z = qtn[2]
    turtle_points.transform.rotation.w = qtn[3]

    broadcaster.sendTransform(turtle_points)

if __name__ == "__main__":
    node_name = "dynamic_broadcast"
    rospy.init_node(node_name)
    topic_name = "/turtle1/pose"
    rospy.Subscriber(topic_name, Pose, subs_callback)
    rospy.spin()