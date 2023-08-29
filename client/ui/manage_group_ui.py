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


class Ui_manage_group(object):
    def setupUi(self, manage_group):
        if not manage_group.objectName():
            manage_group.setObjectName(u"manage_group")
        manage_group.resize(400, 300)
        self.label_2 = QLabel(manage_group)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(30, 20, 111, 61))
        self.group_member_list = QTextEdit(manage_group)
        self.group_member_list.setObjectName(u"group_member_list")
        self.group_member_list.setGeometry(QRect(20, 90, 104, 70))
        self.add_group_butt = QPushButton(manage_group)
        self.add_group_butt.setObjectName(u"add_group_butt")
        self.add_group_butt.setGeometry(QRect(30, 200, 89, 25))
        self.del_group_butt = QPushButton(manage_group)
        self.del_group_butt.setObjectName(u"del_group_butt")
        self.del_group_butt.setGeometry(QRect(230, 110, 89, 25))

        self.retranslateUi(manage_group)

        QMetaObject.connectSlotsByName(manage_group)
    # setupUi

    def retranslateUi(self, manage_group):
        manage_group.setWindowTitle(QCoreApplication.translate("manage_group", u"Form", None))
        self.label_2.setText(QCoreApplication.translate("manage_group", u"<html><head/><body><p>\u65b0\u6dfb\u52a0\u6210\u5458</p></body></html>", None))
        self.add_group_butt.setText(QCoreApplication.translate("manage_group", u"\u6dfb\u52a0", None))
        self.del_group_butt.setText(QCoreApplication.translate("manage_group", u"\u5220\u9664\u7fa4\u804a", None))
    # retranslateUi

