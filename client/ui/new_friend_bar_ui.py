# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_friend_bar.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_new_friend_bar(object):
    def setupUi(self, new_friend_bar):
        if not new_friend_bar.objectName():
            new_friend_bar.setObjectName(u"new_friend_bar")
        new_friend_bar.resize(360, 70)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(new_friend_bar.sizePolicy().hasHeightForWidth())
        new_friend_bar.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(new_friend_bar)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetMain = QWidget(new_friend_bar)
        self.widgetMain.setObjectName(u"widgetMain")
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMinimumSize(QSize(360, 70))
        self.widgetMain.setMaximumSize(QSize(360, 70))
        self.widgetMain.setStyleSheet(u"QWidget#widgetMain {\n"
"    background-color: rgb(233, 185, 110);\n"
"    border-radius: 10px;\n"
"    border-bottom: 0;\n"
"    padding: 7px;\n"
"    margin: 7px;\n"
"}\n"
"")
        self.name = QLabel(self.widgetMain)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 10, 121, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font: 75 14pt \"Arial\";\n"
"	color: blue\n"
"}")
        self.new_text = QLabel(self.widgetMain)
        self.new_text.setObjectName(u"new_text")
        self.new_text.setGeometry(QRect(20, 30, 221, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.new_text.sizePolicy().hasHeightForWidth())
        self.new_text.setSizePolicy(sizePolicy2)
        self.new_text.setStyleSheet(u"QLabel#new_text{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: rgb(32, 74, 135);\n"
"}")
        self.close_butt = QPushButton(self.widgetMain)
        self.close_butt.setObjectName(u"close_butt")
        self.close_butt.setGeometry(QRect(320, 30, 20, 20))
        self.close_butt.setStyleSheet(u"QPushButton#close_butt{\n"
"	border-radius: 10px;\n"
"	background-color: red;\n"
"	color: white;\n"
"}")
        self.config_butt = QPushButton(self.widgetMain)
        self.config_butt.setObjectName(u"config_butt")
        self.config_butt.setGeometry(QRect(290, 30, 20, 20))
        self.config_butt.setStyleSheet(u"QPushButton#config_butt{\n"
"	border-radius: 10px;\n"
"	background-color: green;\n"
"	color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.widgetMain)


        self.retranslateUi(new_friend_bar)

        QMetaObject.connectSlotsByName(new_friend_bar)
    # setupUi

    def retranslateUi(self, new_friend_bar):
        new_friend_bar.setWindowTitle(QCoreApplication.translate("new_friend_bar", u"Form", None))
        self.name.setText(QCoreApplication.translate("new_friend_bar", u"Karson", None))
        self.new_text.setText(QCoreApplication.translate("new_friend_bar", u"\u60a8\u6536\u5230\u4e00\u6761\u65b0\u597d\u53cb\u7533\u8bf7", None))
        self.close_butt.setText(QCoreApplication.translate("new_friend_bar", u"x", None))
        self.config_butt.setText(QCoreApplication.translate("new_friend_bar", u"\u221a", None))
    # retranslateUi

