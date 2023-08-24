# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_reg(object):
    def setupUi(self, reg):
        if not reg.objectName():
            reg.setObjectName(u"reg")
        reg.resize(325, 413)
        self.verticalLayout_2 = QVBoxLayout(reg)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(reg)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.name_in = QLineEdit(reg)
        self.name_in.setObjectName(u"name_in")

        self.verticalLayout.addWidget(self.name_in)

        self.label_2 = QLabel(reg)
        self.label_2.setObjectName(u"label_2")

        self.verticalLayout.addWidget(self.label_2)

        self.num_in = QLineEdit(reg)
        self.num_in.setObjectName(u"num_in")
        self.num_in.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.num_in)

        self.label_5 = QLabel(reg)
        self.label_5.setObjectName(u"label_5")

        self.verticalLayout.addWidget(self.label_5)

        self.mail_in = QLineEdit(reg)
        self.mail_in.setObjectName(u"mail_in")
        self.mail_in.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.mail_in)

        self.label_3 = QLabel(reg)
        self.label_3.setObjectName(u"label_3")

        self.verticalLayout.addWidget(self.label_3)

        self.pwd_in = QLineEdit(reg)
        self.pwd_in.setObjectName(u"pwd_in")
        self.pwd_in.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.pwd_in)

        self.pwd_check = QLineEdit(reg)
        self.pwd_check.setObjectName(u"pwd_check")
        self.pwd_check.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.pwd_check)

        self.buttonBox = QDialogButtonBox(reg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.NoButton)

        self.verticalLayout.addWidget(self.buttonBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reg_cancel = QPushButton(reg)
        self.reg_cancel.setObjectName(u"reg_cancel")

        self.horizontalLayout.addWidget(self.reg_cancel)

        self.reg_confirm = QPushButton(reg)
        self.reg_confirm.setObjectName(u"reg_confirm")

        self.horizontalLayout.addWidget(self.reg_confirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.retranslateUi(reg)

        QMetaObject.connectSlotsByName(reg)
    # setupUi

    def retranslateUi(self, reg):
        reg.setWindowTitle(QCoreApplication.translate("reg", u"Form", None))
        self.label.setText(QCoreApplication.translate("reg", u"\u59d3\u540d", None))
        self.name_in.setPlaceholderText(QCoreApplication.translate("reg", u"\u60a8\u7684\u59d3\u540d", None))
        self.label_2.setText(QCoreApplication.translate("reg", u"\u8d26\u53f7", None))
        self.num_in.setPlaceholderText(QCoreApplication.translate("reg", u"\u8bf7\u8f93\u5165\u8d26\u53f7", None))
        self.label_5.setText(QCoreApplication.translate("reg", u"\u90ae\u7bb1", None))
        self.mail_in.setPlaceholderText(QCoreApplication.translate("reg", u"******@example.com", None))
        self.label_3.setText(QCoreApplication.translate("reg", u"\u5bc6\u7801", None))
        self.pwd_in.setPlaceholderText(QCoreApplication.translate("reg", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pwd_check.setPlaceholderText(QCoreApplication.translate("reg", u"\u8bf7\u91cd\u590d\u5bc6\u7801", None))
        self.reg_cancel.setText(QCoreApplication.translate("reg", u"\u8fd4\u56de", None))
        self.reg_confirm.setText(QCoreApplication.translate("reg", u"\u6ce8\u518c", None))
    # retranslateUi

