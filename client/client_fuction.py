import socket
import json
import threading
from datetime import datetime
from lib.public import shared_module

class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('127.0.0.1', 13582)
        self.client_socket.connect(self.server_address)
        self.user_id = None
        # self.udp_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # self.udp_socket.bind(("127.0.0.1", 13570))

    def user_login(self, user_id, user_pwd):
        def isinteger(string):
            try:
                int(string)
                return True
            except ValueError:
                return False

        # 判断所输入账号是否合法
        if not isinteger(user_id) or len(user_id) != 5:
            print("Login Failed")
            return [2]
        data = {
            'type': 'user_login',
            'content': {
                'user_id': user_id,
                'user_pwd': user_pwd
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        # self.client_socket.sendall(json_data)
        # back_json_data = self.client_socket.recv(1024)
        # back_data = json.loads(back_json_data.decode('utf-8'))
        # if back_data["back_data"] == "0002":
        #     print("Login Success")
        #     #登陆成功后保存本账号
        #     self.user_id = int(data["content"]["user_id"])
        #     return [0]
        # elif back_data["back_data"] == "0003":
        #     print("Login Failed")
        #     return [1]

    #向服务端发送注册请求
    def user_register(self, user_name, user_image, user_pwd, user_email):
        if len(user_pwd) > 25 or len(user_pwd) < 6:
            return [2]
        else:
            data = {
                'type': 'user_register',
                'content': {
                    'user_name': shared_module.reg_page.return_to_login,
                    'user_pwd': user_pwd,
                    'user_email': user_email,
                    'user_image': user_image
                }
            }
            json_data = json.dumps(data).encode('utf-8')
            self.client_socket.sendall(json_data)
            # back_json_data = self.client_socket.recv(1024)
            # back_data = json.loads(back_json_data.decode('utf-8'))
            # if back_data["back_data"] == "0000":
            #     print("Register Success")
            #     return [0, str(back_data["user_id"])]
            # elif back_data["back_data"] == "0001":
            #     print("Register Fail, Sever Error")
            #     return [1]
    
    #向服务端发送好友拉取请求
    def friendinfo(self, user_id): 
        
        data = {
            'type': 'friendinfo',
            'content': {
                'user_id': user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        # back_json_data = self.client_socket.recv(1024)
        # back_data = json.loads(back_json_data.decode('utf-8'))
        # if back_data["back_data"] == "0002":
        #     #成功
        #     return back_data["friendinfo"]        #返回好友信息,分别是id,name,email
        # elif back_data["back_data"] == "0003":
        #    #失败
        #     return 1  
        # else:
        #     return 2          #服务端返回值出错
        

    def user_chat(self, msg, receiver):
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
        # back_json_data = self.client_socket.recv(2048)
        # #需要服务端返回消息
        # back_data = json.loads(back_json_data.decode('utf-8'))

    def group_chat(self, msg, group_id):
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
        # back_json_data = self.client_socket.recv(2048)
        # #需要服务端返回消息
        # back_data = json.loads(back_json_data.decode('utf-8'))

    def private_group_chat(self, msg, group_id, receiver):
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
        # back_json_data = self.client_socket.recv(2048)
        # #需要服务端返回消息
        # back_data = json.loads(back_json_data.decode('utf-8'))

    def user_send_file(self, filename, receiver):
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
        # back_json_data = self.client_socket.recv(2048)
        # back_data = json.loads(back_json_data.decode('utf-8'))
        # if back_data == "知道了，客户端发文件过来吧":
        #     with open(filename, 'rb') as file:
        #         while True:
        #             data = file.read(4096)  # 读取更大的块
        #             if not data:
        #                 break
        #             self.client_socket.send(data)

    def pull_message(self):
        data = {
            "type": "pull_message",
            "content": {
                "sender": self.user_id,
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)

    def server_handler(self):
        # shared_module.login_page.show_registration_page()
        while True:
            try:
                # bufsize 指定要接收的最大数据量
                data = self.client_socket.recv(10240)
                received_data = json.loads(data.decode('utf-8'))
                print("收到服务端消息：", received_data)
            except Exception as e:
                print("服务端已经下线或者收消息过程中寄了，自己看报错吧：" + str(e))
                break
            try:
                print("server_handler处理ing……")
                message_handlers = {
                    'user_register': user_register,
                    'user_login': user_login,
                    'user_chat': user_chat,
                    'user_send_file': receive_file
                }
                handler = message_handlers.get(received_data['type'], None)
                back_data = received_data.get('back_data', None)
                content = received_data.get('content', None)
                if handler:
                    print("handler为" + getattr(handler, "__name__", "unknown_function"))
                    succ = handler(back_data, content)
                    print("处理结果：" + str(succ))
                else:
                    print("收到了服务器不认识的消息类型欸")
                    break
            except Exception as e:
                print("连接异常，准备断开: " + str(e))
                break
            finally:
                print("server_handler完工，等待下一个请求oVo")


