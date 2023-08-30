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


class Ui_chatroom(object):
    def setupUi(self, chatroom):
        if not chatroom.objectName():
            chatroom.setObjectName(u"chatroom")
        chatroom.resize(1454, 1056)
        chatroom.setStyleSheet(u"/* \u8bbe\u7f6e\u6574\u4e2a QTabWidget \u7684\u6837\u5f0f */\n"
"QTabWidget {\n"
"    background-color: #f0f0f0;\n"
"    border: 1px solid #d0d0d0;\n"
"    border-radius: 10px; /* \u6dfb\u52a0\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u9009\u9879\u5361\u90e8\u5206\u7684\u6837\u5f0f */\n"
"QTabBar {\n"
"    background-color: #e0e0e0;\n"
"    border-top-left-radius: 10px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 10px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u9009\u4e2d\u9009\u9879\u5361\u7684\u6837\u5f0f */\n"
"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    color: #333333;\n"
"    border-top-left-radius: 10px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 10px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u672a\u9009\u4e2d\u9009\u9879\u5361\u7684\u6837\u5f0f */\n"
"QTabBar::tab {\n"
"    background-color: #c0c0c0;\n"
"    color: #666666;\n"
""
                        "    border-top-left-radius: 10px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 10px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e QTabWidget \u5185\u90e8\u7684\u6837\u5f0f */\n"
"QTabWidget::pane {\n"
"    border-top: 1px solid #d0d0d0;\n"
"    background-color: white;\n"
"    border-bottom-left-radius: 10px; /* \u6dfb\u52a0\u5de6\u4e0b\u89d2\u5706\u89d2 */\n"
"    border-bottom-right-radius: 10px; /* \u6dfb\u52a0\u53f3\u4e0b\u89d2\u5706\u89d2 */\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(chatroom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.left = QVBoxLayout()
        self.left.setObjectName(u"left")
        self.avatar_show = QLabel(chatroom)
        self.avatar_show.setObjectName(u"avatar_show")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.avatar_show.sizePolicy().hasHeightForWidth())
        self.avatar_show.setSizePolicy(sizePolicy)
        self.avatar_show.setMinimumSize(QSize(50, 50))
        self.avatar_show.setMaximumSize(QSize(80, 80))
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
        self.avatar_show.setPalette(palette)
        self.avatar_show.setCursor(QCursor(Qt.ArrowCursor))
        self.avatar_show.setFrameShape(QFrame.NoFrame)
        self.avatar_show.setFrameShadow(QFrame.Raised)
        self.avatar_show.setTextFormat(Qt.AutoText)
        self.avatar_show.setScaledContents(False)

        self.left.addWidget(self.avatar_show)

        self.avatar_butt = PushButton(chatroom)
        self.avatar_butt.setObjectName(u"avatar_butt")
        self.avatar_butt.setMaximumSize(QSize(100, 16777215))
        palette1 = QPalette()
        brush4 = QBrush(QColor(1, 83, 168, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush2)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush2)
        self.avatar_butt.setPalette(palette1)
        self.avatar_butt.setCursor(QCursor(Qt.PointingHandCursor))

        self.left.addWidget(self.avatar_butt)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left.addItem(self.verticalSpacer_2)

        self.group_manage_butt = QPushButton(chatroom)
        self.group_manage_butt.setObjectName(u"group_manage_butt")

        self.left.addWidget(self.group_manage_butt)

        self.setting_butt = QPushButton(chatroom)
        self.setting_butt.setObjectName(u"setting_butt")
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.setting_butt.sizePolicy().hasHeightForWidth())
        self.setting_butt.setSizePolicy(sizePolicy1)

        self.left.addWidget(self.setting_butt)


        self.horizontalLayout_3.addLayout(self.left)

        self.middle = QVBoxLayout()
        self.middle.setObjectName(u"middle")
        self.view_box = QListWidget(chatroom)
        self.view_box.setObjectName(u"view_box")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.view_box.sizePolicy().hasHeightForWidth())
        self.view_box.setSizePolicy(sizePolicy2)
        self.view_box.setMinimumSize(QSize(900, 600))
        self.view_box.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.middle.addWidget(self.view_box)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.middle.addLayout(self.horizontalLayout_2)

        self.tabWidget_2 = QTabWidget(chatroom)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy3)
        self.tabWidget_2.setMinimumSize(QSize(0, 400))
        self.tabWidget_2.setMaximumSize(QSize(16777215, 370))
        self.text = QWidget()
        self.text.setObjectName(u"text")
        sizePolicy2.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy2)
        self.layoutWidget = QWidget(self.text)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 802, 335))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_in = TextEdit(self.layoutWidget)
        self.text_in.setObjectName(u"text_in")
        sizePolicy4 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.text_in.sizePolicy().hasHeightForWidth())
        self.text_in.setSizePolicy(sizePolicy4)
        self.text_in.setMinimumSize(QSize(800, 250))
        self.text_in.setMaximumSize(QSize(700, 300))

        self.verticalLayout.addWidget(self.text_in)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.wisper_butt = QPushButton(self.layoutWidget)
        self.wisper_butt.setObjectName(u"wisper_butt")
        sizePolicy1.setHeightForWidth(self.wisper_butt.sizePolicy().hasHeightForWidth())
        self.wisper_butt.setSizePolicy(sizePolicy1)
        self.wisper_butt.setMinimumSize(QSize(80, 31))
        self.wisper_butt.setMaximumSize(QSize(80, 31))

        self.horizontalLayout.addWidget(self.wisper_butt)

        self.video_butt = QPushButton(self.layoutWidget)
        self.video_butt.setObjectName(u"video_butt")
        sizePolicy1.setHeightForWidth(self.video_butt.sizePolicy().hasHeightForWidth())
        self.video_butt.setSizePolicy(sizePolicy1)
        self.video_butt.setMinimumSize(QSize(80, 31))
        self.video_butt.setMaximumSize(QSize(80, 31))

        self.horizontalLayout.addWidget(self.video_butt)

        self.send_file_butt = QPushButton(self.layoutWidget)
        self.send_file_butt.setObjectName(u"send_file_butt")
        sizePolicy1.setHeightForWidth(self.send_file_butt.sizePolicy().hasHeightForWidth())
        self.send_file_butt.setSizePolicy(sizePolicy1)
        self.send_file_butt.setMinimumSize(QSize(80, 31))
        self.send_file_butt.setMaximumSize(QSize(80, 31))

        self.horizontalLayout.addWidget(self.send_file_butt)

        self.send_butt = PushButton(self.layoutWidget)
        self.send_butt.setObjectName(u"send_butt")
        sizePolicy1.setHeightForWidth(self.send_butt.sizePolicy().hasHeightForWidth())
        self.send_butt.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.send_butt)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tabWidget_2.addTab(self.text, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget_2.addTab(self.tab_2, "")

        self.middle.addWidget(self.tabWidget_2)


        self.horizontalLayout_3.addLayout(self.middle)

        self.tabWidget = QTabWidget(chatroom)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy5 = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy5.setHorizontalStretch(0)
        sizePolicy5.setVerticalStretch(0)
        sizePolicy5.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy5)
        self.tabWidget.setMinimumSize(QSize(420, 0))
        self.tabWidget.setMaximumSize(QSize(420, 16777215))
        self.tabWidget.setStyleSheet(u"/* \u8bbe\u7f6e\u6574\u4e2a QTabWidget \u7684\u6837\u5f0f */\n"
"QTabWidget {\n"
"    background-color: #f0f0f0;\n"
"    border: 2px solid #d0d0d0;\n"
"    border-radius: 10px; /* \u6dfb\u52a0\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u9009\u9879\u5361\u90e8\u5206\u7684\u6837\u5f0f */\n"
"QTabBar {\n"
"    background-color: #e0e0e0;\n"
"    border-top-left-radius: 5px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 5px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u9009\u4e2d\u9009\u9879\u5361\u7684\u6837\u5f0f */\n"
"QTabBar::tab:selected {\n"
"    background-color: white;\n"
"    color: #333333;\n"
"    border-top-left-radius: 5px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 5px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u672a\u9009\u4e2d\u9009\u9879\u5361\u7684\u6837\u5f0f */\n"
"QTabBar::tab {\n"
"    background-color: #c0c0c0;\n"
"    color: #666666;\n"
"   "
                        " border-top-left-radius: 5px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 5px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e QTabWidget \u5185\u90e8\u7684\u6837\u5f0f */\n"
"QTabWidget::pane {\n"
"    border-top: 1px solid #d0d0d0;\n"
"    background-color: white;\n"
"    border-bottom-left-radius: 10px; /* \u6dfb\u52a0\u5de6\u4e0b\u89d2\u5706\u89d2 */\n"
"    border-bottom-right-radius: 10px; /* \u6dfb\u52a0\u53f3\u4e0b\u89d2\u5706\u89d2 */\n"
"	border-top-right-radius: 10px;\n"
"}\n"
"")
        self.chat_list = QWidget()
        self.chat_list.setObjectName(u"chat_list")
        self.verticalLayout_7 = QVBoxLayout(self.chat_list)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.new_group_butt = QPushButton(self.chat_list)
        self.new_group_butt.setObjectName(u"new_group_butt")

        self.horizontalLayout_5.addWidget(self.new_group_butt)

        self.add_new_chat = QPushButton(self.chat_list)
        self.add_new_chat.setObjectName(u"add_new_chat")

        self.horizontalLayout_5.addWidget(self.add_new_chat)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.chat_list_view = QListWidget(self.chat_list)
        self.chat_list_view.setObjectName(u"chat_list_view")
        sizePolicy2.setHeightForWidth(self.chat_list_view.sizePolicy().hasHeightForWidth())
        self.chat_list_view.setSizePolicy(sizePolicy2)
        self.chat_list_view.setMinimumSize(QSize(420, 0))
        self.chat_list_view.setMaximumSize(QSize(420, 16777215))
        self.chat_list_view.setStyleSheet(u"QListWidget {\n"
"    border-radius: 10px;\n"
"    background-color: #f0f0f0; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272 */\n"
"    border: 3px solid #d0d0d0; /* \u8bbe\u7f6e\u8fb9\u6846 */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"}\n"
"\n"
"QListWidget::item {\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5217\u8868\u9879\u5185\u8fb9\u8ddd */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: #a0a0a0; /* \u8bbe\u7f6e\u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272 */\n"
"    color: white; /* \u8bbe\u7f6e\u9009\u4e2d\u9879\u7684\u6587\u5b57\u989c\u8272 */\n"
"}\n"
"")

        self.verticalLayout_3.addWidget(self.chat_list_view)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.chat_list, "")
        self.friend_list = QWidget()
        self.friend_list.setObjectName(u"friend_list")
        self.toolBox = QToolBox(self.friend_list)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(9, 46, 274, 278))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 274, 210))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.my_friend = QListWidget(self.page)
        self.my_friend.setObjectName(u"my_friend")

        self.verticalLayout_4.addWidget(self.my_friend)

        self.toolBox.addItem(self.page, u"\u6211\u7684\u597d\u53cb")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 88, 88))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listWidget_3 = QListWidget(self.page_2)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_5.addWidget(self.listWidget_3)

        self.toolBox.addItem(self.page_2, u"Page 2")
        self.add_friend_butt = QPushButton(self.friend_list)
        self.add_friend_butt.setObjectName(u"add_friend_butt")
        self.add_friend_butt.setGeometry(QRect(130, 10, 80, 31))
        self.widget = QWidget(self.friend_list)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 10, 98, 31))
        self.get_new_friend_num = QLabel(self.widget)
        self.get_new_friend_num.setObjectName(u"get_new_friend_num")
        self.get_new_friend_num.setGeometry(QRect(0, 0, 21, 17))
        self.get_new_friend = QPushButton(self.widget)
        self.get_new_friend.setObjectName(u"get_new_friend")
        self.get_new_friend.setGeometry(QRect(20, 0, 71, 25))
        self.tabWidget.addTab(self.friend_list, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(chatroom)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(chatroom)
    # setupUi

    def retranslateUi(self, chatroom):
        chatroom.setWindowTitle(QCoreApplication.translate("chatroom", u"Form", None))
        self.avatar_show.setText(QCoreApplication.translate("chatroom", u"<html><head/><body><p><br/></p></body></html>", None))
        self.avatar_butt.setText(QCoreApplication.translate("chatroom", u"\u70b9\u51fb\u4e0a\u4f20\u5934\u50cf", None))
        self.group_manage_butt.setText(QCoreApplication.translate("chatroom", u"\u7fa4\u7ec4\u7ba1\u7406", None))
        self.setting_butt.setText(QCoreApplication.translate("chatroom", u"\u8bbe\u7f6e", None))
        self.wisper_butt.setText(QCoreApplication.translate("chatroom", u"\u8f6c\u6587\u5b57", None))
        self.video_butt.setText(QCoreApplication.translate("chatroom", u"\u89c6\u9891\u901a\u8bdd", None))
        self.send_file_butt.setText(QCoreApplication.translate("chatroom", u"\u53d1\u9001\u6587\u4ef6", None))
        self.send_butt.setText(QCoreApplication.translate("chatroom", u"\u53d1\u9001\u6d88\u606f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.text), QCoreApplication.translate("chatroom", u"\u53d1\u9001\u6d88\u606f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("chatroom", u"\u8868\u60c5", None))
        self.new_group_butt.setText(QCoreApplication.translate("chatroom", u"\u521b\u5efa\u7fa4\u804a\u952e", None))
        self.add_new_chat.setText(QCoreApplication.translate("chatroom", u"\u8c03\u8bd5\u7528", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chat_list), QCoreApplication.translate("chatroom", u"\u6d88\u606f\u5217\u8868", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("chatroom", u"\u6211\u7684\u597d\u53cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("chatroom", u"Page 2", None))
        self.add_friend_butt.setText(QCoreApplication.translate("chatroom", u"\u6dfb\u52a0\u597d\u53cb", None))
        self.get_new_friend_num.setText(QCoreApplication.translate("chatroom", u"99", None))
        self.get_new_friend.setText(QCoreApplication.translate("chatroom", u"\u65b0\u597d\u53cb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.friend_list), QCoreApplication.translate("chatroom", u"\u597d\u53cb\u5217\u8868", None))
    # retranslateUi

