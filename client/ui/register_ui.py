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

from qfluentwidgets import LineEdit
from qfluentwidgets import PushButton


class Ui_reg(object):
    def setupUi(self, reg):
        if not reg.objectName():
            reg.setObjectName(u"reg")
        reg.resize(1247, 552)
        self.horizontalLayout_3 = QHBoxLayout(reg)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.label_4 = QLabel(reg)
        self.label_4.setObjectName(u"label_4")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setMinimumSize(QSize(1045, 532))
        self.label_4.setMaximumSize(QSize(1045, 532))
        self.label_4.setPixmap(QPixmap(u"/client/lib/login_back.png"))
        self.label_4.setScaledContents(True)

        self.horizontalLayout_2.addWidget(self.label_4)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.img_show = QLabel(reg)
        self.img_show.setObjectName(u"img_show")
        self.img_show.setMinimumSize(QSize(50, 50))
        self.img_show.setMaximumSize(QSize(80, 80))
        palette = QPalette()
        brush = QBrush(QColor(57, 234, 242, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(32, 74, 135, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Base, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush1)
        brush2 = QBrush(QColor(190, 190, 190, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        brush3 = QBrush(QColor(239, 239, 239, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        self.img_show.setPalette(palette)
        self.img_show.setCursor(QCursor(Qt.ArrowCursor))
        self.img_show.setFrameShape(QFrame.NoFrame)
        self.img_show.setFrameShadow(QFrame.Raised)
        self.img_show.setTextFormat(Qt.AutoText)
        self.img_show.setScaledContents(False)

        self.verticalLayout.addWidget(self.img_show, 0, Qt.AlignHCenter)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.img_butt = PushButton(reg)
        self.img_butt.setObjectName(u"img_butt")
        self.img_butt.setMaximumSize(QSize(100, 16777215))
        palette1 = QPalette()
        brush4 = QBrush(QColor(1, 83, 168, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.img_butt.setPalette(palette1)
        self.img_butt.setCursor(QCursor(Qt.PointingHandCursor))

        self.verticalLayout.addWidget(self.img_butt, 0, Qt.AlignHCenter)

        self.label = QLabel(reg)
        self.label.setObjectName(u"label")
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        brush5 = QBrush(QColor(52, 101, 164, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.Text, brush5)
        brush6 = QBrush(QColor(0, 0, 0, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette2.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        brush7 = QBrush(QColor(52, 101, 164, 128))
        brush7.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Active, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette2.setBrush(QPalette.Inactive, QPalette.Text, brush5)
        palette2.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush7)
#endif
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.Text, brush2)
        palette2.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette2.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.label.setPalette(palette2)

        self.verticalLayout.addWidget(self.label)

        self.name_in = LineEdit(reg)
        self.name_in.setObjectName(u"name_in")

        self.verticalLayout.addWidget(self.name_in)

        self.label_2 = QLabel(reg)
        self.label_2.setObjectName(u"label_2")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_2.setPalette(palette3)

        self.verticalLayout.addWidget(self.label_2)

        self.num_in = LineEdit(reg)
        self.num_in.setObjectName(u"num_in")
        self.num_in.setClearButtonEnabled(False)

        self.verticalLayout.addWidget(self.num_in)

        self.label_5 = QLabel(reg)
        self.label_5.setObjectName(u"label_5")
        palette4 = QPalette()
        palette4.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette4.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_5.setPalette(palette4)

        self.verticalLayout.addWidget(self.label_5)

        self.mail_in = LineEdit(reg)
        self.mail_in.setObjectName(u"mail_in")
        self.mail_in.setClearButtonEnabled(True)

        self.verticalLayout.addWidget(self.mail_in)

        self.label_3 = QLabel(reg)
        self.label_3.setObjectName(u"label_3")
        palette5 = QPalette()
        palette5.setBrush(QPalette.Active, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Inactive, QPalette.WindowText, brush1)
        palette5.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        self.label_3.setPalette(palette5)

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

        self.buttonBox = QDialogButtonBox(reg)
        self.buttonBox.setObjectName(u"buttonBox")
        self.buttonBox.setStandardButtons(QDialogButtonBox.NoButton)

        self.verticalLayout.addWidget(self.buttonBox)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.reg_cancel = PushButton(reg)
        self.reg_cancel.setObjectName(u"reg_cancel")
        palette6 = QPalette()
        palette6.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Button, brush3)
        brush9 = QBrush(QColor(255, 255, 255, 255))
        brush9.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Light, brush9)
        brush10 = QBrush(QColor(247, 247, 247, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Midlight, brush10)
        brush11 = QBrush(QColor(119, 119, 119, 255))
        brush11.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Dark, brush11)
        brush12 = QBrush(QColor(159, 159, 159, 255))
        brush12.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.Mid, brush12)
        palette6.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Active, QPalette.BrightText, brush9)
        palette6.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Active, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Active, QPalette.Window, brush3)
        palette6.setBrush(QPalette.Active, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Active, QPalette.AlternateBase, brush10)
        brush13 = QBrush(QColor(255, 255, 220, 255))
        brush13.setStyle(Qt.SolidPattern)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipBase, brush13)
        palette6.setBrush(QPalette.Active, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Light, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Midlight, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.Dark, brush11)
        palette6.setBrush(QPalette.Inactive, QPalette.Mid, brush12)
        palette6.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.BrightText, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.Base, brush9)
        palette6.setBrush(QPalette.Inactive, QPalette.Window, brush3)
        palette6.setBrush(QPalette.Inactive, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Inactive, QPalette.AlternateBase, brush10)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipBase, brush13)
        palette6.setBrush(QPalette.Inactive, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette6.setBrush(QPalette.Disabled, QPalette.WindowText, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Button, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Light, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.Midlight, brush10)
        palette6.setBrush(QPalette.Disabled, QPalette.Dark, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Mid, brush12)
        palette6.setBrush(QPalette.Disabled, QPalette.Text, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.BrightText, brush9)
        palette6.setBrush(QPalette.Disabled, QPalette.ButtonText, brush11)
        palette6.setBrush(QPalette.Disabled, QPalette.Base, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Window, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.Shadow, brush6)
        palette6.setBrush(QPalette.Disabled, QPalette.AlternateBase, brush3)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipBase, brush13)
        palette6.setBrush(QPalette.Disabled, QPalette.ToolTipText, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette6.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.reg_cancel.setPalette(palette6)
        self.reg_cancel.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.reg_cancel)

        self.reg_confirm = PushButton(reg)
        self.reg_confirm.setObjectName(u"reg_confirm")
        palette7 = QPalette()
        palette7.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Active, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette7.setBrush(QPalette.Inactive, QPalette.Text, brush6)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush8)
#endif
        palette7.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette7.setBrush(QPalette.Disabled, QPalette.Text, brush2)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette7.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush8)
#endif
        self.reg_confirm.setPalette(palette7)
        self.reg_confirm.setCursor(QCursor(Qt.PointingHandCursor))

        self.horizontalLayout.addWidget(self.reg_confirm)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(reg)

        QMetaObject.connectSlotsByName(reg)
    # setupUi

    def retranslateUi(self, reg):
        reg.setWindowTitle(QCoreApplication.translate("reg", u"Form", None))
        self.label_4.setText("")
        self.img_show.setText(QCoreApplication.translate("reg", u"<html><head/><body><p><br/></p></body></html>", None))
        self.img_butt.setText(QCoreApplication.translate("reg", u"\u70b9\u51fb\u4e0a\u4f20\u5934\u50cf", None))
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

