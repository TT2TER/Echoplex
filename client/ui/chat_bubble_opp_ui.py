# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chat_bubble_opp.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_chat_bubble(object):
    def setupUi(self, chat_bubble):
        if not chat_bubble.objectName():
            chat_bubble.setObjectName(u"chat_bubble")
        chat_bubble.resize(478, 422)
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(chat_bubble.sizePolicy().hasHeightForWidth())
        chat_bubble.setSizePolicy(sizePolicy)
        chat_bubble.setMinimumSize(QSize(0, 0))
        self.widgetMain = QWidget(chat_bubble)
        self.widgetMain.setObjectName(u"widgetMain")
        self.widgetMain.setGeometry(QRect(0, 0, 1000, 114514))
        self.widgetMain.setMinimumSize(QSize(1000, 114514))
        self.widgetMain.setMaximumSize(QSize(114514, 114514))
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
"	border: 2px solid rgb(115, 210, 22);\n"
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
        sizePolicy.setHeightForWidth(self.message_bubble.sizePolicy().hasHeightForWidth())
        self.message_bubble.setSizePolicy(sizePolicy)
        self.message_bubble.setMinimumSize(QSize(0, 0))
        self.message_bubble.setMaximumSize(QSize(16777215, 16777215))
        self.message_bubble.setCursor(QCursor(Qt.PointingHandCursor))
        self.message_bubble.setStyleSheet(u"QLabel#message_bubble {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #DCF8C6, stop:1 #B9E87E);\n"
"    border-radius: 15px;\n"
"    border-top-left-radius: 0px;\n"
"    padding: 10px;\n"
"    \n"
"    \n"
"    /* \u6dfb\u52a0\u8f7b\u5fae\u7684\u5185\u53d1\u5149\u6548\u679c */\n"
"    border: 3px solid rgba(255, 255, 255, 0.4);\n"
"    border-bottom: none;\n"
"    border-right: none;\n"
"    border-left: none;\n"
"    \n"
"    /* \u6dfb\u52a0\u8fb9\u6846\u6548\u679c */\n"
"    border: 2px solid #B9E87E;\n"
"}\n"
"\n"
"QLabel#message_bubble[selected=\"true\"] {\n"
"    background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #1DA1F2, stop:1 #127FBF);\n"
"    color: white;\n"
"}\n"
"")

        self.retranslateUi(chat_bubble)

        QMetaObject.connectSlotsByName(chat_bubble)
    # setupUi

    def retranslateUi(self, chat_bubble):
        chat_bubble.setWindowTitle(QCoreApplication.translate("chat_bubble", u"Form", None))
        self.cur_time.setText(QCoreApplication.translate("chat_bubble", u"01/01/2015 09:00:00", None))
        self.message_bubble.setText(QCoreApplication.translate("chat_bubble", u"qss css html", None))
    # retranslateUi

