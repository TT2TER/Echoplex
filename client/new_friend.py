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
        self.item = []

    def back(self):
        self.close()

    def add_message(self):
        #print(shared_module.client.add_friend_list)
        #在这里读取以下信息
        for sender, time, name in shared_module.client.add_friend_list :
            print("in_for")
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

        #把好友请求队列里的也山了
        for j in shared_module.client.add_friend_list:
            if j[0] == opp_id:
                break
        
        shared_module.client.add_friend_list.remove(j)