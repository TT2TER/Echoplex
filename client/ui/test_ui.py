# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_MsgItem(object):
    def setupUi(self, MsgItem):
        if not MsgItem.objectName():
            MsgItem.setObjectName(u"MsgItem")
        MsgItem.resize(360, 70)
        MsgItem.setMinimumSize(QSize(360, 70))
        MsgItem.setMaximumSize(QSize(360, 70))
        self.horizontalLayout = QHBoxLayout(MsgItem)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.widgetMain = QWidget(MsgItem)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setMinimumSize(QSize(360, 70))
        self.widgetMain.setMaximumSize(QSize(360, 70))
        self.widgetMain.setStyleSheet(u"QWidget#widgetMain{\n"
"	background-color: rgb(255, 255, 255);\n"
"	border-bottom: 1px solid #F2F2F2;\n"
"}\n"
"\n"
"")
        self.widgetHead = QWidget(self.widgetMain)
        self.widgetHead.setObjectName(u"widgetHead")
        self.widgetHead.setGeometry(QRect(10, 10, 48, 48))
        self.widgetHead.setMinimumSize(QSize(48, 48))
        self.widgetHead.setMaximumSize(QSize(48, 48))
        self.widgetHead.setStyleSheet(u"QWidget#widgetHead{\n"
"	background-color: rgb(0, 0, 0);\n"
"	border-radius: 4px;\n"
"	border-image: url(:/image/Head.png);\n"
"}")
        self.widgetCount = QWidget(self.widgetMain)
        self.widgetCount.setObjectName(u"widgetCount")
        self.widgetCount.setGeometry(QRect(50, 0, 21, 21))
        self.widgetCount.setMinimumSize(QSize(21, 21))
        self.widgetCount.setMaximumSize(QSize(21, 21))
        self.widgetCount.setStyleSheet(u"QWidget#widgetCount{\n"
"	border-radius: 10px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.horizontalLayout_2 = QHBoxLayout(self.widgetCount)
        self.horizontalLayout_2.setSpacing(0)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbCount = QLabel(self.widgetCount)
        self.lbCount.setObjectName(u"lbCount")
        self.lbCount.setStyleSheet(u"QLabel#labelCount{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	font: 10pt \"Airal\";\n"
"}")
        self.lbCount.setAlignment(Qt.AlignCenter)

        self.horizontalLayout_2.addWidget(self.lbCount)

        self.lbName = QLabel(self.widgetMain)
        self.lbName.setObjectName(u"lbName")
        self.lbName.setGeometry(QRect(80, 10, 121, 21))
        self.lbName.setStyleSheet(u"QLabel{\n"
"	background-color: transparent;\n"
"	font: 75 14pt \"Arial\";\n"
"	color: #000000\n"
"}")
        self.lbMsg = QLabel(self.widgetMain)
        self.lbMsg.setObjectName(u"lbMsg")
        self.lbMsg.setGeometry(QRect(80, 40, 181, 21))
        self.lbMsg.setStyleSheet(u"QLabel#labelMsg{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: #888888;\n"
"}")
        self.lbTime = QLabel(self.widgetMain)
        self.lbTime.setObjectName(u"lbTime")
        self.lbTime.setGeometry(QRect(205, 10, 141, 21))
        self.lbTime.setStyleSheet(u"QLabel#labelTime{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: #888888;\n"
"}")
        self.btnClose = QPushButton(self.widgetMain)
        self.btnClose.setObjectName(u"btnClose")
        self.btnClose.setGeometry(QRect(320, 30, 20, 20))
        self.btnClose.setStyleSheet(u"QPushButton#btnClose{\n"
"	border-radius: 10px;\n"
"	background-color: red\n"
"}")

        self.horizontalLayout.addWidget(self.widgetMain)


        self.retranslateUi(MsgItem)
        #self.btnClose.clicked.connect(MsgItem.on_btnDeleteClicked)

        QMetaObject.connectSlotsByName(MsgItem)
    # setupUi

    def retranslateUi(self, MsgItem):
        MsgItem.setWindowTitle(QCoreApplication.translate("MsgItem", u"Form", None))
        self.lbCount.setText(QCoreApplication.translate("MsgItem", u"99", None))
        self.lbName.setText(QCoreApplication.translate("MsgItem", u"Karson", None))
        self.lbMsg.setText(QCoreApplication.translate("MsgItem", u"How do you do?", None))
        self.lbTime.setText(QCoreApplication.translate("MsgItem", u"01/01/2015 09:00:00", None))
        self.btnClose.setText(QCoreApplication.translate("MsgItem", u"x", None))
    # retranslateUi

