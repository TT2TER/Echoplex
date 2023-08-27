import socket
import json
import threading
from datetime import datetime
from lib.public import shared_module
from file_thread import FileSendThread, FileReceiveThread, send_file_handler, receive_file_handler
import os,time


class Client:
    def __init__(self, ip, port):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = (ip, int(port))
            self.client_socket.connect(self.server_address)
            self.user_id = None
            self.user_name = None
            self.msg_list = None
            self.add_friend_list = []
        except Exception as e:
            print("不应该在这里报错，这辈子都不能看到这个消息。这个消息在class client inits")

    def back_massage_handler(self, received_data):
        # 处理发射回来的信号
        try:
            message_handlers = {
                'user_register': shared_module.reg_page.recv_register,
                'user_login': shared_module.login_page.recv_login,
                'user_send_file': self.send_file,
                'user_receive_file': self.receive_file,
                'friend_chat': self.receive_friend_message,
                'group_chat': self.receive_group_message,
                'user_addfriend': shared_module.main_page.rcv_addfriend,#self.rcv_addfriend,
                'ans_addfriend': shared_module.main_page.rcv_ans_addfriend, #self.rcv_ans_addfriend
                'init_msg_list': self.init_msg_list
            }
            handler = message_handlers.get(received_data['type'], None)
            back_data = received_data.get('back_data', None)
            content = received_data.get('content', None)
            if handler:
                print("handler为" + getattr(handler, "__name__", "unknown_function"))
                succ = handler(back_data, content)
                print("处理结果：" + str(succ) + "，一般不设返回值所以为none")
            else:
                print("收到处理不了的类型的消息")
        except:
            print("处理消息时候寄了，在client_function这back_message_handler里头")
        finally:
            print("处理完一个服务器来的请求了")

    def user_login(self, user_id, user_pwd):
        # 向服务器发送用户登录请求
        # 包括用户ID和密码
        # 返回状态码以指示登录尝试的结果

        data = {
            'type': 'user_login',
            'content': {
                'user_id': user_id,
                'user_pwd': user_pwd
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    # 向服务端发送注册请求
    def user_register(self, user_name, user_image, user_pwd, user_email):
        # 向服务器发送用户注册请求
        # 包括用户信息如姓名、头像、密码、邮箱
        # 返回状态码以指示注册尝试的结果
        data = {
            'type': 'user_register',
            'content': {
                'user_name': user_name,
                'user_pwd': user_pwd,
                'user_email': user_email,
                'user_image': user_image
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    # 点击头像，显示好友信息
    def friendinfo(self):
        # 向服务器请求好友信息
        # 包括要请求信息的好友的用户ID
        # 根据服务器的响应返回好友信息或错误码
        data = {
            'type': 'friendinfo',
            'content': {
                'user_id': self.user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def friend_chat(self, msg, receiver):
        # 发送聊天消息给另一个用户
        # 包括消息内容、发送者的用户ID、接收者的用户ID和时间戳
        # 发送消息的时间
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "user_chat",
            "content": {
                "msg_type": "friend_chat",
                "msg": msg,
                "sender": self.user_id,
                "receiver": receiver,
                "time": timestamp,
                "filesize": None,
                "filepath": None
            }
        }
        # 向服务端发送消息
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def group_chat(self, msg, group_id):
        # 发送聊天消息到一个群组
        # 包括消息内容、发送者的用户ID、群组ID和时间戳
        # 发送消息的时间
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "user_chat",
            "content": {
                "msg_type": "group_chat",
                "msg": msg,
                "sender": self.user_id,
                "group_id": group_id,
                "time": timestamp,
                "filepath": None,
                "filesize":None
            }
        }
        # 向服务端发送消息
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def private_group_chat(self, msg, group_id, receiver):
        # 发送私密群组聊天消息
        # 包括消息内容、发送者的用户ID、群组ID、接收者的用户ID和时间戳

        # 发送消息的时间
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "user_chat",
            "content": {
                "msg_type": "private_group_chat",
                "msg": msg,
                "sender": self.user_id,
                "group_id": group_id,
                "receiver": receiver,
                "time": timestamp
            }
        }
        # 向服务端发送消息
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    # 用于登录后主动向服务器拉取离线信息
    def pull_message(self):
        # 请求从服务器拉取消息
        # 包括发送者的用户ID
        data = {
            "type": "pull_message",
            "content": {
                "sender": self.user_id,
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def create_group(self, group_member, group_name,image_path):
        # 创建一个群组
        # 包括群主的用户ID、成员列表和群组名称
        data = {
            "type": "create_group",
            "content": {
                "group_manager": self.user_id,
                "group_member": group_member,
                "group_name": group_name,
                "group_create_time":datetime.now(),
                "group_image":image_path
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def user_addfriend(self, target_id):
        # 发送添加好友请求
        # 包括发送者的用户ID、接收者的用户ID和时间戳
        # 发送请求添加好友时间
        #print(target_id)
        now = datetime.now()
        _time = datetime.timestamp(now)
        data = {
            "type": "user_addfriend",
            "content": {
                "sender": self.user_id,
                "receiver": target_id,
                "time": _time,
                "name": self.user_name
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    # def rcv_addfriend(self, back_data, content):
    #     # 对方接收到添加好友请求
    #     # 返回发送者的用户ID和时间戳

    #     sender = content["sender"]
    #     time = content["time"]
    #     print(("收到了好友申请", sender, time))

    def ans_addfriend(self, ans, target_id):
        # 发送同意或拒绝添加好友请求
        # 包括回复内容、发送者的用户ID、接收者的用户ID和时间戳和分组partition

        # 发送同意或拒绝请求
        # 搜索自己的昵称
      
        now = datetime.now()
        time = datetime.timestamp(now)
        data = {
            "type": "ans_addfriend",
            "content": {
                "sender": self.user_id,
                "receiver": target_id,
                "time": time,
                "ans": ans,
                "name": self.user_name
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    # def rcv_ans_addfriend(self, back_data, content):
    #     # 对方接收到同意或拒绝添加好友请求的回复
    #     # 返回发送者的用户ID、时间戳和回复内容

    #     # 对方收到好友请求并确定是否同意
    #     if back_data == "0000":

    #         sender = content["sender"]
    #         time = content["time"]
    #         ans = content["ans"]
    #         print( [sender, time, ans])
    #     elif back_data == "0001":
    #         print("查无此人")



    def pullfriendlist(self):
        data = {
            "type": "pullfriendlist",
            "content": {
                "sender": self.user_id,
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def send_file_request(self, chat_id, file_path):
        # 向服务器发送文件发送请求
        # 包括接收者的ID地址、和本机文件路径
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        file_size = os.path.getsize(file_path)
        data = {
            'type': 'user_send_file',
            'content': {
                "msg_type": "friend_chat",
                "sender": self.user_id,
                "chat_id": chat_id,
                "msg": None,
                "filepath": file_path,
                "time": timestamp,
                "filesize": file_size
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        print("文件发送请求成功发送")

    def change_avatar_request(self, file_path):
        # 向服务器发送文件发送请求
        # 包括本机文件路径
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        file_size = os.path.getsize(file_path)
        data = {
            # 要复用user_send_file
            'type': 'user_send_file',
            'content': {
                "msg_type": "broadcast",
                "sender": self.user_id,
                "chat_id": None,
                "msg": None,
                "filepath": file_path,
                "time": timestamp,
                "filesize": file_size
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        print("更换头像请求成功发送")

    def receive_file_request(self, chat_id, file_path):
        # 向服务器发送文件接受请求
        # 包括接收者的ID地址、和服务端文件路径
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            'type': 'user_send_file',
            'content': {
                "msg_type": "friend_chat",
                "sender": self.user_id,
                "chat_id": chat_id,
                "msg": None,
                "filepath": file_path,
                "time": timestamp,
                "filesize": None
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        print("接收文件请求成功发送")
        # 在从服务器收到允许发文件的答复后，开始发文件线程

    def send_file(self, back_data, content):
        try:
            if back_data == "0000":
                print("服务器允许发送文件，准备发送力")

                shared_module.file_thread = FileSendThread(content["sender_ip"], content["port"], content["filepath"], content["filesize"])
                shared_module.file_thread.start()
                shared_module.file_thread.notify.connect(send_file_handler)
                # file_thread.wait()
                print("send_file函数结束了")
            else:
                print("服务器不允许发送文件，寄了，记载client_function,send_file里头")
        except Exception as e:
            print("send_file寄了，寄在client_function,send_file里头：" + str(e))

    # 在从服务器收到允许接收文件的答复后，开始接收文件线程
    def receive_file(self, back_data, content):
        try:
            if back_data == "0000":
                print("服务器允许接收文件，准备接收力")
                shared_module.file_thread = FileReceiveThread(content)

                shared_module.file_thread.start()
                shared_module.file_thread.notify.connect(receive_file_handler)
            else:
                print("服务器不允许接收文件，寄了，记载client_function,receive_file里头")
        except Exception as e:
            print("receive_file寄了，寄在client_function,receive_file里头：" + str(e))

    def receive_friend_message(self, back_data, content):
        sender = content["sender"]
        msg = content["msg"]
        time = content["time"]
        filepath = content["filepath"]
        if sender == self.user_id:
            if not filepath:
                # 自己的消息发送成功
                # 在聊天窗口打印自己的消息
                # 在文件中写入自己的消息
                print("消息发送成功消息内容是" + msg)
            if not msg:
                # 自己的文件发送成功
                # 在聊天窗口显示人间发送成功
                print("文件发送成功")
        else:
            try:
                if not filepath:
                    # 收到的是文本消息
                    print("收到的是来自" + str(content['sender']) + "文本消息：" + content["msg"])
                    # 写入一个文件

                    # 进行窗口交互

                elif not msg:
                    print("收到的是来自" + str(content['sender']) + "文件")

                    # 进行窗口交互
                    # 将文件 消息 显示在聊天中
            except Exception as e:
                print("receive_friend_message寄了，寄在client_function,receive_friend_message里头：" + str(e))

    def receive_group_message(self, back_data, content):
        sender = content["sender"]
        msg = content["msg"]
        time = content["time"]
        group_id = content["group_id"]
        filepath = content["filepath"]
        try:
            if not filepath:
                # 收到的是文本消息
                print("收到的是来自" + str(content['sender']) + "群组文本消息：" + content["msg"])
                # 写入一个文件

                # 进行窗口交互

            elif not filepath:
                print("收到的是来自" + str(content['sender']) + "群组文件")

                # 进行窗口交互
                # 将文件 消息 显示在聊天中
        except Exception as e:
            print("receive_group_message寄了，寄在client_function,receive_group_message里头：" + str(e))

    def rcv_friendlist(self,back_data,content):
        
        friend_list_info = content["friend_list_info"]
        if back_data == "0012":
            # 好友列表获取成功
            return friend_list_info
            #friend_list_info是（id，name，partition）的list     
            print("这里需要my根据partion，分组显示好友")

        elif back_data == "0013":
            # 好友列表获取失败
            return None
        else:
            # 未知错误
            return None        

    def del_friend(self,friend_id):
        try:
            data = {
                "type": "del_friend",
                "content": {
                    "sender": self.user_id,
                    "friend_id": friend_id
                }
            }
            json_data = json.dumps(data).encode('utf-8')
            self.client_socket.sendall(json_data)
        except Exception as e:
            print("del_friend寄了，寄在client_function,del_friend里头：" + str(e))


    def delete_group(self,group_id):
        data = {
            "type": "delete_group",
            "content": {
                "group_id": group_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)


    def add_new_member(self,group_id,member_id):
        data={
            "type":"add_new_member",
            "content":{
                "group_id":group_id,
                "member_id":member_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def pull_msg_list(self):
        data={
            "type":"init_msg_list",
            "content":{
                "user_id":self.user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def init_msg_list(self, back_data, content):
        if back_data == "0000":
            print("申请消息列表成功")
            self.msg_list = content["list"]
        else:
            print("申请消息列表失败")
