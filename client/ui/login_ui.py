# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import LineEdit
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import HyperlinkButton
from qfluentwidgets import BodyLabel


class Ui_Login(object):
    def setupUi(self, Login):
        if not Login.objectName():
            Login.setObjectName(u"Login")
        Login.resize(394, 338)
        self.horizontalLayout = QHBoxLayout(Login)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label = BodyLabel(Login)
        self.label.setObjectName(u"label")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy)
        self.label.setMouseTracking(False)

        self.verticalLayout.addWidget(self.label)

        self.num_in = LineEdit(Login)
        self.num_in.setObjectName(u"num_in")
        sizePolicy1 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.num_in.sizePolicy().hasHeightForWidth())
        self.num_in.setSizePolicy(sizePolicy1)

        self.verticalLayout.addWidget(self.num_in)

        self.label_2 = BodyLabel(Login)
        self.label_2.setObjectName(u"label_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.label_2.sizePolicy().hasHeightForWidth())
        self.label_2.setSizePolicy(sizePolicy2)

        self.verticalLayout.addWidget(self.label_2)

        self.pwd_in = LineEdit(Login)
        self.pwd_in.setObjectName(u"pwd_in")
        self.pwd_in.setCursor(QCursor(Qt.IBeamCursor))

        self.verticalLayout.addWidget(self.pwd_in)

        self.login_butt = PrimaryPushButton(Login)
        self.login_butt.setObjectName(u"login_butt")

        self.verticalLayout.addWidget(self.login_butt)

        self.reg_butt = PrimaryPushButton(Login)
        self.reg_butt.setObjectName(u"reg_butt")

        self.verticalLayout.addWidget(self.reg_butt)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)


        self.gridLayout.addLayout(self.verticalLayout, 1, 0, 1, 1)

        self.dark_mode_butt = HyperlinkButton(Login)
        self.dark_mode_butt.setObjectName(u"dark_mode_butt")

        self.gridLayout.addWidget(self.dark_mode_butt, 0, 1, 1, 1)


        self.horizontalLayout.addLayout(self.gridLayout)


        self.retranslateUi(Login)

        QMetaObject.connectSlotsByName(Login)
    # setupUi

    def retranslateUi(self, Login):
        Login.setWindowTitle(QCoreApplication.translate("Login", u"Form", None))
        self.label.setText(QCoreApplication.translate("Login", u"\u8d26\u53f7", None))
        self.num_in.setInputMask("")
        self.num_in.setText("")
        self.num_in.setPlaceholderText(QCoreApplication.translate("Login", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.label_2.setText(QCoreApplication.translate("Login", u"\u5bc6\u7801", None))
        self.pwd_in.setInputMask("")
        self.pwd_in.setPlaceholderText(QCoreApplication.translate("Login", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.login_butt.setText(QCoreApplication.translate("Login", u"\u767b\u9646", None))
        self.reg_butt.setText(QCoreApplication.translate("Login", u"\u6ce8\u518c", None))
        self.dark_mode_butt.setText(QCoreApplication.translate("Login", u"\u9ed1\u591c\u6a21\u5f0f", None))
    # retranslateUi

