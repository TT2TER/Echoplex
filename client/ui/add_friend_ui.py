# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_friend.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_add_friend(object):
    def setupUi(self, add_friend):
        if not add_friend.objectName():
            add_friend.setObjectName(u"add_friend")
        add_friend.resize(400, 300)
        self.id_in = QLineEdit(add_friend)
        self.id_in.setObjectName(u"id_in")
        self.id_in.setGeometry(QRect(110, 60, 113, 25))
        self.label = QLabel(add_friend)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(110, 30, 131, 17))
        self.add_fri_butt = QPushButton(add_friend)
        self.add_fri_butt.setObjectName(u"add_fri_butt")
        self.add_fri_butt.setGeometry(QRect(120, 100, 89, 25))

        self.retranslateUi(add_friend)

        QMetaObject.connectSlotsByName(add_friend)
    # setupUi

    def retranslateUi(self, add_friend):
        add_friend.setWindowTitle(QCoreApplication.translate("add_friend", u"Form", None))
        self.label.setText(QCoreApplication.translate("add_friend", u"\u8bf7\u8f93\u5165\u597d\u53cbid:", None))
        self.add_fri_butt.setText(QCoreApplication.translate("add_friend", u"\u6dfb\u52a0\u597d\u53cb", None))
    # retranslateUi

