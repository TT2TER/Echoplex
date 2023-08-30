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

from qfluentwidgets import PushButton
from qfluentwidgets import LineEdit


class Ui_add_friend(object):
    def setupUi(self, add_friend):
        if not add_friend.objectName():
            add_friend.setObjectName(u"add_friend")
        add_friend.resize(184, 199)
        self.horizontalLayout = QHBoxLayout(add_friend)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.mini_butt = QPushButton(add_friend)
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

        self.close_butt = QPushButton(add_friend)
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

        self.label = QLabel(add_friend)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.id_in = LineEdit(add_friend)
        self.id_in.setObjectName(u"id_in")

        self.verticalLayout.addWidget(self.id_in)

        self.add_fri_butt = PushButton(add_friend)
        self.add_fri_butt.setObjectName(u"add_fri_butt")

        self.verticalLayout.addWidget(self.add_fri_butt)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.retranslateUi(add_friend)

        QMetaObject.connectSlotsByName(add_friend)
    # setupUi

    def retranslateUi(self, add_friend):
        add_friend.setWindowTitle(QCoreApplication.translate("add_friend", u"Form", None))
        self.mini_butt.setText(QCoreApplication.translate("add_friend", u"\u2796", None))
        self.close_butt.setText(QCoreApplication.translate("add_friend", u"\u2716", None))
        self.label.setText(QCoreApplication.translate("add_friend", u"\u8bf7\u8f93\u5165\u597d\u53cbid:", None))
        self.add_fri_butt.setText(QCoreApplication.translate("add_friend", u"\u6dfb\u52a0\u597d\u53cb", None))
    # retranslateUi

