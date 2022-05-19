#!/usr/bin/env python
#coding:utf-8
"""
PyQt中有非常多的功能模块,开发中最常用的功能模块主要有三个:
QtCore:包含了核心的非GUI的功能: 主要和时间、文件与文件夹、各种数据、流、URLs、mime类文件、进程与线程一起使用
QtGui:包含了窗口系统、事件处理、2D图像、基本绘画、字体和文字类
QtWidgets:包含了一些列创建桌面应用的UI元素
"""
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys


class QtWindow(object):
    def __init__(self, maxentrylen=10, title='黑马ROS无人小车'):
        self.win_title = title
        self.maxentrylen = maxentrylen

        self.single_line = True
        self.layout_style = ['vertical', 'honrizental', 'form', 'grid']
        self.instruments = []
        self.echomode = [QLineEdit.Normal, QLineEdit.NoEcho, QLineEdit.Password, QLineEdit.PasswordEchoOnEdit]

        self.create_window()

    def create_window(self):
        # 1.创建应用程序
        self.app = QApplication(sys.argv)
        # 2.创建窗口
        self.window = QWidget()
        # 设置窗口标题
        self.window.setWindowTitle(self.win_title)
        icon = QIcon('vehicle.jpeg')
        # 设置图标
        self.window.setWindowIcon(icon)

    def add_text(self):
        self.label_txt = QLabel()
        self.label_txt.setText('第一个文本')
        self.label_txt_font = QFont()
        self.label_txt_font.setPixelSize(40)
        self.label_txt.setFont(self.label_txt_font)
        # 将文本控件添加到窗口中
        self.label_txt.setParent(self.window)

        self.instruments.append(self.label_txt)

    def add_image(self):
        self.label_img = QLabel()
        pixmap = QPixmap('vehicle.jpeg')
        self.label_img.setPixmap(pixmap)
        self.label_img.setParent(self.window)

        self.window.resize(pixmap.width(), pixmap.height())  # 改变窗口大小
        self.instruments.append(self.label_img)

    def add_entry(self):
        if self.single_line:
            self.edit_entry = QLineEdit()  # 单行输入框
            self.edit_entry.setMaxLength(self.maxentrylen)  # 设置输入框最大字符数

            self.edit_entry.setEchoMode(self.echomode[0])  # etup display mode of entried texts

            self.edit_entry.setPlaceholderText('请输入用户名')  # 设置输入框提示

            self.edit_entry.setText('张三')  # 设置文本

            self.get_entry_text = self.edit_entry.text() # 获取单选框的文字

        else:
            self.edit_entry = QTextEdit()  # 多行文本输入框
            self.edit_entry.setPlainText("hello itcast\nhello itheima\n")  # 设置多行文本框的文本内容
            self.edit_entry.setHtml("<h1>hello python</h1>")  # 设置多行文本框的内容为HTML文档

        self.edit_entry.setParent(self.window)  # 显示输入框
        self.instruments.append(self.edit_entry)

    def add_button(self):
        self.btn = QPushButton()
        # 添加按钮提示
        self.btn.setText('登录')
        # 提示气泡
        self.btn.setToolTip('登录按钮')
        # 展示按钮
        self.btn.setParent(self.window)

        self.btn.clicked.connect(self.btn_clicked_inputdialog)

        self.instruments.append(self.btn)

    def add_radiobtn(self):
        # 创建两个单选框
        self.rb1 = QRadioButton('男')
        self.rb2 = QRadioButton('女')
        self.rb1.setChecked(True)

        # 绑定信号和槽
        self.rb1.toggled.connect(self.toggled)
        self.instruments.append(self.rb1)
        self.instruments.append(self.rb2)

        self.ck1 = QCheckBox('抽烟')
        self.ck2 = QCheckBox('喝酒')
        self.ck3 = QCheckBox('烫头')
        self.instruments.append(self.ck1)
        self.instruments.append(self.ck2)
        self.instruments.append(self.ck3)
        # 绑定信号和槽
        self.ck1.stateChanged.connect(self.stateChanged1)
        self.ck2.stateChanged.connect(self.stateChanged2)
        self.ck3.stateChanged.connect(self.stateChanged3)

    def design_layout(self):
        instruments_title = ['image', 'text', 'entry', 'btn', 'radiobtn1', 'radiobtn2', 'ck1','ck2','ck3']
        if len(self.layout_style) == 2:
            self.layout = QHBoxLayout()
            for name in self.instruments:
                self.layout.addWidget(name)
        elif len(self.layout_style) == 1:
            self.layout = QVBoxLayout()
            for name in self.instruments:
                self.layout.addWidget(name)
        elif len(self.layout_style) == 4:
            self.layout = QFormLayout()
            for index, name in enumerate(self.instruments):
                self.layout.addRow(instruments_title[index], name)
        elif len(self.layout_style) == 3:
            self.layout = QGridLayout()
            for i in range(4):
                for j in range(4):
                    btn = QPushButton("按钮 {} {}".format(i, j))

                    self.layout.addWidget(btn, i, j)
        # 添加布局到窗口中
        self.window.setLayout(self.layout)

    def btn_clicked(self):
        print('Hello, MF')

    def btn_clicked_msgbox(self):
        # QMessageBox 对话框
        # information： 信息对话框 parent, title, content 阻塞式
        QMessageBox.information(self.window, '我是对话框的title', '我是对话框的内容')

        # question: 问答对话框
        result = QMessageBox.question(self.window, 'title', 'content')
        print(type(result))
        if result == QMessageBox.Yes:
            print('yes')
        else:
            print('no')

        # warining
        # QMessageBox.warning(self.window, 'title', 'content')

        # critical
        # QMessageBox.critical(self.window, 'title', 'content')

        # about
        QMessageBox.about(self.window, 'title', 'content')

        print('对话框消失了')

    def btn_clicked_inputdialog(self):
        str, success = QInputDialog.getText(self.window, '提示', '请输入角色名称')
        if success:
            self.edit_entry.setText(str)

    def toggled(self, checked):
        print('hello, {}'.format(checked))

    def stateChanged1(self, state):
        if state == 2:
            print('CK1选中')
        elif state == 0:
            print('取消选中')

    def stateChanged2(self, state):
        if state == 2:
            print('选中')
        elif state == 0:
            print('取消选中')

    def stateChanged3(self, state):
        if state == 2:
            print('选中')
        elif state == 0:
            print('取消选中')

    def app_setup(self):
        self.window.show()  # 3.显示窗口
        self.app.exec_()  # 4.程序启动执行


if __name__ == '__main__':
    test1 = QtWindow()
    test1.add_image()
    test1.add_text()
    test1.add_entry()
    test1.add_button()
    test1.add_radiobtn()

    test1.design_layout()
    test1.app_setup()
    sys.exit()
