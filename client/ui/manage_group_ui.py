# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'manage_group.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import TextEdit


class Ui_manage_group(object):
    def setupUi(self, manage_group):
        if not manage_group.objectName():
            manage_group.setObjectName(u"manage_group")
        manage_group.resize(187, 264)
        self.verticalLayout = QVBoxLayout(manage_group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.mini_butt = QPushButton(manage_group)
        self.mini_butt.setObjectName(u"mini_butt")
        self.mini_butt.setStyleSheet(u"QPushButton {\n"
"        background-color: green;\n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        width: 20px;\n"
"        height: 20px;\n"
"        font-size: 14px;\n"
"        color: white;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: rgba(0, 128, 0, 0.8);\n"
"    }\n"
"    \n"
"    QPushButton:pressed {\n"
"        background-color: rgba(0, 128, 0, 1);\n"
"    }")

        self.horizontalLayout_4.addWidget(self.mini_butt)

        self.close_butt = QPushButton(manage_group)
        self.close_butt.setObjectName(u"close_butt")
        self.close_butt.setStyleSheet(u"QPushButton {\n"
"        background-color: red;\n"
"        border: none;\n"
"        border-radius: 10px;\n"
"        width: 20px;\n"
"        height: 20px;\n"
"        font-size: 12px;\n"
"        color: white;\n"
"    }\n"
"    \n"
"    QPushButton:hover {\n"
"        background-color: rgba(255, 0, 0, 0.8);\n"
"    }\n"
"    \n"
"    QPushButton:pressed {\n"
"        background-color: rgba(255, 0, 0, 1);\n"
"    }")

        self.horizontalLayout_4.addWidget(self.close_butt)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.label_2 = QLabel(manage_group)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.group_member_list = TextEdit(manage_group)
        self.group_member_list.setObjectName(u"group_member_list")

        self.verticalLayout.addWidget(self.group_member_list)

        self.add_member_butt = PushButton(manage_group)
        self.add_member_butt.setObjectName(u"add_member_butt")

        self.verticalLayout.addWidget(self.add_member_butt)

        self.line = QFrame(manage_group)
        self.line.setObjectName(u"line")
        self.line.setFrameShape(QFrame.HLine)
        self.line.setFrameShadow(QFrame.Sunken)

        self.verticalLayout.addWidget(self.line)

        self.del_group_butt = PushButton(manage_group)
        self.del_group_butt.setObjectName(u"del_group_butt")

        self.verticalLayout.addWidget(self.del_group_butt)


        self.retranslateUi(manage_group)

        QMetaObject.connectSlotsByName(manage_group)
    # setupUi

    def retranslateUi(self, manage_group):
        manage_group.setWindowTitle(QCoreApplication.translate("manage_group", u"Form", None))
        self.mini_butt.setText(QCoreApplication.translate("manage_group", u"\u2796", None))
        self.close_butt.setText(QCoreApplication.translate("manage_group", u"\u2716", None))
        self.label_2.setText(QCoreApplication.translate("manage_group", u"<html><head/><body><p>\u65b0\u6dfb\u52a0\u6210\u5458</p></body></html>", None))
        self.add_member_butt.setText(QCoreApplication.translate("manage_group", u"\u6dfb\u52a0", None))
        self.del_group_butt.setText(QCoreApplication.translate("manage_group", u"\u5220\u9664\u7fa4\u804a", None))
    # retranslateUi

