#!/usr/bin/env python
# coding: utf-8
import rospy
from std_srvs.srv import Empty, EmptyRequest, EmptyResponse
from turtlesim.srv import Spawn, SpawnRequest, SpawnResponse, Kill, KillRequest, KillResponse, \
    SetPen, SetPenRequest, SetPenResponse
from math import radians, degrees

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

import sys

class MyWindow(QWidget):
    def __init__(self):
        super(MyWindow, self).__init__()

        self.setWindowTitle('ROS乌龟上位机')
        self.resize(600, 0)
        layout = QVBoxLayout()
        self.setLayout(layout)

        # l1
        # l1_layout = QFormLayout()
        l1_layout = QHBoxLayout()
        layout.addLayout(l1_layout)

        self.clear_btn = QPushButton('清理画布')
        l1_layout.addRow(self.clear_btn)
        self.clear_btn.clicked.connect(self.clear_track)

        self.reset_btn = QPushButton('重置')
        l1_layout.addRow(self.reset_btn)
        self.reset_btn.clicked.connect(self.reset_turtle)

        # l2
        l2_layout = QHBoxLayout()
        layout.addLayout(l2_layout)

        self.spawn_x = QLineEdit()
        l2_layout.addWidget(self.spawn_x)
        self.spawn_x.setPlaceholderText('x')
        self.spawn_y = QLineEdit()
        l2_layout.addWidget(self.spawn_y)
        self.spawn_y.setPlaceholderText('y')
        self.spawn_z = QLineEdit()
        l2_layout.addWidget(self.spawn_z)
        self.spawn_z.setPlaceholderText('angular')
        self.spawn_name = QLineEdit()
        l2_layout.addWidget(self.spawn_name)
        self.spawn_name.setPlaceholderText('name')

        self.spawn_btn = QPushButton('创建小乌龟')
        l2_layout.addWidget(self.spawn_btn)
        self.spawn_btn.clicked.connect(self.spawn_turtle)

        # l3
        l3_layout = QHBoxLayout()
        layout.addLayout(l3_layout)

        self.spawned_name = QLineEdit()
        l3_layout.addWidget(self.spawned_name)
        self.spawned_name.setPlaceholderText('name')

        self.kill_turtle_btn = QPushButton('杀死小乌龟')
        l3_layout.addWidget(self.kill_turtle_btn)

        self.kill_turtle_btn.clicked.connect(self.kill_turtle)

        # l4
        l4_layout = QHBoxLayout()
        layout.addLayout(l4_layout)

        self.penname = QLineEdit('turtle1')
        l4_layout.addWidget(self.penname)
        self.penname.setPlaceholderText('name')
        self.penred = QLineEdit('0')
        l4_layout.addWidget(self.penred)
        self.penred.setPlaceholderText('red')
        self.pengreen = QLineEdit('0')
        l4_layout.addWidget(self.pengreen)
        self.pengreen.setPlaceholderText('green')
        self.penblue = QLineEdit('0')
        l4_layout.addWidget(self.penblue)
        self.penblue.setPlaceholderText('blue')
        self.penwidth = QLineEdit('0')
        l4_layout.addWidget(self.penwidth)
        self.penwidth.setPlaceholderText('width')

        self.penwidth_radbtn = QRadioButton('关闭')
        l4_layout.addWidget(self.penwidth_radbtn)

        self.penswitch = QPushButton('设置画笔')
        l4_layout.addWidget(self.penswitch)
        self.penswitch.clicked.connect(self.pen_switch)

        # l5
        l5_layout = QHBoxLayout()
        layout.addLayout(l5_layout)

        self.abs_name = QLineEdit()
        l5_layout.addWidget(self.abs_name)
        self.abs_name.setPlaceholderText('name')
        self.set_x = QLineEdit()
        l5_layout.addWidget(self.set_x)
        self.set_x.setPlaceholderText('x')
        self.set_y = QLineEdit()
        l5_layout.addWidget(self.set_y)
        self.set_y.setPlaceholderText('y')
        self.set_angle = QLineEdit()
        l5_layout.addWidget(self.set_angle)
        self.set_angle.setPlaceholderText('angle')

        self.set_pos_btn = QPushButton('设置绝对位置')
        l5_layout.addWidget(self.set_pos_btn)
        self.set_pos_btn.clicked.connect(self.set_abs_pos)

        # l6
        l6_layout = QHBoxLayout()
        layout.addLayout(l6_layout)

        self.rel_name = QLineEdit()
        l6_layout.addWidget(self.rel_name)
        self.rel_name.setPlaceholderText('name')
        self.velocity = QLineEdit()
        l6_layout.addWidget(self.velocity)
        self.velocity.setPlaceholderText('velocity')
        self.ang_vel = QLineEdit()
        l6_layout.addWidget(self.ang_vel)
        self.ang_vel.setPlaceholderText('angular velocity')

        self.set_rel_btn = QPushButton('设置相对位置')
        l6_layout.addWidget(self.set_rel_btn)
        self.set_rel_btn.clicked.connect(self.set_rel_pos)

    # get access to the turtlesim Service: clear
    def clear_track(self):
        # since the service is created only when it is used, then creation of service will be performed
        # in the function, insead of i the init

        # 0. create the client
        # 0.1 get the service name via two steps
        #     (1) run the turtle node: rosrun turtlesim turtlesim_node
        #     (2) get the nodeinfo: rosnode info /turtlesim
        service_name = '/clear'

        # 0.2 get the service type:
        #     (1) rosservice info /clear
        #     (2) import the library
        client = rospy.ServiceProxy(service_name, Empty)

        # 1. get the service ---before doing this, create the client in the function at first
        client.wait_for_service()

        # 2. call the request
        # note that there is no response for this request
        request = EmptyRequest()
        client.call(request)

        # close the client
        client.close()

    def reset_turtle(self):
        service_name = '/reset'
        client = rospy.ServiceProxy(service_name, Empty)
        client.wait_for_service()
        request = EmptyRequest()
        client.call(request)
        client.close()

    def spawn_turtle(self):
        service_name = '/spawn'
        client = rospy.ServiceProxy(service_name, Spawn)
        client.wait_for_service()
        request = SpawnRequest()
        request.x = float(self.spawn_x.text())
        request.y = float(self.spawn_y.text())
        request.theta = radians(float(self.spawn_z.text()))
        request.name = self.spawn_name.text()
        client.call(request)
        client.close()

    def kill_turtle(self):
        service_name = '/kill'
        client = rospy.ServiceProxy(service_name, Kill)
        client.wait_for_service()
        request = KillRequest()
        request.name = self.spawned_name.text()
        client.call(request)
        client.close()

    def pen_switch(self):
        service_name = '/{}/set_pen'.format(self.penname.text())
        client = rospy.ServiceProxy(service_name, SetPen)
        client.wait_for_service()
        request = SetPenRequest()
        request.b = int(self.penblue.text())
        request.g = int(self.pengreen.text())
        request.r = int(self.penred.text())
        request.width = int(self.penwidth.text())

        off_btn = 1 if self.penwidth_radbtn.isChecked() else 0
        request.off = off_btn

        client.call(request)
        client.close()

    def set_abs_pos(self):
        pass

    def set_rel_pos(self):
        pass




if __name__ == '__main__':
    # ROS
    rospy.init_node('turtle_control_node')


    app = QApplication(sys.argv)

    mywin = MyWindow()
    mywin.show()

    sys.exit(app.exec_())
