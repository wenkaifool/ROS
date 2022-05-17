#!/usr/bin/env python
# coding:utf-8

import rospy
import serial
import struct
from std_msgs.msg import Int32, Float32

def subscriber_callback(msg):
    if not isinstance(msg, Int32):
        return

    pwm = msg.data

    pack = struct.pack('h', pwm)

    data = bytearray([0x03, pack[0], pack[1]])
    ser.write(data)


if __name__ == '__main__':
    node_name = 'topic_driver_node'
    rospy.init_node(node_name)

    count = 0
    while count < 10:
        count += 1
        try:
            ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
            break
        except Exception as e:
            print (e)

    motor_topic_name = '/motor'
    rospy.Subscriber(motor_topic_name, Int32, subscriber_callback)

    # 编码器
    encode_topic_name = '/rpm'
    rpm_publisher = rospy.Publisher(encode_topic_name, Float32, queue_size=1000)

    # 和下位机通信
    while not rospy.is_shutdown():
        read = ser.read(2)
        data = bytearray([])
        data.extend(read)

        data = struct.unpack('h', data)[0]
        rpm = data/100.0

        msg = Float32()
        msg.data = rpm
        rpm_publisher.publish(msg)

    rospy.spin()

