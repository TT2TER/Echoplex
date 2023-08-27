from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.chatroom_ui import Ui_chatroom
from ui.add_friend_ui import Ui_add_friend
from chating_item import Chating_item
from chat_bubble import Message_bubble
from datetime import datetime
import os
class Main_win(QWidget):

    def __init__(self):
        super().__init__()
        self.ui= Ui_chatroom()
        self.ui.setupUi(self)
        
#以下是正式的的信號槽和函數
        self.ui.send_butt.clicked.connect(self.send)
        self.ui.add_friend_butt.clicked.connect(self.add_friend)
        self.ui.get_new_friend.clicked.connect(self.check_add_friend)
        #維護一個當前顯示的對象id
        self.cur_id =None
        

#以上是最終實現的信號槽
        #以下是測試用的信號槽和函數
        self.ui.add_new_chat.clicked.connect(self.add_test)
    
    def add_test(self):
            #以下測試
            
            opp_id=self.cur_id=2
            #以上測試
            name=opp_id
            time= datetime.now()
            self.img_path = "lib/login_back.png"
            self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
            self.add_list(opp_id,str(name),self.image_path, time, "最近消息測試")
    
    def add_friend(self):
        #TODO:写成类
        add_friend_win=Ui_add_friend()
        add_friend_win.setupUi(self)
        add_friend_win.show()
        opp_id=add_friend_win.id_in.text()
        add_friend_win.add_fri_butt.connect(shared_module.client.user_addfriend(opp_id))

    def check_add_friend(self):
        #TODO:画一个列表，画一个列表里的内容
        while len(shared_module.client.add_friend_list) > 0:
            (sender, time, name) = shared_module.client.add_friend_list.pop(0)

            #TODO mayu 将name请求者姓名显示在表上
            print("消息列表打印完毕")
        #opp_id。
        shared_module.client.ans_addfriend(yes_or_no, opp_id,defult)
        pass
        
        

    def rcv_addfriend(self, back_data, content):
        # 对方接收到添加好友请求
        # 返回发送者的用户ID和时间戳
        sender = content["sender"]
        time = content["time"]
        name = content["name"]
        shared_module.client.add_friend_list.append((sender, time, name))
        print(("收到了好友申请", sender, time, name))

    def rcv_ans_addfriend(self, back_data, content):
        # 对方接收到同意或拒绝添加好友请求的回复
        # 返回发送者的用户ID、时间戳和回复内容

        # 对方收到好友请求并确定是否同意
        if back_data == "0000":
            
            sender = content["sender"]
            time = content["time"]
            ans = content["ans"]
            print( [sender, time, ans])

            if ans == "yes":
                #TODO：添加到好友列表
                #TODO：添加到聊天列表
                #TODO：zf 返回对方昵称
                pass
            else : 
                #别知道了 ，，或者是在信号由申请列表显示谁谁谁拒绝
                pass
        elif back_data == "0001":
            print("查无此人")
            QMessageBox.information(self,"查无此人","请检查id是否正确")

    def send(self):
        # 获取发送框中的文本
        message = self.ui.text_in.toPlainText()
        #维护一个当下的聊天对象的id
        # 在这里添加发送的功能
        #请在这里给我发消息的对象id
        opp_id=self.cur_id
        me_id=1
        #TODO:
        
        if message:
            # 以下是展示用的，证明客户端发消息是好的
            id=me_id
            name=id
            time= datetime.now()
            self.img_path = "lib/login_back.png"
            self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
            self.add_message(id,name,self.image_path,str(time),message)
            # 清空发送框
            self.ui.text_in.clear()

    def chating_item_clicked(self,opp_id):
        #这是跳转函数，点击聊天列表跳转到对应的聊天，具体实现如下：
        #收到点击的value（也即用户id)，
        #获取对应用户的历史聊天记录（从本地）
        #循环加载add_message
        print("Item clicked with value:", opp_id)
        if self.cur_id!=opp_id:
            pass
        if len(shared_module.client.msg_list) == 0:
            print("聊天消息列表为空")
        while len(shared_module.client.msg_list) > 0:
            (chat_id, sender_id, chat_time, chat_content) = shared_module.client.msg_list.pop(0)
            #TODO mayu 将上述元组的内容显示在表上
            #chat_id是整数，sender_id是整数，chat_time是datetime格式，chat_content是字符串


        print("消息列表打印完毕")




    def add_list(self,opp_id,name,avatar_path, time:str="" , msg:str=""):

        #實例化一個消息列表框
        new_chat_bar=Chating_item(opp_id,name,avatar_path,time,msg)
        #將消息列表框放進item里
        list_item=QListWidgetItem(self.ui.chat_list_view)
        list_item.setSizeHint(new_chat_bar.sizeHint())
        self.ui.chat_list_view.setItemWidget(list_item,new_chat_bar)

        #如果框體被點擊，連接到的函數
        new_chat_bar.itemClicked.connect(self.chating_item_clicked)
    
    def add_message(self,id,name,avatar_path, time:str="", msg:str=""):
        #id是用户id，avatar_path,time为收到该条消息的时间，msg为消息内容

        show_message=Message_bubble(id,name,avatar_path,time,msg)
        message_item=QListWidgetItem(self.ui.view_box)
        message_item.setSizeHint(show_message.sizeHint())
        self.ui.view_box.setItemWidget(message_item,show_message)


if __name__ == "__main__":
    app = QApplication([])
    login = Main_win()
    login.show()
    app.exec_()