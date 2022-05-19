#!/usr/bin/env python
#coding:utf-8

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

import serial
import struct, threading


class MyWindow(QWidget):

    def __init__(self):
        super(MyWindow, self).__init__()

        self.__init_ui()

        count = 0
        while count < 10:
            count += 1
            try:
                self.ser = serial.Serial(port='/dev/ttyUSB0', baudrate=115200)
                # 如果出错了，后面的代码就不执行了
                # 能到达这个位置说明，链接成功
                break
            except Exception as e:
                print('count =', count, e)

        t = threading.Thread(target=self.receiev_data)
        t.start()

    def receiev_data(self):
        while True:

            readdata = self.ser.read(2)

            data = bytearray([])
            data.extend(readdata)
            data = struct.unpack('h', data)[0]
            rpm = data/100.0

            self.__lb_rpm.setText(str(rpm))

    def __init_ui(self):
        self.setWindowTitle('下位机控制')

        layout = QHBoxLayout()
        self.setLayout(layout)

        first_layout = QVBoxLayout()
        second_layout = QVBoxLayout()
        third_layout = QVBoxLayout()

        layout.addLayout(first_layout)
        layout.addLayout(second_layout)
        layout.addLayout(third_layout)

        self.__init_first(first_layout)
        self.__init_second(second_layout)
        self.__init_third(third_layout)

    def __init_first(self, layout):
        led_group = QGroupBox('LED控制')
        layout.addWidget(led_group)
        led_layout = QVBoxLayout(led_group)
        self.__init_led_layout(led_layout)

        buzzer_group = QGroupBox('蜂鸣器控制')
        layout.addWidget(buzzer_group)
        buzzer_layout = QVBoxLayout(buzzer_group)
        self.__init_buzzer_layout(buzzer_layout)

    def __init_led_layout(self, layout):
        btn_open = QPushButton('打开LED')
        btn_close = QPushButton('关闭LED')
        btn_toggle = QPushButton('开关LED')

        layout.addWidget(btn_open)
        layout.addWidget(btn_close)
        layout.addWidget(btn_toggle)

        btn_open.clicked.connect(self.led_open)
        btn_close.clicked.connect(self.led_close)
        btn_toggle.clicked.connect(self.led_toggle)

    def __init_buzzer_layout(self, layout):
        btn_open = QPushButton('打开蜂鸣器')
        btn_close = QPushButton('关闭蜂鸣器')
        btn_toggle = QPushButton('开关蜂鸣器')

        layout.addWidget(btn_open)
        layout.addWidget(btn_close)
        layout.addWidget(btn_toggle)

        btn_open.clicked.connect(self.buzzer_open)
        btn_close.clicked.connect(self.buzzer_close)
        btn_toggle.clicked.connect(self.buzzer_toggle)

    def __init_second(self, layout):
        motor_group = QGroupBox('电机控制')
        layout.addWidget(motor_group)
        motor_layout = QVBoxLayout(motor_group)
        self.__init_motor_layout(motor_layout)

        oled_group = QGroupBox('OLED控制')
        layout.addWidget(oled_group)
        oled_layout = QVBoxLayout(oled_group)
        self.__init_oled_layout(oled_layout)

    def __init_motor_layout(self, layout):
        self.__le_motor = QLineEdit()
        btn = QPushButton("发送")

        layout.addWidget(self.__le_motor)
        layout.addWidget(btn)

        btn.clicked.connect(self.motor_spin)

    def __init_oled_layout(self, layout):
        self.__le_oled = QLineEdit()
        btn = QPushButton("发送")

        layout.addWidget(self.__le_oled)
        layout.addWidget(btn)

        btn.clicked.connect(self.oled_show)

    def __init_third(self, layout):
        rpm_group = QGroupBox('转速显示')
        rpm_layout = QFormLayout(rpm_group)
        layout.addWidget(rpm_group)
        self.__init_rpm_ui(rpm_layout)

    def __init_rpm_ui(self, layout):
        self.__lb_rpm = QLabel()
        layout.addRow('转速(圈/秒)', self.__lb_rpm)

    def led_open(self):
        # 字节数据
        data = bytearray([0x01, 0x01])
        self.ser.write(data)

    def led_close(self):
        # 字节数据
        data = bytearray([0x01, 0x02])
        self.ser.write(data)

    def led_toggle(self):
        # 字节数据
        data = bytearray([0x01, 0x03])
        self.ser.write(data)

    def buzzer_open(self):
        # 字节数据
        data = bytearray([0x02, 0x01])
        self.ser.write(data)

    def buzzer_close(self):
        # 字节数据
        data = bytearray([0x02, 0x02])
        self.ser.write(data)

    def buzzer_toggle(self):
        # 字节数据
        data = bytearray([0x02, 0x03])
        self.ser.write(data)

    def motor_spin(self):
        text = self.__le_motor.text()
        pwm = int(text)
        pack = struct.pack('h', pwm)
        data = bytearray([0x03, pack[0], pack[1]])
        self.ser.write(data)

    def oled_show(self):
        text = self.__le_oled.text()
        data = bytearray([0x04])
        data.extend(text.encode())
        self.ser.write(data)


if __name__ == '__main__':
    app = QApplication(sys.argv)

    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
