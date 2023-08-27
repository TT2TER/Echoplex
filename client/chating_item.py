from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Signal, Qt, QRect
from ui.chating_item_ui import Ui_chating_item


class Chating_item(QWidget):

    itemClicked = Signal(int)  # 自定义信号，用于发出项被点击的信号

    def __init__(self, opp_id, name, avatar_path, time, recent_msg, parent=None):
        super().__init__(parent)

        self.ui = Ui_chating_item()
        self.ui.setupUi(self)

        # 设置实例变量
        self.name = name
        self.opp_id=opp_id
        self.time=time

        # 初始化更新姓名
        self.ui.name.setText(name)

        # 初始化头像
        self.avatar_label = QLabel(self.ui.avatar)
        self.avatar_label.setGeometry(QRect(0, 0, 48, 48))
        self.avatar_label.setStyleSheet(
            u"background-color: transparent; border-radius: 6px;")
        image = QPixmap(avatar_path)  # 用实际的图像路径替换
        self.avatar_label.setPixmap(image)
        self.avatar_label.setScaledContents(True)  # 自适应图像大小
        self.ui.resent_message.setText(recent_msg)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Widget clicked")
            # 在这里可以执行选中效果的操作，例如修改颜色、样式等
            #TODO: 最好選中一次後就不能再選中了，點擊到別人再不選中
            self.itemClicked.emit(self.opp_id)
