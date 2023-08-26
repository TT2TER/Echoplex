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
        chatroom.resize(802, 419)
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
        self.horizontalLayout_4 = QHBoxLayout(chatroom)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.img_show = QLabel(chatroom)
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

        self.img_butt = PushButton(chatroom)
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

        self.pushButton = QPushButton(chatroom)
        self.pushButton.setObjectName(u"pushButton")

        self.verticalLayout.addWidget(self.pushButton)

        self.send_butt = PushButton(chatroom)
        self.send_butt.setObjectName(u"send_butt")

        self.verticalLayout.addWidget(self.send_butt)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.horizontalLayout)


        self.horizontalLayout_2.addLayout(self.verticalLayout_2)

        self.tabWidget = QTabWidget(chatroom)
        self.tabWidget.setObjectName(u"tabWidget")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tabWidget.sizePolicy().hasHeightForWidth())
        self.tabWidget.setSizePolicy(sizePolicy)
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
        self.tab = QWidget()
        self.tab.setObjectName(u"tab")
        self.verticalLayout_3 = QVBoxLayout(self.tab)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.chat_list_view = QListWidget(self.tab)
        QListWidgetItem(self.chat_list_view)
        QListWidgetItem(self.chat_list_view)
        self.chat_list_view.setObjectName(u"chat_list_view")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.chat_list_view.sizePolicy().hasHeightForWidth())
        self.chat_list_view.setSizePolicy(sizePolicy1)
        self.chat_list_view.setMinimumSize(QSize(380, 0))
        self.chat_list_view.setMaximumSize(QSize(380, 16777215))
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

        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.verticalLayout_6 = QVBoxLayout(self.tab_2)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.toolBox = QToolBox(self.tab_2)
        self.toolBox.setObjectName(u"toolBox")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 88, 88))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.listWidget_2 = QListWidget(self.page)
        self.listWidget_2.setObjectName(u"listWidget_2")

        self.verticalLayout_4.addWidget(self.listWidget_2)

        self.toolBox.addItem(self.page, u"\u6211\u7684\u597d\u53cb")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 384, 293))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listWidget_3 = QListWidget(self.page_2)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_5.addWidget(self.listWidget_3)

        self.toolBox.addItem(self.page_2, u"Page 2")

        self.verticalLayout_6.addWidget(self.toolBox)

        self.tabWidget.addTab(self.tab_2, "")

        self.horizontalLayout_2.addWidget(self.tabWidget)


        self.horizontalLayout_3.addLayout(self.horizontalLayout_2)


        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)


        self.retranslateUi(chatroom)

        self.tabWidget.setCurrentIndex(0)
        self.toolBox.setCurrentIndex(1)


        QMetaObject.connectSlotsByName(chatroom)
    # setupUi

    def retranslateUi(self, chatroom):
        chatroom.setWindowTitle(QCoreApplication.translate("chatroom", u"Form", None))
        self.img_show.setText(QCoreApplication.translate("chatroom", u"<html><head/><body><p><br/></p></body></html>", None))
        self.img_butt.setText(QCoreApplication.translate("chatroom", u"\u70b9\u51fb\u4e0a\u4f20\u5934\u50cf", None))
        self.pushButton.setText(QCoreApplication.translate("chatroom", u"PushButton", None))
        self.send_butt.setText(QCoreApplication.translate("chatroom", u"send", None))

        __sortingEnabled = self.chat_list_view.isSortingEnabled()
        self.chat_list_view.setSortingEnabled(False)
        ___qlistwidgetitem = self.chat_list_view.item(0)
        ___qlistwidgetitem.setText(QCoreApplication.translate("chatroom", u"New Item", None));
        ___qlistwidgetitem1 = self.chat_list_view.item(1)
        ___qlistwidgetitem1.setText(QCoreApplication.translate("chatroom", u"New Item", None));
        self.chat_list_view.setSortingEnabled(__sortingEnabled)

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), QCoreApplication.translate("chatroom", u"Tab 1", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("chatroom", u"\u6211\u7684\u597d\u53cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), QCoreApplication.translate("chatroom", u"Page 2", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("chatroom", u"Tab 2", None))
    # retranslateUi

