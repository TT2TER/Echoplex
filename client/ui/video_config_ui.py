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

from qfluentwidgets import PushButton


class Ui_video_config(object):
    def setupUi(self, video_config):
        if not video_config.objectName():
            video_config.setObjectName(u"video_config")
        video_config.resize(274, 300)
        self.verticalLayout = QVBoxLayout(video_config)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.info = QLabel(video_config)
        self.info.setObjectName(u"info")

        self.verticalLayout.addWidget(self.info)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.yes = PushButton(video_config)
        self.yes.setObjectName(u"yes")
        self.yes.setMinimumSize(QSize(30, 30))
        self.yes.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: green;\n"
"	color: white;\n"
"	font: 75 16pt \"Arial\";\n"
"}")

        self.horizontalLayout.addWidget(self.yes)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.no = PushButton(video_config)
        self.no.setObjectName(u"no")
        self.no.setMinimumSize(QSize(30, 30))
        self.no.setStyleSheet(u"QPushButton{\n"
"	border-radius: 15px;\n"
"	background-color: red;\n"
"	color: white;\n"
"}")

        self.horizontalLayout.addWidget(self.no)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_3)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.retranslateUi(video_config)

        QMetaObject.connectSlotsByName(video_config)
    # setupUi

    def retranslateUi(self, video_config):
        video_config.setWindowTitle(QCoreApplication.translate("video_config", u"Form", None))
        self.info.setText(QCoreApplication.translate("video_config", u"\u6d4b\u8bd5\u6587\u672c", None))
        self.yes.setText(QCoreApplication.translate("video_config", u"\u221a", None))
        self.no.setText(QCoreApplication.translate("video_config", u"\u2716", None))
    # retranslateUi

