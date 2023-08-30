# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_group.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import LineEdit
from qfluentwidgets import TextEdit


class Ui_new_group(object):
    def setupUi(self, new_group):
        if not new_group.objectName():
            new_group.setObjectName(u"new_group")
        new_group.resize(270, 273)
        self.verticalLayout = QVBoxLayout(new_group)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.mini_butt = QPushButton(new_group)
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

        self.close_butt = QPushButton(new_group)
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

        self.label = QLabel(new_group)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.new_group_name = LineEdit(new_group)
        self.new_group_name.setObjectName(u"new_group_name")

        self.verticalLayout.addWidget(self.new_group_name)

        self.label_2 = QLabel(new_group)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.group_member_list = TextEdit(new_group)
        self.group_member_list.setObjectName(u"group_member_list")

        self.verticalLayout.addWidget(self.group_member_list)

        self.creat_group_butt = PushButton(new_group)
        self.creat_group_butt.setObjectName(u"creat_group_butt")

        self.verticalLayout.addWidget(self.creat_group_butt)


        self.retranslateUi(new_group)

        QMetaObject.connectSlotsByName(new_group)
    # setupUi

    def retranslateUi(self, new_group):
        new_group.setWindowTitle(QCoreApplication.translate("new_group", u"Form", None))
        self.mini_butt.setText(QCoreApplication.translate("new_group", u"\u2796", None))
        self.close_butt.setText(QCoreApplication.translate("new_group", u"\u2716", None))
        self.label.setText(QCoreApplication.translate("new_group", u"\u7fa4\u540d:", None))
        self.label_2.setText(QCoreApplication.translate("new_group", u"<html><head/><body><p>\u7fa4\u6210\u5458(\u8bf7\u7528\u5206\u53f7\u9694\u5f00)</p></body></html>", None))
        self.creat_group_butt.setText(QCoreApplication.translate("new_group", u"\u521b\u5efa\u7fa4\u804a", None))
    # retranslateUi

