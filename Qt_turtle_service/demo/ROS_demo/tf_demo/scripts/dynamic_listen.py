#!/usr/bin/env python
# coding:utf-8

from logging import exception
import tf.transformations
import rospy
from turtlesim.msg import Pose
import tf2_ros
from tf2_geometry_msgs import PointStamped


if __name__ == "__main__":
    node_name = "dynamic_listen"
    rospy.init_node(node_name)
    
    buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(buffer)

    rate = rospy.Rate(1)

    while not rospy.is_shutdown():
        point_source = PointStamped()
        point_source.header.frame_id = "turtle1"
        point_source.header.stamp = rospy.Time()
        point_source.point.x = 10
        point_source.point.y = 2
        point_source.point.z = 3
        try:
            point_target = buffer.transform(point_source,"world",rospy.Duration(1))
            
            rospy.loginfo("转换结果:x = %.2f, y = %.2f, z = %.2f",
                            point_target.point.x,
                            point_target.point.y,
                            point_target.point.z)

        except exception as e:
            rospy.logerr("异常: %s", e)

        rate.sleep()

    