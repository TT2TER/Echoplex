# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_chat(object):
    def setupUi(self, chat):
        if not chat.objectName():
            chat.setObjectName(u"chat")
        chat.resize(400, 300)

        self.retranslateUi(chat)

        QMetaObject.connectSlotsByName(chat)
    # setupUi

    def retranslateUi(self, chat):
        chat.setWindowTitle(QCoreApplication.translate("chat", u"Form", None))
    # retranslateUi

