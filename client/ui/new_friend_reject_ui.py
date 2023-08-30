# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_friend_reject.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(360, 70)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Form.sizePolicy().hasHeightForWidth())
        Form.setSizePolicy(sizePolicy)
        self.horizontalLayout = QHBoxLayout(Form)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetMain = QWidget(Form)
        self.widgetMain.setObjectName(u"widgetMain")
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMinimumSize(QSize(360, 70))
        self.widgetMain.setMaximumSize(QSize(360, 70))
        self.widgetMain.setStyleSheet(u"QWidget#widgetMain {\n"
"    background-color: rgb(239, 41, 41);\n"
"    border-radius: 10px;\n"
"    border-bottom: 0;\n"
"    padding: 7px;\n"
"    margin: 7px;\n"
"    box-shadow: 0px 5px 0px #F2F2F2; /* \u6dfb\u52a0\u5e95\u90e8\u8fb9\u6846\u6548\u679c */\n"
"}\n"
"")
        self.name = QLabel(self.widgetMain)
        self.name.setObjectName(u"name")
        self.name.setGeometry(QRect(20, 13, 121, 21))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.name.sizePolicy().hasHeightForWidth())
        self.name.setSizePolicy(sizePolicy1)
        self.name.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: blue\n"
"}")
        self.new_text = QLabel(self.widgetMain)
        self.new_text.setObjectName(u"new_text")
        self.new_text.setGeometry(QRect(20, 35, 221, 21))
        sizePolicy2 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.new_text.sizePolicy().hasHeightForWidth())
        self.new_text.setSizePolicy(sizePolicy2)
        self.new_text.setStyleSheet(u"QLabel#new_text{\n"
"	background-color: transparent;\n"
"	font: 75 9pt \"Arial\";\n"
"	color: rgb(238, 238, 236);\n"
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


        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.name.setText(QCoreApplication.translate("Form", u"Karson", None))
        self.new_text.setText(QCoreApplication.translate("Form", u"\u62d2\u7edd\u4e86\u4f60\u7684\u597d\u53cb\u8bf7\u6c42", None))
        self.config_butt.setText(QCoreApplication.translate("Form", u"\u221a", None))
    # retranslateUi

