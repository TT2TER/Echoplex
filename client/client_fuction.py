import socket
import json
import threading
from datetime import datetime
from lib.public import shared_module


class Client:
    def __init__(self,ip,port):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip, int(port))
        self.client_socket.connect(self.server_address)
        self.user_id = None

    def back_massage_handler(self, received_data):
        # 处理发射回来的信号
        try:
            message_handlers = {
                'user_register': shared_module.reg_page.recv_register,
                'user_login': shared_module.login_page.recv_login
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
    def friendinfo(self, user_id):
        # 向服务器请求好友信息
        # 包括要请求信息的好友的用户ID
        # 根据服务器的响应返回好友信息或错误码
        data = {
            'type': 'friendinfo',
            'content': {
                'user_id': user_id
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
                "time": timestamp
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
                "time": timestamp
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

    def user_send_file(self, filename, receiver):
        # 发送文件给另一个用户
        # 包括文件名、发送者的用户ID、接收者的用户ID和时间戳
        # 根据服务器的响应可能进行文件传输
        # filename = "files/package.zip"
        now = datetime.now()
        timestamp = datetime.timestamp(now)
        data = {
            "type": "user_send_file",
            "content": {
                "sender": self.user_id,
                "receiver": receiver,
                "time": timestamp
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

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

    def create_group(self):
        # 创建一个群组
        # 包括群主的用户ID、成员列表和群组名称
        group_member = [10001, 10002]
        group_name = "test_group"
        data = {
            "type": "create_group",
            "content": {
                "group_manager": self.user_id,
                "group_member": group_member,
                "group_name": group_name
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def user_addfriend(self, user_id, target_id):
        # 发送添加好友请求
        # 包括发送者的用户ID、接收者的用户ID和时间戳
        # 发送请求添加好友时间
        now = datetime.now()
        _time = datetime.timestamp(now)
        data = {
            "type": "user_addfriend",
            "content": {
                "sender": user_id,
                "receiver": target_id,
                "time": _time
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def rcv_addfriend(self, back_data, content):
        # 对方接收到添加好友请求并确认是否同意
        # 返回发送者的用户ID和时间戳

        # 对方收到好友请求并确定是否同意
        sender = back_data["content"]["sender"]
        time = back_data["content"]["time"]
        return [sender, time]

    def ans_addfriend(self, ans, user_id, target_id):
        # 发送同意或拒绝添加好友请求
        # 包括回复内容、发送者的用户ID、接收者的用户ID和时间戳

        # 发送同意或拒绝请求
        now = datetime.now()
        time = datetime.timestamp(now)
        data = {
            "type": "ans_addfriend",
            "content": {
                "sender": user_id,
                "receiver": target_id,
                "time": time,
                "ans": ans
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def rcv_ans_addfriend(self, back_data, content):
        # 对方接收到同意或拒绝添加好友请求的回复
        # 返回发送者的用户ID、时间戳和回复内容

        # 对方收到好友请求并确定是否同意
        sender = back_data["content"]["sender"]
        time = back_data["content"]["time"]
        ans = back_data["content"]["ans"]
        return [sender, time, ans]

