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
        new_friends.resize(440, 312)
        self.verticalLayout = QVBoxLayout(new_friends)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(new_friends)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.mini_butt = QPushButton(new_friends)
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

        self.close_butt = QPushButton(new_friends)
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


        self.horizontalLayout.addLayout(self.horizontalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.new_friends_box = QListWidget(new_friends)
        self.new_friends_box.setObjectName(u"new_friends_box")
        self.new_friends_box.setStyleSheet(u"QListWidget::item:selected {\n"
"        background-color:rgba(255, 255, 255, 0); /* \u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272\u8bbe\u4e3a\u900f\u660e */\n"
"    }")

        self.verticalLayout.addWidget(self.new_friends_box)


        self.retranslateUi(new_friends)

        QMetaObject.connectSlotsByName(new_friends)
    # setupUi

    def retranslateUi(self, new_friends):
        new_friends.setWindowTitle(QCoreApplication.translate("new_friends", u"Form", None))
        self.label.setText(QCoreApplication.translate("new_friends", u"\u65b0\u597d\u53cb\u4fe1\u606f\u5904\u7406", None))
        self.mini_butt.setText(QCoreApplication.translate("new_friends", u"\u2796", None))
        self.close_butt.setText(QCoreApplication.translate("new_friends", u"\u2716", None))
    # retranslateUi

