#!/usr/bin/env python
# coding:utf-8

import rospy
import serial
import struct
from std_msgs.msg import Int32, Float32
from std_srvs.srv import SetBool,SetBoolRequest, SetBoolResponse

buzzer_state = False

def subs_callback(msg):
    if not isinstance(msg, Int32):
        return

    pwm = msg.data
    packed_data = struct.pack('h',pwm)
    byte_data = bytearray([0x03, packed_data[0], packed_data[1]])
    ser.write(byte_data)


def do_encoder(read):
    data = bytearray([])
    data.append(read[1])
    data.append(read[2])

    data = struct.unpack('h', data)[0]
    rpm = data/100.0

    msg = Float32()
    msg.data = rpm

    rpm_publisher.publish(msg)


def led_callback(request):
    if not isinstance(request, SetBoolRequest):
        return

    led_state = request.data
    b = 0x01 if led_state else 0x02
    data = bytearray([0x01, b])
    ser.write(data)

    response = SetBoolResponse()

    # setstate = SetBool()
    response.success = led_state

    return response


def buzzer_callback(request):
    if not isinstance(request, SetBoolRequest):
        return

    buzzer_request_state = request.data
    b = 0x01 if buzzer_request_state else 0x02
    data = bytearray([0x02, b])
    ser.write(data)

    # Wait for the updated state after writing to the core.
    rospy.sleep(0.1)

    response = SetBoolResponse()

    # setstate = SetBool()
    response.success = buzzer_state == buzzer_request_state

    return response


if __name__ == '__main__':
    node_name = 'service_driver_node'
    rospy.init_node(node_name)

    count = 0
    while count < 10:
        count += 1
        try:
            ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
            break
        except Exception as e:
            print (e)

    ##########################################topic#############################################################
    motor_topic_name = '/motor'
    subscriber = rospy.Subscriber(motor_topic_name, Int32, subs_callback)

    encode_topic_name = '/rpm'
    rpm_publisher = rospy.Publisher(encode_topic_name, Float32, queue_size=1000)

    ###########################################service###########################################################
    # LED
    led_service_name = '/led'
    rospy.Service(led_service_name, SetBool, led_callback)
    # Buzzer
    buzz_service_name = '/buzzer'
    rospy.Service(buzz_service_name, SetBool, buzzer_callback)

    while not rospy.is_shutdown():
        read = ser.read(3)
        read = bytearray(read)

        if read[0] == 0x03:
            do_encoder(read)
        elif read[0] == 0x01:
            pass
        elif read[0] == 0x02:
            buzzer_state = read[1] == 0x01
        for i in read:
            print (hex(i)),
            print (' '),
        print ('')

    rospy.spin()