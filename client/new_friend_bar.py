from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Signal, Qt, QRect
from ui.new_friend_bar_ui import Ui_new_friend_bar
from lib.public import shared_module


class New_friend_bar(QWidget):

    #itemClicked = Signal(int)  # 自定义信号，用于发出项被点击的信号

    def __init__(self, opp_id,name, parent=None):
        super().__init__(parent)

        self.ui = Ui_new_friend_bar()
        self.ui.setupUi(self)


        self.ui.close_butt.clicked.connect(self.reject)
        self.ui.config_butt.clicked.connect(self.config)

        # 设置实例变量
        self.name = name
        self.opp_id=opp_id

        # 初始化更新姓名
        self.ui.name.setText(name)


    def reject(self):
        #拒绝这个人并且关掉这个bar
        print("拒绝")
        shared_module.new_friends.del_message(self.opp_id)
        shared_module.client.ans_addfriend("no",self.opp_id)
        pass
    def config(self):
        #同意这个人并关闭这个bar
        print("同意")
        shared_module.new_friends.del_message(self.opp_id)
        shared_module.client.ans_addfriend("yes",self.opp_id)

        #TODO: #把对方放到defult
        #加載新聊天窗口
        pass
