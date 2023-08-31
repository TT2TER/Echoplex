from PySide2.QtWidgets import QWidget, QMessageBox
from ui.add_friend_ui import Ui_add_friend
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import Qt
from dependencies.public import shared_module

class Add_friend(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_add_friend()
        self.ui.setupUi(self)

        self.ui.add_fri_butt.clicked.connect(self.add_friend)
        self.ui.close_butt.clicked.connect(self.close_win)
        self.ui.mini_butt.clicked.connect(self.minimize_win)

    def add_friend(self):
        opp_id=self.ui.id_in.text()
        opp_id=int(opp_id)
        ret=shared_module.client.user_addfriend(opp_id)
        if ret ==0:
            self.close()
        else :
            QMessageBox.warning(self,"请求发送失败","请稍后再试")
        #以下函数是移动窗口用的
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False
    def close_win(self):
        self.close()
    def minimize_win(self):
        #这个是最小化窗口函数
        self.showMinimized()