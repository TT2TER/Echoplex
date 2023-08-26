from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.chatroom_ui import Ui_chatroom
from chating_item import Chating_item
from chat_bubble import Message_bubble
import os
class Main_win(QWidget):

    def __init__(self):
        super().__init__()
        self.ui= Ui_chatroom()
        self.ui.setupUi(self)
        

        self.ui.send_butt.clicked.connect(self.send)
        self.ui.send_butt.clicked.connect(self.add_list)
    
    def send(self):
        # 获取发送框中的文本
        message = self.ui.text_in.toPlainText()

        # 在这里添加发送的功能
        #TODO:
        
        if message:
            # 将文本添加到 view_box 中
            item = QListWidgetItem(message)
            self.ui.view_box.addItem(item)

            # 清空发送框
            self.ui.text_in.clear()

    def chating_item_clicked(self,value):
        #这是跳转函数，点击聊天列表跳转到对应的聊天，具体实现如下：
        #收到点击的value（也即用户id)，
        #获取对应用户的历史聊天记录（从本地）
        #循环加载add_message
        print("Item clicked with value:", value)

        self.img_path = "lib/login_back.png"
        self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
        self.add_message(value,self.image_path,"today,test","测试消非第三方和角色的看法和集散地和佛发动机斯科飞机的思考和发达省份集散地和附近的开始发掘速度快恢复健康锁定和佛教思考的合法的角色刻画佛教快速的恢复健康的书法家符号计算的看法和的角色可恢复健康锁定和法第四尽快恢复健康和三等奖第三开发环境思考的反对和赛季开发和三等奖开发和第三空间划分教思考东方航空锁定和附近的时可恢复思考息1")
        #这里写循环



    def add_list(self):
        self.img_path = "lib/login_back.png"
        self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
        new_chat_bar=Chating_item(self.image_path,"mayu","message")
        list_item=QListWidgetItem(self.ui.chat_list_view)
        list_item.setSizeHint(new_chat_bar.sizeHint())
        self.ui.chat_list_view.setItemWidget(list_item,new_chat_bar)
        new_chat_bar.itemClicked.connect(self.chating_item_clicked)
    
    def add_message(self,who,avatar_path, time:str="", msg:str=""):
        #who是用户id，avatar_path,time为收到该条消息的时间，msg为消息内容

        show_message=Message_bubble(who,self.image_path,time,msg)
        message_item=QListWidgetItem(self.ui.view_box)
        message_item.setSizeHint(show_message.sizeHint())
        self.ui.view_box.setItemWidget(message_item,show_message)


if __name__ == "__main__":
    app = QApplication([])
    login = Main_win()
    login.show()
    app.exec_()