# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chating_item.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_chating_item(object):
    def setupUi(self, chating_item):
        if not chating_item.objectName():
            chating_item.setObjectName(u"chating_item")
        chating_item.resize(360, 70)
        chating_item.setMinimumSize(QSize(360, 70))
        chating_item.setMaximumSize(QSize(360, 70))
        self.horizontalLayout = QHBoxLayout(chating_item)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetMain = QWidget(chating_item)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setMinimumSize(QSize(360, 70))
        self.widgetMain.setMaximumSize(QSize(360, 70))
        self.widgetMain.setStyleSheet(u"QWidget#widgetMain{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-bottom: 1px solid #F2F2F2;\n"
"}\n"
"\n"
"")
        self.avatar = QWidget(self.widgetMain)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setGeometry(QRect(10, 10, 48, 48))
        self.avatar.setMinimumSize(QSize(48, 48))
        self.avatar.setMaximumSize(QSize(48, 48))
        self.avatar.setStyleSheet(u"QWidget#widgetHead{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 4px;\n"
"	border-image: url(:/image/Head.png);\n"
"}")
        self.new_message = QWidget(self.widgetMain)
        self.new_message.setObjectName(u"new_message")
        self.new_message.setGeometry(QRect(50, 0, 21, 21))
        self.new_message.setMinimumSize(QSize(21, 21))
        self.new_message.setMaximumSize(QSize(21, 21))
        self.new_message.setStyleSheet(u"QWidget#widgetCount{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.new_message)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.massage_num = QLabel(self.new_message)
        self.massage_num.setObjectName(u"massage_num")
        self.massage_num.setStyleSheet(u"QLabel#labelCount{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	font: 10pt \"Airal\";\n"
"}")
        self.massage_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.massage_num)

        self.name = QLabel(self.widgetMain)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(80, 10, 121, 21))
        self.name.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font: 75 14pt \"Arial\";\n"
"	color: #000000\n"
"}")
        self.resent_message = QLabel(self.widgetMain)
        self.resent_message.setObjectName(u"resent_message")
        self.resent_message.setGeometry(QRect(80, 40, 181, 21))
        self.resent_message.setStyleSheet(u"QLabel#labelMsg{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: #888888;\n"
"}")
        self.cur_time = QLabel(self.widgetMain)
        self.cur_time.setObjectName(u"cur_time")
        self.cur_time.setGeometry(QRect(205, 10, 141, 21))
        self.cur_time.setStyleSheet(u"QLabel#labelTime{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: #888888;\n"
"}")
        self.close_butt = QPushButton(self.widgetMain)
        self.close_butt.setObjectName(u"close_butt")
        self.close_butt.setGeometry(QRect(320, 30, 20, 20))
        self.close_butt.setStyleSheet(u"QPushButton#btnClose{\n"
"	border-radius: 10px;\n"
"	background-color: red\n"
"}")

        self.horizontalLayout.addWidget(self.widgetMain)


        self.retranslateUi(chating_item)
        self.close_butt.clicked.connect(chating_item.on_btnDeleteClicked)

        QMetaObject.connectSlotsByName(chating_item)
    # setupUi

    def retranslateUi(self, chating_item):
        chating_item.setWindowTitle(QCoreApplication.translate("chating_item", u"Form", None))
        self.massage_num.setText(QCoreApplication.translate("chating_item", u"99", None))
        self.name.setText(QCoreApplication.translate("chating_item", u"Karson", None))
        self.resent_message.setText(QCoreApplication.translate("chating_item", u"How do you do?", None))
        self.cur_time.setText(QCoreApplication.translate("chating_item", u"01/01/2015 09:00:00", None))
        self.close_butt.setText(QCoreApplication.translate("chating_item", u"x", None))
    # retranslateUi

