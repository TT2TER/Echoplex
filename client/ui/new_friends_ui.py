# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_friends.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_new_friends(object):
    def setupUi(self, new_friends):
        if not new_friends.objectName():
            new_friends.setObjectName(u"new_friends")
        new_friends.resize(400, 371)
        self.label = QLabel(new_friends)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(40, 10, 151, 61))
        self.new_friends_box = QListWidget(new_friends)
        self.new_friends_box.setObjectName(u"new_friends_box")
        self.new_friends_box.setGeometry(QRect(40, 60, 321, 211))
        self.back_butt = QPushButton(new_friends)
        self.back_butt.setObjectName(u"back_butt")
        self.back_butt.setGeometry(QRect(250, 30, 89, 25))

        self.retranslateUi(new_friends)

        QMetaObject.connectSlotsByName(new_friends)
    # setupUi

    def retranslateUi(self, new_friends):
        new_friends.setWindowTitle(QCoreApplication.translate("new_friends", u"Form", None))
        self.label.setText(QCoreApplication.translate("new_friends", u"\u65b0\u597d\u53cb\u4fe1\u606f\u5904\u7406", None))
        self.back_butt.setText(QCoreApplication.translate("new_friends", u"\u8fd4\u56de", None))
    # retranslateUi

