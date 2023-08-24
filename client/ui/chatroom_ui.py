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
from qfluentwidgets import ImageLabel
from qfluentwidgets import AvatarWidget
from qfluentwidgets import TextEdit
from qfluentwidgets import ListWidget


class Ui_chatroom(object):
    def setupUi(self, chatroom):
        if not chatroom.objectName():
            chatroom.setObjectName(u"chatroom")
        chatroom.resize(739, 503)
        self.verticalLayout_8 = QVBoxLayout(chatroom)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.AvatarWidget = AvatarWidget(chatroom)
        self.AvatarWidget.setObjectName(u"AvatarWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.AvatarWidget.sizePolicy().hasHeightForWidth())
        self.AvatarWidget.setSizePolicy(sizePolicy)
        self.AvatarWidget.setMinimumSize(QSize(40, 40))
        self.AvatarWidget.setMaximumSize(QSize(40, 40))
        self.AvatarWidget.setBaseSize(QSize(40, 40))
        self.AvatarWidget.setPixmap(QPixmap(u"../../../../../Pictures/Camera Roll/\u622a\u56fe-FIFA.png"))
        self.AvatarWidget.setScaledContents(False)

        self.verticalLayout_7.addWidget(self.AvatarWidget)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_7.addItem(self.verticalSpacer_2)


        self.horizontalLayout_3.addLayout(self.verticalLayout_7)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tabWidget = QTabWidget(chatroom)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy1 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy1)
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.ListWidget = ListWidget(self.tab)
        QListWidgetItem(self.ListWidget)
        QListWidgetItem(self.ListWidget)
        QListWidgetItem(self.ListWidget)
        self.ListWidget.setObjectName(u"ListWidget")
        sizePolicy1.setHeightForWidth(self.ListWidget.sizePolicy().hasHeightForWidth())
        self.ListWidget.setSizePolicy(sizePolicy1)

        self.verticalLayout_3.addWidget(self.ListWidget)

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
        self.page_2.setGeometry(QRect(0, 0, 98, 88))
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
        self.view_box = QListWidget(chatroom)
        self.view_box.setObjectName(u"view_box")

        self.verticalLayout_2.addWidget(self.view_box)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.text_in = TextEdit(chatroom)
        self.text_in.setObjectName(u"text_in")

        self.horizontalLayout.addWidget(self.text_in)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.send_butt = PushButton(chatroom)
        self.send_butt.setObjectName(u"send_butt")

        self.verticalLayout.addWidget(self.send_butt)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.verticalLayout_8.addLayout(self.horizontalLayout_3)


        self.retranslateUi(chatroom)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(chatroom)
    # setupUi

    def retranslateUi(self, chatroom):
        chatroom.setWindowTitle(QCoreApplication.translate("chatroom", u"Form", None))

        __sortingEnabled = self.ListWidget.isSortingEnabled()
        self.ListWidget.setSortingEnabled(False)
        ___qlistwidgetitem = self.ListWidget.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("chatroom", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem1 = self.ListWidget.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("chatroom", u"\u65b0\u5efa\u9879\u76ee", None));
        ___qlistwidgetitem2 = self.ListWidget.item(2)
        ___qlistwidgetitem2.setText(QCoreApplication.translate("chatroom", u"\u65b0\u5efa\u9879\u76ee", None));
        self.ListWidget.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("chatroom", u"Tab 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("chatroom", u"\u6211\u7684\u597d\u53cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("chatroom", u"Page 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("chatroom", u"Tab 2", None))
        self.send_butt.setText(QCoreApplication.translate("chatroom", u"send", None))
    # retranslateUi

