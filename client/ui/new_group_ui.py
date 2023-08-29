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


class Ui_new_group(object):
    def setupUi(self, new_group):
        if not new_group.objectName():
            new_group.setObjectName(u"new_group")
        new_group.resize(142, 300)
        self.creat_group_butt = QPushButton(new_group)
        self.creat_group_butt.setObjectName(u"creat_group_butt")
        self.creat_group_butt.setGeometry(QRect(20, 240, 89, 25))
        self.group_member_list = QTextEdit(new_group)
        self.group_member_list.setObjectName(u"group_member_list")
        self.group_member_list.setGeometry(QRect(10, 160, 104, 70))
        self.new_group_name = QLineEdit(new_group)
        self.new_group_name.setObjectName(u"new_group_name")
        self.new_group_name.setGeometry(QRect(10, 60, 113, 25))
        self.label = QLabel(new_group)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 30, 67, 17))
        self.label_2 = QLabel(new_group)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 90, 111, 61))

        self.retranslateUi(new_group)

        QMetaObject.connectSlotsByName(new_group)
    # setupUi

    def retranslateUi(self, new_group):
        new_group.setWindowTitle(QCoreApplication.translate("new_group", u"Form", None))
        self.creat_group_butt.setText(QCoreApplication.translate("new_group", u"\u521b\u5efa\u7fa4\u804a", None))
        self.label.setText(QCoreApplication.translate("new_group", u"\u7fa4\u540d:", None))
        self.label_2.setText(QCoreApplication.translate("new_group", u"<html><head/><body><p>\u7fa4\u6210\u5458(\u8bf7\u7528</p><p>\u5206\u53f7\u9694\u5f00)</p></body></html>", None))
    # retranslateUi

