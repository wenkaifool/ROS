#!/usr/bin/env python
# coding:utf-8
import rospy
from tf2_ros import StaticTransformBroadcaster, TransformListener
import tf
from geometry_msgs.msg import TransformStamped
import tf.transformations

if __name__ == "__main__":

    node_name = "static_broadcast"
    rospy.init_node(node_name)

    # 3.创建 静态坐标广播器
    broadcaster = StaticTransformBroadcaster()

    # 4.创建并组织被广播的消息
    tf_msg = TransformStamped()

    # --- 头信息
    tf_msg.header.frame_id = "world"
    tf_msg.header.stamp = rospy.Time.now()
    tf_msg.header.seq = 101
    # --- 子坐标系
    tf_msg.child_frame_id = "radar"
    # --- 坐标系相对信息
    # ------ 偏移量
    tf_msg.transform.translation.x = 0.2
    tf_msg.transform.translation.y = 0.0
    tf_msg.transform.translation.z = 0.5
    # ------ 四元数
    qtn = tf.transformations.quaternion_from_euler(0,0,0)
    tf_msg.transform.rotation.x = qtn[0]
    tf_msg.transform.rotation.y = qtn[1]
    tf_msg.transform.rotation.z = qtn[2]
    tf_msg.transform.rotation.w = qtn[3]

    broadcaster.sendTransform(tf_msg)

    rospy.spin()




    