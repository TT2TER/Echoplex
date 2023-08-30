from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QListWidgetItem, QFileDialog
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.chatroom_ui import Ui_chatroom
from chating_item import Chating_item
from chat_bubble import Message_bubble
from video_request_dialog import Video_request_dialog
from datetime import datetime
import time
import os,sys
import json
from record2text import record2text
class Main_win(QWidget):

    def __init__(self):
        super().__init__()
        self.ui= Ui_chatroom()
        self.ui.setupUi(self)
        
#以下是正式的的信號槽和函數
        self.ui.send_butt.clicked.connect(self.send)
        self.ui.add_friend_butt.clicked.connect(self.add_friend)
        self.ui.get_new_friend.clicked.connect(self.check_add_friend)
        self.ui.send_file_butt.clicked.connect(self.show_file_dialog)
        self.ui.group_manage_butt.clicked.connect(self.manage_group)
        self.ui.new_group_butt.clicked.connect(self.add_new_group)
        self.ui.video_butt.clicked.connect(self.send_an_vedio_request)
        self.ui.wisper_butt.clicked.connect(self.wisper)
        #維護一個當前顯示的對象id
        self.cur_id =None

        # 用于动态维护的好友列表和消息列表
        self.friend_item = []
        self.chat_item = []

        #用於指向當前加載的消息框
        self.cur_bubble=None

#以上是最終實現的信號槽
#以下是測試用的信號槽和函數
        self.ui.add_new_chat.clicked.connect(self.add_test)
        self.img_path = "lib/login_back.png"
        self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
    def add_test(self):
            #以下測試
            self.ui.chat_list_view.clear()
        
#以上是測試用的函數和槽


#以下是添加好友相關功能
    def add_friend(self):
        shared_module.add_friend.show()

        #测试成功
        

    def check_add_friend(self):
        
        shared_module.new_friends.show()
        shared_module.new_friends.add_message()
        #opp_id。
        #shared_module.client.ans_addfriend(yes_or_no, opp_id,defult)
        pass


    def rcv_addfriend(self, back_data, content):
        # 收到对方的添加好友请求
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
            _time = content["time"]
            ans = content["ans"]
            name = content["name"]
            print( [sender, time, ans,name])

            if ans == "yes":
                #TODO：添加到好友列表 defult
                shared_module.client.friend_list.append((sender, name, 'default'))
                #TODO：添加到聊天列表
                if sender>shared_module.client.user_id:
                    chat_id=shared_module.client.user_id*100000+sender
                else :
                    chat_id=shared_module.client.user_id+sender*100000
                sender_id=sender
                #TODO: 这里可能有bug
                #shared_module.main_page.add_one_list(chat_id, sender_id,name,"", time , name+"已经成为了您的新好友")
                pass
                print("收到",name,"的消息，对方同意，已经添加到聊天列表中了")
            else : 
                print("收到",name,"回复，对方拒绝，舔狗舔到最后一无所有")
                pass
        elif back_data == "0001":
            print("查无此人")
            QMessageBox.information(self,"查无此人","请检查id是否正确")

#以上是添加好友相關函數杀人

#以下是发送文件功能
    def show_file_dialog(self):
        """这个函数负责让用户选择要发送的文件并将文件地址提取出来"""
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        full_path, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)', options=options)

        if full_path:
            # 这个里面有full_path, base_name是文件名称的“example.txt",file_extension是文件类型字符串
            print('Selected File:', full_path)
            base_name = os.path.basename(full_path)
            file_extension = os.path.splitext(base_name)[1]
            display_text = f'<a href="file:{full_path}">文件名：{base_name}</a><br>文件类型：{file_extension}'
            shared_module.client.send_file_request(self.cur_id,full_path)
        else:
            QMessageBox.warning(self,"发送失败","文件路径获取失败")

    def progress_bar_show(self):
        shared_module.progress_bar.show()

    def update_label(self, text):
        self.text_browser.setHtml(text)

    def open_file(self, link):
        if sys.platform.startswith('win'):
            os.startfile(link)  # 适用于Windows系统
        elif sys.platform.startswith('darwin'):
            os.system(f'open "{link}"')  # 适用于macOS系统
        elif sys.platform.startswith('linux'):
            os.system(f'xdg-open "{link}"')  # 适用于Linux系统


#以上是发送文件功能

#以下是私聊收發消息相關函數（群聊也许能复用
    def send(self):
        # 获取发送框中的文本
        message = self.ui.text_in.toPlainText()
        #维护一个当下的聊天对象的id
        # 在这里添加发送的功能
        #请在这里给我发消息的对象id
        chat_id=self.cur_id #私聊是10位，群聊是五位，2開頭
        
        if chat_id>1000000:
            shared_module.client.friend_chat(message, chat_id)
        else :
            shared_module.client.group_chat(message, chat_id)

        self.ui.text_in.clear()
        
    def print_online_message(self,content):
        """把在線的消息打印出來,如果不是當前窗口，存在文件里。
        要找name,avatar_path
        """
        print("进入了打印在线消息\n")
        shared_module.client.append_msg(content)
        #在這裡面找到sender_name和sender_avatar_path
        chat_id = content["chat_id"]

        flag = 0
        for i in self.chat_item:
            if i.chat_id == chat_id:
                self.renew_list(content)
                flag=1
                break
        
        if flag == 0 :
            self.add_one_list(content)
        if self.cur_id == chat_id:
            print(chat_id)
            self.add_one_message(content)
            pass
        else :
            print("不是当前窗口，等待用户点击后加载")
            pass

#以上是私聊收發消息相關函數（群聊也许能复用

#以下是聊天列表的功能函數
    def init_chat_list(self):
        """這個函數用來從登陸界面打開時初始化聊天列表"""

        for chat_id, sender_id, _time, msg in shared_module.client.msg_list :

            content = {
                'chat_id' : chat_id,
                'sender': sender_id,
                'time': _time,
                'msg': msg,
                'filepath': None,
                'filesize': None,
                'msg_type': 'friend_chat',
                'is_avatar': False
            }
            flag = 0
            for i in self.chat_item:
                if i.chat_id == chat_id:
                    flag = 1
                    break

            if flag == 0:
                self.add_one_list(content)
        pass

    def add_one_list(self,content):
        chat_id=content["chat_id"]
        print("实例化了", chat_id)
        """實例化一個消息列表框"""
        new_chat_bar=Chating_item(content)
        self.chat_item.insert(0,new_chat_bar)
        #將消息列表框放進item里
        list_item=QListWidgetItem()
        list_item.setSizeHint(new_chat_bar.sizeHint())
        self.ui.chat_list_view.insertItem(0,list_item)
        self.ui.chat_list_view.setItemWidget(list_item,new_chat_bar)
        #如果框體被點擊，連接到的函數
        new_chat_bar.itemClicked.connect(self.chating_item_clicked)

    def del_one_list(self,chat_id):
        """在動態List里找到該item的位置"""
        print("进入了del_one_list")
        ind = 0
        for i in self.chat_item:
            if i.chat_id == chat_id:
                break
            ind += 1
        #刪掉ui里的東西
        print(chat_id)
        print(ind)
        self.chat_item.remove(i)
        try:
            item_to_remove=self.ui.chat_list_view.takeItem(ind)
            item_to_remove=None
        except:
            print("删除chat_list_item失败")
        pass

    def renew_list(self,content):
        """更新消息的時候要用"""
        chat_id=content["chat_id"]
        self.del_one_list(chat_id)
        self.add_one_list(content)
#以上是聊天列表的功能函數
    

#以下是聊天窗口的功能函數
    def chating_item_clicked(self,chat_id):
        """
        这是跳转函数，点击聊天列表跳转到对应的聊天，具体实现如下：

        #收到点击的value（也即用户id)，
        #获取对应用户的历史聊天记录（从本地）
        #循环加载add_message
        """
        print("Item clicked with value:", chat_id)

        #如果點擊到的列表本身就是窗口里的，pass
        if self.cur_id==chat_id:
            pass
        #如果列表本身是新的，清空列表模擬重新加載
        else :  
            self.ui.view_box.clear()
            self.cur_id=chat_id

            # TODO 读消息

            # filepath = 'files/chats/' + str(chat_id)
            # # 如果目录不存在，就创建一个目录
            # msg_list = []
            # if not os.path.exists(filepath):
            #     # 如果文件不存在，创建空文件
            #     # 往空文件中写入json格式的"[]"
            #     with open(filepath, 'w') as f:
            #         msg_list = []
            # else:
            #     with open(filepath, 'r') as f:
            #         msg_list = json.loads(f)

            filepath = 'files/chats/' + str(chat_id) + '.json'

            # 如果目录不存在，就创建一个目录
            if not os.path.exists('files/chats/'):
                os.makedirs('files/chats/')

            msg_list = []
            if not os.path.exists(filepath):
                # 如果文件不存在，创建空文件
                # 往空文件中写入json格式的"[]"
                with open(filepath, 'w') as f:
                    json.dump(msg_list, f)
            else:
                with open(filepath, 'r') as f:
                    msg_list = json.load(f)

            #TODO:给我content
            if len(msg_list) == 0:
                print("消息记录为空")
            else:
                print("将打印与此用户的历史消息")
                msg_list.reverse()
                for content in msg_list:
                    #chat_id是整数，sender_id是整数，chat_time是timestamp格式，msg是字符串
                    self.add_one_message(content)
                    print(chat_id,"的消息列表打印完毕")

    def add_one_message(self,content):
        """
        調用這個函數來打印消息

        :sender_id根據是不是自己可以將消息顯示成兩種不同的氣泡

        :avatar_path,time为收到该条消息的时间，msg为消息内容
        """
        print("向屏幕中打印")
        try:
            self.cur_bubble=Message_bubble(content)
            message_item=QListWidgetItem(self.ui.view_box)
            message_item.setSizeHint(self.cur_bubble.sizeHint())
            self.ui.view_box.setItemWidget(message_item,self.cur_bubble)
            # if self.cur_bubble.is_file:
            #     for i in range(101):
            #         self.cur_bubble.update_progress(i)
            #         time.sleep(0.1)
        except Exception as e:
            print("新建消息報錯", e)

#以上是聊天窗口的功能函數

#這個是用來更新percentage的函數，有小的時間順序bug，但已經奇技淫巧解決了
    def update_percentage(self,percentage):
        if self.cur_bubble.is_file:
            self.cur_bubble.update_progress(percentage)

#以下是群聊的跳转逻辑
    def add_new_group(self):
        """創建群聊
        
        这个函数是点击了创建新群聊后调用的函数
        会调起创建新群组弹窗
        """
        
        print("即将打开新建群聊窗口……")
        shared_module.new_group.show()

    def manage_group(self):
        """管理群聊
        
        這個函數是點擊群聊管理後調用的函數"""
        shared_module.manage_group.show()

    def recv_delete_group(self, back_data, content):
        # 收到对方的添加好友请求
        # 返回发送者的用户ID和时间戳
        if back_data == '0002':
            for i in shared_module.client.group_list:
                if i[0] == content['group_id']:
                    shared_module.client.group_list.remove(i)
                    break
            if content['sender_id'] == shared_module.client.user_id:
                QMessageBox.information(self,"解散成功","群聊已解散")
            self.del_one_list(content['group_id'])
            if not self.chat_item.empty():
                self.chating_item_clicked(self.chat_item[0].chat_id)
        elif back_data == '0003':
            QMessageBox.information(self,"解散失败","您不是管理员，无法解散群聊")
#以上是群聊的跳转逻辑

#以下是视频聊天功能
    def send_an_vedio_request(self):
        if self.cur_id!=None:
            #在这里写你的发送视频请求的代码
            #cur_id是当前的十位chat_id
            print(self.cur_id)

            print("发送视频申请成功")

    def receive_an_vedio_request(self,content):
        print("点击了视频聊天按钮")
        #调用这个函数的时候要传入id和ip
        id = content['user_id']
        ip = content['user_ip']
        try:
            shared_module.video_page.update_info_label(id,ip,content)
            shared_module.video_page.show()
        except Exception as e:
            print (e)
        print("窗口创建成功")
        pass


#以下是语音转文字
    def wisper(self):
        #这里调用wisper
        #给我返回一个result
        result = record2text()
        self.ui.text_in.append(result)


if __name__ == "__main__":
    app = QApplication([])
    login = Main_win()
    login.show()
    app.exec_()