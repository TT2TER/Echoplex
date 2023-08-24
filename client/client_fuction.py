import socket
import json
import threading


class Client:
    def __init__(self):
        self.client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = ('127.0.0.1', 13582)
        self.client_socket.connect(self.server_address)

    def user_login(self, user_id, user_pwd):
        def isinteger(string):
            try:
                int(string)
                return True
            except ValueError:
                return False
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
        self.client_socket.sendall(json_data)
        back_json_data = self.client_socket.recv(1024)
        back_data = json.loads(back_json_data.decode('utf-8'))
        if back_data["back_data"] == "0002":
            print("Login Success")
            return [0]
        elif back_data["back_data"] == "0003":
            print("Login Failed")
            return [1]

    def user_register(self, user_name, user_image, user_pwd, user_email):
        if len(user_pwd) > 25 or len(user_pwd) < 6:
            return [2]
        else:
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
            back_json_data = self.client_socket.recv(1024)
            back_data = json.loads(back_json_data.decode('utf-8'))
            if back_data["back_data"] == "0000":
                print("Register Success")
                return [0, str(back_data["user_id"])]
            elif back_data["back_data"] == "0001":
                print("Register Fail, Sever Error")
                return [1]
            
    def friendinfo(self, user_id): 
        
        data = {
            'type': 'friendinfo',
            'content': {
                'user_id': user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        self.client_socket.sendall(json_data)
        back_json_data = self.client_socket.recv(1024)
        back_data = json.loads(back_json_data.decode('utf-8'))
        if back_data["back_data"] == "0002":
            #成功
            return back_data["friendinfo"]        #返回好友信息,分别是id,name,email
        elif back_data["back_data"] == "0003":
           #失败
            return 1  
        else:
            return 2          #服务端返回值出错
        
        

        
 
