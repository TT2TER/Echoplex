from PySide2.QtWidgets import QWidget, QListWidgetItem
from ui.new_friends_ui import Ui_new_friends
from lib.public import shared_module
from new_friend_bar import New_friend_bar

class New_friends(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_new_friends()
        self.ui.setupUi(self)

        self.ui.back_butt.clicked.connect(self.add_message)

    def back(self):
        self.close()

    def add_message(self):

        #在这里读取以下信息
        opp_id=123
        name="test name"
        
        #写循环实现把所有请求写进去

        new_friend_bar=New_friend_bar(opp_id,name)
        #將消息列表框放進item里
        list_item=QListWidgetItem(self.ui.new_friends_box)
        list_item.setSizeHint(new_friend_bar.sizeHint())
        self.ui.new_friends_box.setItemWidget(list_item,new_friend_bar)

        

        pass