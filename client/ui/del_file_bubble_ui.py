# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'del_file_bubble.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_file_bubble(object):
    def setupUi(self, file_bubble):
        if not file_bubble.objectName():
            file_bubble.setObjectName(u"file_bubble")
        file_bubble.resize(818, 141)
        self.horizontalLayout = QHBoxLayout(file_bubble)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.widgetMain = QWidget(file_bubble)
        self.widgetMain.setObjectName(u"widgetMain")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.widgetMain.sizePolicy().hasHeightForWidth())
        self.widgetMain.setSizePolicy(sizePolicy)
        self.widgetMain.setMinimumSize(QSize(800, 0))
        self.widgetMain.setMaximumSize(QSize(800, 114514))
        self.widgetMain.setStyleSheet(u"QWidget#widgetMain{\n"
"	border-radius: 10px;\n"
"	border-bottom: 2px solid #F2F2F2;\n"
"}\n"
"\n"
"")
        self.avatar = QWidget(self.widgetMain)
        self.avatar.setObjectName(u"avatar")
        self.avatar.setGeometry(QRect(10, 20, 50, 50))
        self.avatar.setMinimumSize(QSize(50, 50))
        self.avatar.setMaximumSize(QSize(50, 50))
        self.avatar.setStyleSheet(u"QWidget#avatar{\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"	border: 2px solid #8A4FFF;\n"
"}")
        self.cur_time = QLabel(self.widgetMain)
        self.cur_time.setObjectName(u"cur_time")
        self.cur_time.setGeometry(QRect(70, 20, 141, 21))
        self.cur_time.setStyleSheet(u"QLabel#cur_time{\n"
"	background-color: transparent;\n"
"	font: 75 11pt \"Arial\";\n"
"	color: #888888;\n"
"}")
        self.message_bubble = QLabel(self.widgetMain)
        self.message_bubble.setObjectName(u"message_bubble")
        self.message_bubble.setGeometry(QRect(70, 60, 141, 41))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.message_bubble.sizePolicy().hasHeightForWidth())
        self.message_bubble.setSizePolicy(sizePolicy1)
        self.message_bubble.setMinimumSize(QSize(0, 0))
        self.message_bubble.setMaximumSize(QSize(16777215, 16777215))
        self.message_bubble.setCursor(QCursor(Qt.PointingHandCursor))
        self.message_bubble.setStyleSheet(u"QLabel#message_bubble {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #B482FF, stop:1 #8A4FFF); /* \u4fee\u6539\u4e3a\u7d2b\u8272\u7cfb\u6e10\u53d8 */\n"
"    border-radius: 15px;\n"
"    border-top-left-radius: 0px;\n"
"    padding: 10px;\n"
"\n"
"    /* \u6dfb\u52a0\u8f7b\u5fae\u7684\u5185\u53d1\u5149\u6548\u679c */\n"
"    border: 3px solid rgba(255, 255, 255, 0.4);\n"
"    border-bottom: none;\n"
"    border-right: none;\n"
"    border-left: none;\n"
"\n"
"    /* \u6dfb\u52a0\u8fb9\u6846\u6548\u679c */\n"
"    border: 2px solid #8A4FFF; /* \u4fee\u6539\u4e3a\u7d2b\u8272\u7cfb\u8fb9\u6846\u989c\u8272 */\n"
"	color:white;\u4ece\n"
"}\n"
"\n"
"QLabel#message_bubble[selected=\"true\"] {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1DA1F2, stop:1 #127FBF);\n"
"    color: white;\n"
"}\n"
"")
        self.who = QLabel(self.widgetMain)
        self.who.setObjectName(u"who")
        self.who.setGeometry(QRect(220, 20, 67, 17))

        self.horizontalLayout.addWidget(self.widgetMain)


        self.retranslateUi(file_bubble)

        QMetaObject.connectSlotsByName(file_bubble)
    # setupUi

    def retranslateUi(self, file_bubble):
        file_bubble.setWindowTitle(QCoreApplication.translate("file_bubble", u"Form", None))
        self.cur_time.setText(QCoreApplication.translate("file_bubble", u"01/01/2015 09:00:00", None))
        self.message_bubble.setText(QCoreApplication.translate("file_bubble", u"qss css html", None))
        self.who.setText(QCoreApplication.translate("file_bubble", u"name", None))
    # retranslateUi

