import socket
import json
import threading
from datetime import datetime
from dependencies.public import shared_module
from video_chat_thread import *
from file_thread import FileSendThread, FileReceiveThread, receive_file_handler
import os, time


class Client:
    def __init__(self, ip, port):
        try:
            self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = (ip, int(port))
            self.client_socket.connect(self.server_address)
            self.user_id = None
            self.user_name = None
            self.msg_list = []  # [(1000110004,10001,"test_time","第一條消息"),(1000310004,10004,"test_time","第二條消息"),(100021004,10002,"test_time","第三條消息")]  #(chat_id, sender_id, name, time, msg)
            self.add_friend_list = []
            self.friend_list = []
            self.group_list=[]
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
                'user_chat': self.receive_friend_message,
                'user_addfriend': shared_module.main_page.rcv_addfriend,  # self.rcv_addfriend,
                'ans_addfriend': shared_module.main_page.rcv_ans_addfriend,  # self.rcv_ans_addfriend
                'init_msg_list': self.init_msg_list,
                'user_friendlist': self.rcv_friendlist,
                'group_list':self.rcv_group_list,
                'create_group': self.rcv_create_group,
                'a_delete_group': self.rcv_delete_group,
                'add_new_member': self.rcv_add_new_member,
                'user_video_chat': self.rcv_video_chat,
                'ans_video_chat': self.rcv_ans_video_chat,
                'delete_group': shared_module.main_page.recv_delete_group,
            }
            handler = message_handlers.get(received_data['type'], None)
            back_data = received_data.get('back_data', None)
            content = received_data.get('content', None)
            print(handler,back_data,content)
            if handler:
                print("handler为" + getattr(handler, "__name__", "unknown_function"))
                succ = handler(back_data, content)
                print("处理结果：" + str(succ) + "，一般不设返回值所以为none")
            else:
                print("收到处理不了的类型的消息")
        except Exception as e:
            print("处理消息时候寄了，在client_function这back_message_handler里头", e)
        finally:
            print("处理完一个服务器来的请求了")

    def user_login(self, user_id, user_pwd):
        # 向服务器发送用户登录请求
        # 包括用户ID和密码
        # 返回状态码以指示登录尝试的结果
        data = {
            'type': 'user_login',
            'content': {
                'token': None,
                'user_id': user_id,
                'user_pwd': user_pwd,
                "face": False
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        print("User_login已发送", data)
        self.client_socket.sendall(json_data)

    def auto_login(self):
        # 向服务器发送用户登录请求
        # 使用token
        # 返回状态码以指示登录尝试的结果
        token_filepath = "files/token/token.txt"
        try:
            with open(token_filepath, 'r') as token_file:
                token = token_file.read().strip()
                print(f"Read token from file: {token}")
                data = {
                    'type': 'user_login',
                    'content': {
                        'token': token,
                        'user_id': None,
                        'user_pwd': None,
                        "face": False
                    }
                }
                json_data = json.dumps(data).encode('utf-8')
                print("Auto_login已发送", data)
                self.client_socket.sendall(json_data)
        except FileNotFoundError:
            print("Token file not found.")

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
            'type': 'friend_info',
            'content': {
                'user_id': self.user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def friend_chat(self, msg, chat_id):
        # 发送聊天消息给另一个用户
        # 包括消息内容、发送者的用户ID、接收者的用户ID和时间戳
        # 发送消息的时间
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "user_chat",
            "content": {
                "is_avatar": False,
                "msg": msg,
                "sender": self.user_id,
                "chat_id": chat_id,
                "time": timestamp,
                #                "time":now,
                "filesize": None,
                "filepath": None
            }
        }
        # 向服务端发送消息
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def group_chat(self, msg, chat_id):
        # 发送聊天消息到一个群组
        # 包括消息内容、发送者的用户ID、群组ID和时间戳
        # 发送消息的时间
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "user_chat",
            "content": {
                "is_avatar": False,
                "msg": msg,
                "sender": self.user_id,
                "chat_id": chat_id,
                "time": timestamp,
                # "time":now,
                "filepath": None,
                "filesize": None
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
                "time": timestamp,
                #                "time": now,
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

    def create_group(self, group_member, group_name, image_path):
        # 创建一个群组
        # 包括群主的用户ID、成员列表和群组名称
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "create_group",
            "content": {
                "group_manager": self.user_id,
                "group_member": group_member,
                "group_name": group_name,
                "group_create_time": timestamp,
                "group_image": image_path
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def user_addfriend(self, target_id):
        # 发送添加好友请求
        # 包括发送者的用户ID、接收者的用户ID和时间戳
        # 发送请求添加好友时间
        # print(target_id)
        now = datetime.now()
        _time = datetime.timestamp(now)
        data = {
            "type": "user_addfriend",
            "content": {
                "sender": self.user_id,
                "receiver": target_id,
                "time": _time,
                # "time":now,
                "name": self.user_name
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        return 0

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
                # "time":now,
                "ans": ans,
                "name": self.user_name
            }
        }

        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        print("all_send")

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

    def pull_friendlist(self):
        data = {
            "type": "pull_friendlist",
            "content": {
                "sender": self.user_id,
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def pull_grouplist(self):
        data={
            "type":"pull_group_list",
            "content":{
                "owner":self.user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

#以下是发送文件的函数
    def send_file_request(self, chat_id, file_path):
        # 向服务器发送文件发送请求
        # 包括接收者的ID地址、和本机文件路径
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        file_size = os.path.getsize(file_path)
        if chat_id==None:
            return
        data = {
            'type': 'user_send_file',
            'content': {
                "msg_type": "friend_chat",
                "sender": self.user_id,
                "chat_id": chat_id,
                "msg": None,
                "filepath": file_path,
                "time": timestamp,
                # "time":now,
                "filesize": file_size,
                "is_avatar": False
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
                # "time":now,
                "filesize": file_size,
                "is_avatar": True,
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        print("更换头像请求成功发送")

    def receive_file_request(self, chat_id, file_path, content=None):
        # 向服务器发送文件接受请求
        # file_path是服务器发给我的，我要再发回去
        # 包括接收者的ID地址、和服务端文件路径
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        is_avatar = False
        filesize = None
        if content:
            is_avatar = True
            filesize = content['filesize']
        data = {
            'type': 'user_receive_file',
            'content': {
                "msg_type": "friend_chat",
                "sender": self.user_id,
                "chat_id": chat_id,
                "msg": None,
                "filepath": file_path,
                "time": timestamp,
                # "time":now,
                "filesize": filesize,
                "is_avatar": is_avatar
            }
        }
        if content:
            data["content"]["sender"] = content["sender"]
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        print("接收文件请求成功发送")
        # 在从服务器收到允许发文件的答复后，开始发文件线程

    def send_file(self, back_data, content):
        # 发送发送文件请求，服务器同意接受，在这里
        try:
            if back_data == "0000":
                print("服务器允许发送文件，准备发送力")
                shared_module.file_thread = FileSendThread(content["sender_ip"], content["port"], content["filepath"],
                                                           content["filesize"],content['is_avatar'])
                shared_module.file_thread.percentage.connect(shared_module.main_page.update_percentage)
                shared_module.file_thread.start()
                #shared_module.main_page.progress_bar_show()
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
                    print("服务器准备发送文件，我准备接收力！")
                    shared_module.file_thread = FileReceiveThread(content)
                    shared_module.file_thread.notify.connect(receive_file_handler)
                    shared_module.file_thread.percentage.connect(shared_module.main_page.update_mainpage_percentage)
                    #shared_module.main_page.progress_bar_show()

                    shared_module.file_thread.start()
                    print("头像接收完了")
                else:
                    print("服务器不允许接收文件，寄了，记载client_function,receive_file里头")
            except Exception as e:
                print("receive_file寄了，寄在client_function,receive_file里头：" + str(e))
            #调用我的chating_item的函数
            pass

    def receive_friend_message(self, back_data, content):
        is_avatar=content['is_avatar']
        print("进入了receive_friend_message\n")
            #这个是要留的
        if is_avatar:
            print("收到一个头像，正在存储……")
            self.receive_file_request(chat_id=None, file_path=content["filepath"], content=content)
        else:
            shared_module.main_page.print_online_message(content)
            print("收到一条消息/文件，正在处理……")
            pass

    def rcv_friendlist(self,back_data,content):

        friend_list_info = content["friend_list_info"]
        if back_data == "0012":
            # 好友列表获取成功
            self.friend_list = friend_list_info
            # friend_list_info是字典，partition，id,name
            print("拉取到了好友列表")
            print(friend_list_info)

        elif back_data == "0013":
            # 好友列表获取失败
            self.friend_list = friend_list_info
            print("好友列表为空")
        else:
            # 未知错误
            return None

    def rcv_group_list(self,back_data,content):
        group_list_info= content['group_list_info']
        if back_data=="0012":
            self.group_list=group_list_info
            print("拉取到了群聊列表")
            print(self.group_list)
        elif back_data=="0013":
            print("群聊列表为空")
        else:
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

    def delete_group(self, group_id):
        data = {
            "type": "delete_group",
            "content": {
                "group_id": group_id,
                "sender": self.user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def add_new_member(self, group_id, member_id):
        data = {
            "type": "add_new_member",
            "content": {
                "group_id": group_id,
                "member_id": member_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def pull_msg_list(self):
        data = {
            "type": "init_msg_list",
            "content": {
                "user_id": self.user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def init_msg_list(self, back_data, content):
        if back_data == "0000":
            print("申请消息列表成功")
            print(self.msg_list)
            self.msg_list = content["list"]
            print(self.msg_list)
            shared_module.main_page.init_chat_list()
        else:
            print("申请消息列表失败")

    def find_name(self, chat_id):
        num1 = int(str(chat_id)[0:5])
        num2 = int(str(chat_id)[5:10])
        if num1 == self.user_id:
            opp_id = num2
        else:
            opp_id = num1
        opp_name = ''
        for id, name, part in self.friend_list:
            if id == opp_id:
                opp_name = name
        print(opp_name)
        return opp_name

    def find_oppid(self, chat_id):
        num1 = int(str(chat_id)[0:5])
        num2 = int(str(chat_id)[5:10])
        if num1 == self.user_id:
            opp_id = num2
        else:
            opp_id = num1

        return opp_id

    def find_group_name(self,chat_id):
        n=''
        for group_id,group_name in self.group_list:
            if group_id==chat_id:
                n=group_name
                return n
        print(n)
        return n


    def rcv_create_group(self,back_data,content):
        if back_data=="0000":
            #群聊创建成功
            group_id=content['group_id']
            group_manager=content['group_manager']
            group_name=content['group_name']
            group_member=content['group_member']
            #   UI function 
            #group_chat()
            self.group_list.append([group_id,group_name])
            if group_manager==self.user_id:
                self.friend_chat("群组已经创建！",group_id)
            #
        elif back_data=="0001":
            pass
            # 群聊创建失败
            #   UI function
            pass
        else:
            return None

    def rcv_delete_group(self, back_data, content):
        if back_data == "0000":
            pass
            # 群聊删除成功
            #   UI function 
            pass
        elif back_data == "0001":
            pass
            # 群聊删除失败
            #   UI function
            pass
        else:
            return None

    def rcv_add_new_member(self, back_data, content):
        if back_data == "0000":
            pass
            #添加成员成功
            group_id=content['group_id']
            group_name=content['group_name']
#            group_member=content['group_member']
            #   UI function 
            self.group_list.append([group_id,group_name])
            self.friend_chat("我已加群！",group_id)
        elif back_data=="0001":
            pass
            # 添加成员失败
            #   UI function
            pass
        else:
            return None

    def append_msg(self, content):
        # TODO
        chat_id = content['chat_id']
        filepath = 'files/chats/' + str(chat_id) + '.json'
        if not os.path.exists('files/chats/'):
            os.makedirs('files/chats/')
        # 如filepath不存在，创建目录
        msg_list = []
        if not os.path.exists(filepath):
            # 如果文件不存在，创建空文件
            # 往空文件中写入json格式的"[]"
            with open(filepath, 'w') as files:
                json.dump(msg_list, files)
        else:
            with open(filepath, 'r') as files:
                msg_list = json.load(files)

        msg_list.insert(0, content)
        print(msg_list)
        with open(filepath, 'w') as files:
            json.dump(msg_list, files)

    def video_chat_request(self, chat_id):
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "user_video_chat",
            "content": {
                "user_id": self.user_id,
                "chat_id": chat_id,
                "time": timestamp
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def rcv_video_chat(self, back_data, content):
        # 0000，则是视频接受者收到此消息
        if back_data == "0000":
            sender_id = content["user_id"]
            sender_ip = content["user_ip"]
            time = content["time"]
            sender_name = content["username"]
            # 大概有个弹窗,可能放到window.py下面？
            shared_module.main_page.receive_an_vedio_request(content)
            print("收到了视频申请", sender_id, sender_ip, sender_name,time)
            # 把ans填了，然后去掉注释
            # ans = "yes" or "no"
            # self.ans_video_chat(ans, content)
            # if ans == "yes":
            #     ip = content['ip']
            #     shared_module.video_thread = VideoChatThread(ip)
            #     shared_module.video_thread.start()
        # 0001，则是视频发起者接受到此消息，因为接收者不在线
        elif back_data == "0001":
            # TODO 大概有个弹窗提示吧
            print("没这个人，或者好友不在线")

    def ans_video_chat(self, ans, content):
        # 发送同意或拒绝视频请求
        now = datetime.now()
        time = datetime.timestamp(now)
        content['time'] = time
        content['ans'] = ans
        data = {
            "type": "ans_video_chat",
            "content": content
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        print("all_send")

    def rcv_ans_video_chat(self, back_data, content):
        # 对方接收到同意或拒绝添加好友请求的回复
        # 返回发送者的用户ID、时间戳和回复内容
        # 对方收到好友请求并确定是否同意
        """
            data = {
                    "type": "user_video_chat",
                    "content": {
                        "user_id": self.user_id,
                        "chat_id": chat_id,
                        "time": timestamp,
                        "receiver_id":,
                        "receiver_ip":,
                        "user_ip":,
                        "username"
                    }
                }
            """
        sender = content["user_id"]
        time = content["time"]
        ans = content["ans"]
        name = content["username"]
        receiver_ip = content["receiver_ip"]
        print([sender, time, ans, name, receiver_ip])

        if ans == "yes":
            # 聊天！
            shared_module.video_thread = VideoChatThread(receiver_ip)
            shared_module.video_thread.start()
            print("收到", name, receiver_ip, "的消息，对方同意，开始视频聊天")
        else:
            print("收到", name, "回复，对方拒绝，舔狗舔到最后一无所有")

    def retrieve_password_request(self, user_id):
        data = {
            "type": "retrieve_password",
            "content": {
                "user_id": user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
