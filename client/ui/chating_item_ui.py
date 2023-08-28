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
        self.widgetMain.setStyleSheet(u"QWidget#widgetMain {\n"
"        background-color: rgba(70, 236, 206, 87);\n"
"        border-radius: 10px;\n"
"    	border-bottom: 0;\n"
"    	padding: 7px;\n"
"   	 margin: 7px;\n"
"    }")
        self.avatar = QWidget(self.widgetMain)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setGeometry(QRect(10, 10, 48, 48))
        self.avatar.setMinimumSize(QSize(48, 48))
        self.avatar.setMaximumSize(QSize(48, 48))
        self.avatar.setStyleSheet(u"QWidget#avatar{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 6px;\n"
"}")
        self.new_message = QWidget(self.widgetMain)
        self.new_message.setObjectName(u"new_message")
        self.new_message.setGeometry(QRect(44, 5, 21, 21))
        self.new_message.setMinimumSize(QSize(21, 21))
        self.new_message.setMaximumSize(QSize(21, 21))
        self.new_message.setStyleSheet(u"QWidget#new_message{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.new_message)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.massage_num = QLabel(self.new_message)
        self.massage_num.setObjectName(u"massage_num")
        self.massage_num.setStyleSheet(u"QLabel#massage_num{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	font: 10pt \"Airal\";\n"
"}")
        self.massage_num.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.massage_num)

        self.name = QLabel(self.widgetMain)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(80, 10, 121, 21))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy)
        self.name.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font: 75 14pt \"Arial\";\n"
"	color: blue\n"
"}")
        self.resent_message = QLabel(self.widgetMain)
        self.resent_message.setObjectName(u"resent_message")
        self.resent_message.setGeometry(QRect(80, 40, 221, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.resent_message.sizePolicy().hasHeightForWidth())
        self.resent_message.setSizePolicy(sizePolicy1)
        self.resent_message.setStyleSheet(u"QLabel#resent_message{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: rgb(32, 74, 135);\n"
"}")
        self.message_time = QLabel(self.widgetMain)
        self.message_time.setObjectName(u"message_time")
        self.message_time.setGeometry(QRect(205, 10, 141, 21))
        self.message_time.setStyleSheet(u"QLabel#message_time{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: #888888;\n"
"}")
        self.close_butt = QPushButton(self.widgetMain)
        self.close_butt.setObjectName(u"close_butt")
        self.close_butt.setGeometry(QRect(320, 30, 20, 20))
        self.close_butt.setStyleSheet(u"QPushButton#close_butt{\n"
"	border-radius: 10px;\n"
"	background-color: red;\n"
"	color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.widgetMain)


        self.retranslateUi(chating_item)

        QMetaObject.connectSlotsByName(chating_item)
    # setupUi

    def retranslateUi(self, chating_item):
        chating_item.setWindowTitle(QCoreApplication.translate("chating_item", u"Form", None))
        self.massage_num.setText(QCoreApplication.translate("chating_item", u"99", None))
        self.name.setText(QCoreApplication.translate("chating_item", u"Karson", None))
        self.resent_message.setText(QCoreApplication.translate("chating_item", u"How do you do?", None))
        self.message_time.setText(QCoreApplication.translate("chating_item", u"01/01/2015 09:00:00", None))
        self.close_butt.setText(QCoreApplication.translate("chating_item", u"x", None))
    # retranslateUi

