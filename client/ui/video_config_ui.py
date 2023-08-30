# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'video_config.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_video_config(object):
    def setupUi(self, video_config):
        if not video_config.objectName():
            video_config.setObjectName(u"video_config")
        video_config.resize(400, 300)
        self.yes = QPushButton(video_config)
        self.yes.setObjectName(u"yes")
        self.yes.setGeometry(QRect(100, 160, 89, 25))
        self.no = QPushButton(video_config)
        self.no.setObjectName(u"no")
        self.no.setGeometry(QRect(230, 160, 89, 25))
        self.info = QLabel(video_config)
        self.info.setObjectName(u"info")
        self.info.setGeometry(QRect(60, 40, 321, 121))

        self.retranslateUi(video_config)

        QMetaObject.connectSlotsByName(video_config)
    # setupUi

    def retranslateUi(self, video_config):
        video_config.setWindowTitle(QCoreApplication.translate("video_config", u"Form", None))
        self.yes.setText(QCoreApplication.translate("video_config", u"\u540c\u610f", None))
        self.no.setText(QCoreApplication.translate("video_config", u"\u4e0d\u540c\u610f", None))
        self.info.setText(QCoreApplication.translate("video_config", u"\u6d4b\u8bd5\u6587\u672c", None))
    # retranslateUi

