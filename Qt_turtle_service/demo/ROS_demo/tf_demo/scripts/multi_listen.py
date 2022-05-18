#!/usr/bin/env python
#coding:utf-8

import rospy
import tf2_ros
from geometry_msgs.msg import TransformStamped
from tf2_geometry_msgs import PointStamped

if __name__ =="__main__":
    node_name = "multi_listen"
    rospy.init_node(node_name)

    buffer = tf2_ros.Buffer()
    listener = tf2_ros.TransformListener(buffer)

    r = rospy.Rate(1)

    while not rospy.is_shutdown():
        try:
            tfs = TransformStamped()
            tfs = buffer.lookup_transform("son2", "son1", rospy.Time(0))
            rospy.loginfo("son1 与 son2 相对关系:")
            rospy.loginfo("父级坐标系:%s",tfs.header.frame_id)
            rospy.loginfo("子级坐标系:%s",tfs.child_frame_id)
            rospy.loginfo("相对坐标:x=%.2f, y=%.2f, z=%.2f",
                        tfs.transform.translation.x,
                        tfs.transform.translation.y,
                        tfs.transform.translation.z,
            )
            # 创建一依赖于 son1 的坐标点，调用 API 求出该点在 son2 中的坐标
            point_source = PointStamped()
            point_source.header.frame_id = "son1"
            point_source.header.stamp = rospy.Time.now()
            point_source.point.x = 1
            point_source.point.y = 1
            point_source.point.z = 1

            point_target = buffer.transform(point_source,"son2",rospy.Duration(0.5))
            rospy.loginfo("point_target 所属的坐标系:%s",point_target.header.frame_id)
            rospy.loginfo("坐标点相对于 son2 的坐标:(%.2f,%.2f,%.2f)",
                        point_target.point.x,
                        point_target.point.y,
                        point_target.point.z
            )


        except Exception as e:
            rospy.logwarn("异常情况: %s", e)
