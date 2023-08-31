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

from qfluentwidgets import PushButton
from qfluentwidgets import LineEdit


class Ui_reg(object):
    def setupUi(self, reg):
        if not reg.objectName():
            reg.setObjectName(u"reg")
        reg.resize(1247, 552)
        self.horizontalLayout_3 = QHBoxLayout(reg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.side_pic = QLabel(reg)
        self.side_pic.setObjectName(u"side_pic")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.side_pic.sizePolicy().hasHeightForWidth())
        self.side_pic.setSizePolicy(sizePolicy)
        self.side_pic.setMinimumSize(QSize(1045, 532))
        self.side_pic.setMaximumSize(QSize(1045, 532))
        self.side_pic.setPixmap(QPixmap(u"../dependencies/login_back.png"))
        self.side_pic.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.side_pic)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 10, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.mini_butt = QPushButton(reg)
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

        self.close_butt = QPushButton(reg)
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

        self.label = QLabel(reg)
        self.label.setObjectName(u"label")
        palette = QPalette()
        brush = QBrush(QColor(32, 74, 135, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(52, 101, 164, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush1)
        brush2 = QBrush(QColor(0, 0, 0, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        brush3 = QBrush(QColor(52, 101, 164, 128))
        brush3.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush3)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush3)
#endif
        brush4 = QBrush(QColor(190, 190, 190, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        brush5 = QBrush(QColor(0, 0, 0, 128))
        brush5.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.label.setPalette(palette)

        self.verticalLayout.addWidget(self.label)

        self.name_in = LineEdit(reg)
        self.name_in.setObjectName(u"name_in")

        self.verticalLayout.addWidget(self.name_in)

        self.label_5 = QLabel(reg)
        self.label_5.setObjectName(u"label_5")
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.label_5.setPalette(palette1)

        self.verticalLayout.addWidget(self.label_5)

        self.mail_in = LineEdit(reg)
        self.mail_in.setObjectName(u"mail_in")
        self.mail_in.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.mail_in)

        self.label_3 = QLabel(reg)
        self.label_3.setObjectName(u"label_3")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        self.label_3.setPalette(palette2)

        self.verticalLayout.addWidget(self.label_3)

        self.pwd_in = LineEdit(reg)
        self.pwd_in.setObjectName(u"pwd_in")
        self.pwd_in.setEchoMode(QLineEdit.Password)
        self.pwd_in.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.pwd_in)

        self.pwd_check = LineEdit(reg)
        self.pwd_check.setObjectName(u"pwd_check")
        self.pwd_check.setEchoMode(QLineEdit.Password)
        self.pwd_check.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.pwd_check)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reg_cancel = PushButton(reg)
        self.reg_cancel.setObjectName(u"reg_cancel")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        brush6 = QBrush(QColor(239, 239, 239, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Button, brush6)
        brush7 = QBrush(QColor(255, 255, 255, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Light, brush7)
        brush8 = QBrush(QColor(247, 247, 247, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Midlight, brush8)
        brush9 = QBrush(QColor(119, 119, 119, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Dark, brush9)
        brush10 = QBrush(QColor(159, 159, 159, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.Mid, brush10)
        palette3.setBrush(QPalette.Active, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Active, QPalette.BrightText, brush7)
        palette3.setBrush(QPalette.Active, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Active, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Active, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Active, QPalette.Shadow, brush2)
        palette3.setBrush(QPalette.Active, QPalette.AlternateBase, brush8)
        brush11 = QBrush(QColor(255, 255, 220, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipBase, brush11)
        palette3.setBrush(QPalette.Active, QPalette.ToolTipText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Light, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Midlight, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.Dark, brush9)
        palette3.setBrush(QPalette.Inactive, QPalette.Mid, brush10)
        palette3.setBrush(QPalette.Inactive, QPalette.Text, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.BrightText, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.ButtonText, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        palette3.setBrush(QPalette.Inactive, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.Shadow, brush2)
        palette3.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush8)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush11)
        palette3.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Button, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Light, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.Midlight, brush8)
        palette3.setBrush(QPalette.Disabled, QPalette.Dark, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Mid, brush10)
        palette3.setBrush(QPalette.Disabled, QPalette.Text, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.BrightText, brush7)
        palette3.setBrush(QPalette.Disabled, QPalette.ButtonText, brush9)
        palette3.setBrush(QPalette.Disabled, QPalette.Base, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Window, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.Shadow, brush2)
        palette3.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush6)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush11)
        palette3.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette3.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.reg_cancel.setPalette(palette3)
        self.reg_cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.reg_cancel)

        self.reg_confirm = PushButton(reg)
        self.reg_confirm.setObjectName(u"reg_confirm")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Active, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Active, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush2)
        palette4.setBrush(QPalette.Inactive, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush5)
#endif
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        palette4.setBrush(QPalette.Disabled, QPalette.Text, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette4.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush5)
#endif
        self.reg_confirm.setPalette(palette4)
        self.reg_confirm.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.reg_confirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)

        self.buttonBox = QDialogButtonBox(reg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.NoButton)

        self.horizontalLayout_3.addWidget(self.buttonBox)


        self.retranslateUi(reg)

        QMetaObject.connectSlotsByName(reg)
    # setupUi

    def retranslateUi(self, reg):
        reg.setWindowTitle(QCoreApplication.translate("reg", u"Form", None))
        self.side_pic.setText("")
        self.mini_butt.setText(QCoreApplication.translate("reg", u"\u2796", None))
        self.close_butt.setText(QCoreApplication.translate("reg", u"\u2716", None))
        self.label.setText(QCoreApplication.translate("reg", u"\u59d3\u540d", None))
        self.name_in.setPlaceholderText(QCoreApplication.translate("reg", u"\u60a8\u7684\u59d3\u540d", None))
        self.label_5.setText(QCoreApplication.translate("reg", u"\u90ae\u7bb1", None))
        self.mail_in.setPlaceholderText(QCoreApplication.translate("reg", u"******@example.com", None))
        self.label_3.setText(QCoreApplication.translate("reg", u"\u5bc6\u7801", None))
        self.pwd_in.setPlaceholderText(QCoreApplication.translate("reg", u"\u8bf7\u8f93\u5165\u5bc6\u7801", None))
        self.pwd_check.setPlaceholderText(QCoreApplication.translate("reg", u"\u8bf7\u91cd\u590d\u5bc6\u7801", None))
        self.reg_cancel.setText(QCoreApplication.translate("reg", u"\u8fd4\u56de", None))
        self.reg_confirm.setText(QCoreApplication.translate("reg", u"\u6ce8\u518c", None))
    # retranslateUi

