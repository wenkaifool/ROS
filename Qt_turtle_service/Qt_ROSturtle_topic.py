#!/usr/bin/env python
# coding: utf-8

import rospy
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from geometry_msgs.msg import Twist
from math import radians, degrees
from turtlesim.msg import Pose
import sys

class MainWindow1(QWidget):
    def __init__(self):
        super(MainWindow1, self).__init__()

        # 自定义刷新
        updateTimer = QTimer(self)
        updateTimer.setInterval(16)
        updateTimer.start()

        updateTimer.timeout.connect(self.onUpdate)

        self.setWindowTitle('Turtle Control')
        self.resize(400, 120)

        layout = QFormLayout()
        self.setLayout(layout)

        self.editLinear = QLineEdit('0')
        layout.addRow("线速度", self.editLinear)

        self.editAngular = QLineEdit("0")
        layout.addRow("角速度", self.editAngular)

        self.labelX = QLabel()
        layout.addRow("当前X坐标", self.labelX)

        self.labelY = QLabel()
        layout.addRow("当前Y坐标", self.labelY)

        self.labelLinear = QLabel()
        layout.addRow("当前线速度", self.labelLinear)

        self.labelAngular = QLabel()
        layout.addRow("当前角速度", self.labelAngular)

        self.labelDegrees = QLabel()
        layout.addRow("当前角度", self.labelDegrees)

        self.btnSend = QPushButton("发送")
        layout.addRow(self.btnSend)

        self.btnSend.clicked.connect(self.clickSend)

        topicName = "/turtle1/cmd_vel"
        self.publisher = rospy.Publisher(topicName, Twist, queue_size=1000)

        poseTopicName = "/turtle1/pose"
        rospy.Subscriber(poseTopicName, Pose, self.poseCallback)

    def clickSend(self):
        linearX = float(self.editLinear.text())
        angularZ = radians(float(self.editAngular.text()))

        # 构建消息
        twist = Twist()
        twist.linear.x = linearX
        twist.angular.z = angularZ
        # 发布
        self.publisher.publish(twist)

    def poseCallback(self, msg):
        if not isinstance(msg, Pose):
            return
        self.labelX.setText(str(msg.x))
        self.labelY.setText(str(msg.y))
        self.labelLinear.setText(str(msg.linear_velocity))
        self.labelAngular.setText(str(msg.angular_velocity))
        self.labelDegrees.setText(str(degrees(msg.theta)))

    def onUpdate(self):
        self.update()
        if rospy.is_shutdown():
            self.close()


if __name__ == '__main__':
    nodeName = "turtle_ctrl"
    rospy.init_node(nodeName)

    app = QApplication(sys.argv)

    mywin = MainWindow1()
    mywin.show()

    sys.exit(app.exec_())
