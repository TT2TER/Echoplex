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

from qfluentwidgets import TextEdit


class Ui_chatroom(object):
    def setupUi(self, chatroom):
        if not chatroom.objectName():
            chatroom.setObjectName(u"chatroom")
        chatroom.resize(1476, 1064)
        chatroom.setStyleSheet(u"/* \u8bbe\u7f6e\u6574\u4e2a QTabWidget \u7684\u6837\u5f0f */\n"
"QTabWidget {\n"
"    background-color: rgba(255, 250, 0, 134);\n"
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
"    background-color: rgba(144, 238, 144, 1);\n"
"    color: rgb(85, 87, 83);\n"
"    border-top-left-radius: 5px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 5px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u672a\u9009\u4e2d\u9009\u9879\u5361\u7684\u6837\u5f0f */\n"
"QTabBar::tab {\n"
"    background-color: "
                        "#c0c0c0;\n"
"    color: #666666;\n"
"    border-top-left-radius: 5px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
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
"QListWidget::item:selected {\n"
"        background-color:rgba(255, 255, 255, 0); /* \u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272\u8bbe\u4e3a\u900f\u660e */\n"
"    }")
        self.verticalLayout_2 = QVBoxLayout(chatroom)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_3)

        self.mini_butt = QPushButton(chatroom)
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

        self.close_butt = QPushButton(chatroom)
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


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

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
        self.avatar_show.setStyleSheet(u"QLable{\n"
"	background-color: rgba(191, 64, 64, 0);\n"
"	border: 2px solid #FADB5F;\n"
"}")
        self.avatar_show.setFrameShape(QFrame.NoFrame)
        self.avatar_show.setFrameShadow(QFrame.Raised)
        self.avatar_show.setTextFormat(Qt.AutoText)
        self.avatar_show.setScaledContents(False)

        self.left.addWidget(self.avatar_show)

        self.avatar_butt = QPushButton(chatroom)
        self.avatar_butt.setObjectName(u"avatar_butt")
        self.avatar_butt.setMinimumSize(QSize(120, 30))
        self.avatar_butt.setMaximumSize(QSize(100, 16777215))
        palette1 = QPalette()
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette1.setBrush(QPalette.Active, QPalette.WindowText, brush4)
        gradient = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient.setSpread(QGradient.PadSpread)
        gradient.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient.setColorAt(0, QColor(144, 238, 144, 255))
        gradient.setColorAt(1, QColor(255, 255, 255, 0))
        brush5 = QBrush(gradient)
        palette1.setBrush(QPalette.Active, QPalette.Button, brush5)
        palette1.setBrush(QPalette.Active, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Active, QPalette.ButtonText, brush4)
        gradient1 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient1.setSpread(QGradient.PadSpread)
        gradient1.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient1.setColorAt(0, QColor(144, 238, 144, 255))
        gradient1.setColorAt(1, QColor(255, 255, 255, 0))
        brush6 = QBrush(gradient1)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush6)
        gradient2 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient2.setSpread(QGradient.PadSpread)
        gradient2.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient2.setColorAt(0, QColor(144, 238, 144, 255))
        gradient2.setColorAt(1, QColor(255, 255, 255, 0))
        brush7 = QBrush(gradient2)
        palette1.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(0, 0, 0, 128))
        brush8.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush8)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.WindowText, brush4)
        gradient3 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient3.setSpread(QGradient.PadSpread)
        gradient3.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient3.setColorAt(0, QColor(144, 238, 144, 255))
        gradient3.setColorAt(1, QColor(255, 255, 255, 0))
        brush9 = QBrush(gradient3)
        palette1.setBrush(QPalette.Inactive, QPalette.Button, brush9)
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Inactive, QPalette.ButtonText, brush4)
        gradient4 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient4.setSpread(QGradient.PadSpread)
        gradient4.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient4.setColorAt(0, QColor(144, 238, 144, 255))
        gradient4.setColorAt(1, QColor(255, 255, 255, 0))
        brush10 = QBrush(gradient4)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush10)
        gradient5 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient5.setSpread(QGradient.PadSpread)
        gradient5.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient5.setColorAt(0, QColor(144, 238, 144, 255))
        gradient5.setColorAt(1, QColor(255, 255, 255, 0))
        brush11 = QBrush(gradient5)
        palette1.setBrush(QPalette.Inactive, QPalette.Window, brush11)
        brush12 = QBrush(QColor(0, 0, 0, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.WindowText, brush4)
        gradient6 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient6.setSpread(QGradient.PadSpread)
        gradient6.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient6.setColorAt(0, QColor(144, 238, 144, 255))
        gradient6.setColorAt(1, QColor(255, 255, 255, 0))
        brush13 = QBrush(gradient6)
        palette1.setBrush(QPalette.Disabled, QPalette.Button, brush13)
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush4)
        palette1.setBrush(QPalette.Disabled, QPalette.ButtonText, brush4)
        gradient7 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient7.setSpread(QGradient.PadSpread)
        gradient7.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient7.setColorAt(0, QColor(144, 238, 144, 255))
        gradient7.setColorAt(1, QColor(255, 255, 255, 0))
        brush14 = QBrush(gradient7)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush14)
        gradient8 = QRadialGradient(0.5, 0.5, 0.63, 0.5, 0.5)
        gradient8.setSpread(QGradient.PadSpread)
        gradient8.setCoordinateMode(QGradient.ObjectBoundingMode)
        gradient8.setColorAt(0, QColor(144, 238, 144, 255))
        gradient8.setColorAt(1, QColor(255, 255, 255, 0))
        brush15 = QBrush(gradient8)
        palette1.setBrush(QPalette.Disabled, QPalette.Window, brush15)
        brush16 = QBrush(QColor(0, 0, 0, 128))
        brush16.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush16)
#endif
        self.avatar_butt.setPalette(palette1)
        self.avatar_butt.setCursor(QCursor(Qt.PointingHandCursor))
        self.avatar_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.left.addWidget(self.avatar_butt)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.left.addItem(self.verticalSpacer_2)

        self.group_manage_butt = QPushButton(chatroom)
        self.group_manage_butt.setObjectName(u"group_manage_butt")
        self.group_manage_butt.setMinimumSize(QSize(120, 30))
        self.group_manage_butt.setMaximumSize(QSize(16777215, 30))
        self.group_manage_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.7, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 sto"
                        "p: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.left.addWidget(self.group_manage_butt)

        self.verticalSpacer = QSpacerItem(20, 90, QSizePolicy.Minimum, QSizePolicy.Fixed)

        self.left.addItem(self.verticalSpacer)


        self.horizontalLayout_3.addLayout(self.left)

        self.middle = QVBoxLayout()
        self.middle.setObjectName(u"middle")
        self.view_box = QListWidget(chatroom)
        self.view_box.setObjectName(u"view_box")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Expanding)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.view_box.sizePolicy().hasHeightForWidth())
        self.view_box.setSizePolicy(sizePolicy1)
        self.view_box.setMinimumSize(QSize(900, 600))
        self.view_box.setEditTriggers(QAbstractItemView.NoEditTriggers)

        self.middle.addWidget(self.view_box)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")

        self.middle.addLayout(self.horizontalLayout_2)

        self.tabWidget_2 = QTabWidget(chatroom)
        self.tabWidget_2.setObjectName(u"tabWidget_2")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tabWidget_2.sizePolicy().hasHeightForWidth())
        self.tabWidget_2.setSizePolicy(sizePolicy2)
        self.tabWidget_2.setMinimumSize(QSize(0, 400))
        self.tabWidget_2.setMaximumSize(QSize(16777215, 370))
        self.tabWidget_2.setStyleSheet(u"")
        self.text = QWidget()
        self.text.setObjectName(u"text")
        sizePolicy1.setHeightForWidth(self.text.sizePolicy().hasHeightForWidth())
        self.text.setSizePolicy(sizePolicy1)
        self.layoutWidget = QWidget(self.text)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(10, 0, 802, 354))
        self.verticalLayout = QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.text_in = TextEdit(self.layoutWidget)
        self.text_in.setObjectName(u"text_in")
        sizePolicy3 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.text_in.sizePolicy().hasHeightForWidth())
        self.text_in.setSizePolicy(sizePolicy3)
        self.text_in.setMinimumSize(QSize(800, 200))
        self.text_in.setMaximumSize(QSize(800, 300))

        self.verticalLayout.addWidget(self.text_in)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)

        self.start_record = QLabel(self.layoutWidget)
        self.start_record.setObjectName(u"start_record")

        self.horizontalLayout.addWidget(self.start_record)

        self.wisper_butt = QPushButton(self.layoutWidget)
        self.wisper_butt.setObjectName(u"wisper_butt")
        sizePolicy4 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.wisper_butt.sizePolicy().hasHeightForWidth())
        self.wisper_butt.setSizePolicy(sizePolicy4)
        self.wisper_butt.setMinimumSize(QSize(150, 40))
        self.wisper_butt.setMaximumSize(QSize(150, 40))
        self.wisper_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.wisper_butt)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_4)

        self.video_butt = QPushButton(self.layoutWidget)
        self.video_butt.setObjectName(u"video_butt")
        sizePolicy4.setHeightForWidth(self.video_butt.sizePolicy().hasHeightForWidth())
        self.video_butt.setSizePolicy(sizePolicy4)
        self.video_butt.setMinimumSize(QSize(150, 40))
        self.video_butt.setMaximumSize(QSize(100, 40))
        self.video_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.video_butt)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_5)

        self.send_file_butt = QPushButton(self.layoutWidget)
        self.send_file_butt.setObjectName(u"send_file_butt")
        sizePolicy4.setHeightForWidth(self.send_file_butt.sizePolicy().hasHeightForWidth())
        self.send_file_butt.setSizePolicy(sizePolicy4)
        self.send_file_butt.setMinimumSize(QSize(150, 40))
        self.send_file_butt.setMaximumSize(QSize(100, 40))
        self.send_file_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.send_file_butt)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_6)

        self.send_butt = QPushButton(self.layoutWidget)
        self.send_butt.setObjectName(u"send_butt")
        sizePolicy4.setHeightForWidth(self.send_butt.sizePolicy().hasHeightForWidth())
        self.send_butt.setSizePolicy(sizePolicy4)
        self.send_butt.setMinimumSize(QSize(150, 40))
        self.send_butt.setMaximumSize(QSize(100, 40))
        self.send_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

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
"    background-color: rgba(255, 250, 0, 134);\n"
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
"    background-color: rgba(144, 238, 144, 1);\n"
"    color: rgb(85, 87, 83);\n"
"    border-top-left-radius: 5px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
"    border-top-right-radius: 5px; /* \u6dfb\u52a0\u53f3\u4e0a\u89d2\u5706\u89d2 */\n"
"}\n"
"\n"
"/* \u8bbe\u7f6e\u672a\u9009\u4e2d\u9009\u9879\u5361\u7684\u6837\u5f0f */\n"
"QTabBar::tab {\n"
"    background-color: "
                        "#c0c0c0;\n"
"    color: #666666;\n"
"    border-top-left-radius: 5px; /* \u6dfb\u52a0\u5de6\u4e0a\u89d2\u5706\u89d2 */\n"
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
        sizePolicy6 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy6.setHorizontalStretch(0)
        sizePolicy6.setVerticalStretch(0)
        sizePolicy6.setHeightForWidth(self.new_group_butt.sizePolicy().hasHeightForWidth())
        self.new_group_butt.setSizePolicy(sizePolicy6)
        self.new_group_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")

        self.horizontalLayout_5.addWidget(self.new_group_butt)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_3.addLayout(self.horizontalLayout_5)

        self.chat_list_view = QListWidget(self.chat_list)
        self.chat_list_view.setObjectName(u"chat_list_view")
        sizePolicy1.setHeightForWidth(self.chat_list_view.sizePolicy().hasHeightForWidth())
        self.chat_list_view.setSizePolicy(sizePolicy1)
        self.chat_list_view.setMinimumSize(QSize(410, 0))
        self.chat_list_view.setMaximumSize(QSize(410, 16777215))
        self.chat_list_view.setStyleSheet(u"QListWidget {\n"
"    border-radius: 10px;\n"
"    background-color: #f0f0f0; /* \u8bbe\u7f6e\u80cc\u666f\u989c\u8272 */\n"
"    border: 3px solid #d0d0d0; /* \u8bbe\u7f6e\u8fb9\u6846 */\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5185\u8fb9\u8ddd */\n"
"}\n"
"QListWidget::item {\n"
"    padding: 5px; /* \u8bbe\u7f6e\u5217\u8868\u9879\u5185\u8fb9\u8ddd */\n"
"}\n"
"\n"
"QListWidget::item:selected {\n"
"    background-color: rgba(255, 255, 255, 0); /* \u8bbe\u7f6e\u9009\u4e2d\u9879\u7684\u80cc\u666f\u989c\u8272 *//* \u8bbe\u7f6e\u9009\u4e2d\u9879\u7684\u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"\n"
"")

        self.verticalLayout_3.addWidget(self.chat_list_view)


        self.verticalLayout_7.addLayout(self.verticalLayout_3)

        self.tabWidget.addTab(self.chat_list, "")
        self.friend_list = QWidget()
        self.friend_list.setObjectName(u"friend_list")
        self.toolBox = QToolBox(self.friend_list)
        self.toolBox.setObjectName(u"toolBox")
        self.toolBox.setGeometry(QRect(9, 83, 274, 241))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.page.setGeometry(QRect(0, 0, 274, 173))
        self.verticalLayout_4 = QVBoxLayout(self.page)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.my_friend = QListWidget(self.page)
        self.my_friend.setObjectName(u"my_friend")

        self.verticalLayout_4.addWidget(self.my_friend)

        self.toolBox.addItem(self.page, u"\u6211\u7684\u597d\u53cb")
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.page_2.setGeometry(QRect(0, 0, 274, 210))
        self.verticalLayout_5 = QVBoxLayout(self.page_2)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.listWidget_3 = QListWidget(self.page_2)
        self.listWidget_3.setObjectName(u"listWidget_3")

        self.verticalLayout_5.addWidget(self.listWidget_3)

        self.toolBox.addItem(self.page_2, u"")
        self.add_friend_butt = QPushButton(self.friend_list)
        self.add_friend_butt.setObjectName(u"add_friend_butt")
        self.add_friend_butt.setGeometry(QRect(230, 10, 111, 31))
        self.add_friend_butt.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")
        self.widget = QWidget(self.friend_list)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(40, 10, 151, 61))
        self.get_new_friend_num = QLabel(self.widget)
        self.get_new_friend_num.setObjectName(u"get_new_friend_num")
        self.get_new_friend_num.setGeometry(QRect(0, 0, 21, 17))
        self.get_new_friend_num.setStyleSheet(u"QLabel#get_new_friend_num{\n"
"	color: white;\n"
"	background-color: transparent;\n"
"	font: 10pt \"Airal\";\n"
"}")
        self.get_new_friend = QPushButton(self.widget)
        self.get_new_friend.setObjectName(u"get_new_friend")
        self.get_new_friend.setGeometry(QRect(20, 0, 121, 31))
        sizePolicy6.setHeightForWidth(self.get_new_friend.sizePolicy().hasHeightForWidth())
        self.get_new_friend.setSizePolicy(sizePolicy6)
        self.get_new_friend.setStyleSheet(u"QPushButton {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.63, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1), /* \u4e2d\u5fc3\u4e3a\u6d45\u7eff\u8272 */\n"
"                                 stop: 1 rgba(255, 255, 255, 0)); /* \u9010\u6e10\u53d8\u900f\u660e */\n"
"    border: none; /* \u65e0\u8fb9\u6846 */\n"
"    border-radius: 10px; /* \u5706\u89d2 */\n"
"    color: black; /* \u6587\u5b57\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:hover {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(144, 238, 144, 1),\n"
"                                 stop: 1 rgba(204, 255, 204, 0.8)); /* \u9f20\u6807\u60ac\u505c\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"\n"
"QPushButton:pressed {\n"
"    background: qradialgradient(cx: 0.5, cy: 0.5, radius: 0.8, fx: 0.5, fy: 0.5,\n"
"                                 stop: 0 rgba(124, 218, 124, 1),\n"
"                                 st"
                        "op: 1 rgba(184, 255, 184, 0.9)); /* \u6309\u4e0b\u65f6\u7684\u80cc\u666f\u989c\u8272 */\n"
"}\n"
"")
        self.new_friend = QWidget(self.widget)
        self.new_friend.setObjectName(u"new_friend")
        self.new_friend.setGeometry(QRect(20, 0, 10, 10))
        self.new_friend.setStyleSheet(u"QWidget#new_friend{\n"
"	border-radius: 5px;\n"
"	background-color: rgb(255, 0, 0);\n"
"}")
        self.tabWidget.addTab(self.friend_list, "")

        self.horizontalLayout_3.addWidget(self.tabWidget)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(chatroom)

        self.tabWidget_2.setCurrentIndex(0)
        self.tabWidget.setCurrentIndex(1)
        self.toolBox.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(chatroom)
    # setupUi

    def retranslateUi(self, chatroom):
        chatroom.setWindowTitle(QCoreApplication.translate("chatroom", u"Form", None))
        self.mini_butt.setText(QCoreApplication.translate("chatroom", u"\u2796", None))
        self.close_butt.setText(QCoreApplication.translate("chatroom", u"\u2716", None))
        self.avatar_show.setText(QCoreApplication.translate("chatroom", u"<html><head/><body><p><br/></p></body></html>", None))
        self.avatar_butt.setText(QCoreApplication.translate("chatroom", u"\u4e0a\u4f20\u5934\u50cf", None))
        self.group_manage_butt.setText(QCoreApplication.translate("chatroom", u"\u7fa4\u7ec4\u7ba1\u7406", None))
        self.start_record.setText("")
        self.wisper_butt.setText(QCoreApplication.translate("chatroom", u"\u8f6c\u6587\u5b57", None))
        self.video_butt.setText(QCoreApplication.translate("chatroom", u"\u89c6\u9891\u901a\u8bdd", None))
        self.send_file_butt.setText(QCoreApplication.translate("chatroom", u"\u53d1\u9001\u6587\u4ef6", None))
        self.send_butt.setText(QCoreApplication.translate("chatroom", u"\u53d1\u9001\u6d88\u606f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.text), QCoreApplication.translate("chatroom", u"\u53d1\u9001\u6d88\u606f", None))
        self.tabWidget_2.setTabText(self.tabWidget_2.indexOf(self.tab_2), QCoreApplication.translate("chatroom", u"\u8868\u60c5", None))
        self.new_group_butt.setText(QCoreApplication.translate("chatroom", u"\u521b\u5efa\u7fa4\u804a", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.chat_list), QCoreApplication.translate("chatroom", u"\u6d88\u606f\u5217\u8868", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page), QCoreApplication.translate("chatroom", u"\u6211\u7684\u597d\u53cb", None))
        self.toolBox.setItemText(self.toolBox.indexOf(self.page_2), "")
        self.add_friend_butt.setText(QCoreApplication.translate("chatroom", u"\u6dfb\u52a0\u597d\u53cb", None))
        self.get_new_friend_num.setText("")
        self.get_new_friend.setText(QCoreApplication.translate("chatroom", u"\u65b0\u597d\u53cb", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.friend_list), QCoreApplication.translate("chatroom", u"\u597d\u53cb\u5217\u8868", None))
    # retranslateUi

