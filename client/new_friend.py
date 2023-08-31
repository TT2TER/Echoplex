from PySide2.QtWidgets import QWidget, QListWidgetItem
from ui.new_friends_ui import Ui_new_friends
from dependencies.public import shared_module
from new_friend_bar import New_friend_bar
from PySide2.QtCore import Qt
from PySide2.QtGui import QMouseEvent


class New_friends(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        # Set window flags to customize the window behavior
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_new_friends()
        self.ui.setupUi(self)
        
        self.ui.close_butt.clicked.connect(self.close_win)
        self.ui.mini_butt.clicked.connect(self.minimize_win)
        #self.ui.back_butt.clicked.connect(self.back)
        self.item = []

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

    #以下是关窗口函数
    def close_win(self):
        self.close()
    def minimize_win(self):
        #这个是最小化窗口函数
        self.showMinimized()

    def add_message(self):

        #在这里读取以下信息
        for sender, time, name in shared_module.client.add_friend_list :
            new_friend_bar=New_friend_bar(sender,name)
            self.item.append(new_friend_bar)
            #將消息列表框放進item里
            list_item=QListWidgetItem(self.ui.new_friends_box)
            list_item.setSizeHint(new_friend_bar.sizeHint())
            self.ui.new_friends_box.setItemWidget(list_item,new_friend_bar)
        pass

    def del_message(self,opp_id):
        ind = 0
        for i in self.item:
            if i.opp_id == opp_id:
                break
            ind += 1

        self.item.remove(i)
        item_to_remove=self.ui.new_friends_box.takeItem(ind)
        item_to_remove=None
        #把好友请求队列里的也刪了
        for j in shared_module.client.add_friend_list:
            if j[0] == opp_id:
                shared_module.client.add_friend_list.remove(j)
                break
        if len(shared_module.client.friend_list) == 0:
            shared_module.main_page.hide_friend_red()

