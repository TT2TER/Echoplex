# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'chatroom.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import TextEdit
from qfluentwidgets import ListWidget


class Ui_chatroom(object):
    def setupUi(self, chatroom):
        if not chatroom.objectName():
            chatroom.setObjectName(u"chatroom")
        chatroom.resize(802, 419)
        self.layoutWidget = QWidget(chatroom)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(0, 0, 760, 398))
        self.horizontalLayout_3 = QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.img_show = QLabel(self.layoutWidget)
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

        self.verticalLayout_7.addWidget(self.img_show)

        self.img_butt = PushButton(self.layoutWidget)
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

        self.verticalLayout_7.addWidget(self.img_butt)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(self.layoutWidget)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.chat_list_view = ListWidget(self.tab)
        self.chat_list_view.setObjectName(u"chat_list_view")
        sizePolicy.setHeightForWidth(self.chat_list_view.sizePolicy().hasHeightForWidth())
        self.chat_list_view.setSizePolicy(sizePolicy)

        self.verticalLayout_3.addWidget(self.chat_list_view)

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolBox = QToolBox(self.tab_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 98, 88))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listWidget_2 = QListWidget(self.page)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_4.addWidget(self.listWidget_2)

        self.toolBox.addItem(self.page, u"\u6211\u7684\u597d\u53cb")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 274, 277))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listWidget_3 = QListWidget(self.page_2)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_5.addWidget(self.listWidget_3)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_6.addWidget(self.toolBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.view_box = QListWidget(self.layoutWidget)
        self.view_box.setObjectName(u"view_box")

        self.verticalLayout_2.addWidget(self.view_box)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_in = TextEdit(self.layoutWidget)
        self.text_in.setObjectName(u"text_in")

        self.horizontalLayout.addWidget(self.text_in)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.send_butt = PushButton(self.layoutWidget)
        self.send_butt.setObjectName(u"send_butt")

        self.verticalLayout.addWidget(self.send_butt)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.retranslateUi(chatroom)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(chatroom)
    # setupUi

    def retranslateUi(self, chatroom):
        chatroom.setWindowTitle(QCoreApplication.translate("chatroom", u"Form", None))
        self.img_show.setText(QCoreApplication.translate("chatroom", u"<html><head/><body><p><br/></p></body></html>", None))
        self.img_butt.setText(QCoreApplication.translate("chatroom", u"\u70b9\u51fb\u4e0a\u4f20\u5934\u50cf", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("chatroom", u"Tab 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("chatroom", u"\u6211\u7684\u597d\u53cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("chatroom", u"Page 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("chatroom", u"Tab 2", None))
        self.pushButton.setText(QCoreApplication.translate("chatroom", u"PushButton", None))
        self.send_butt.setText(QCoreApplication.translate("chatroom", u"send", None))
    # retranslateUi

