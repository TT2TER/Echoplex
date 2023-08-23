import socket
import json
import threading

class Login:
    
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 13579)
client_socket.connect(server_address)

def user_login():
    #获取账号密码
    username = "test"
    userpwd = "test"
    data={
        'type':'user_login',
        'content':{
            'user_name': username,
            'user_pwd': userpwd
        }
    }
    json_data=json.dumps(data).encode('utf-8')
    client_socket.sendall(json_data)
    back_json_data=client_socket.recv(1024)
    back_data=json.loads(back_json_data.decode('utf-8'))
    if back_data["back_data"] == "0002":
        #登录成功的动作
        print("login success")
    elif back_data["back_data"] == "0003":
        #从back_data中获取错误信息并显示



def user_register():
    #和界面交互获得 id name pwd 图床链接 email
    user_id = ""
    user_name = ""
    user_image = ""
    user_pwd = ""
    user_repwd = ""
    user_email = ""
    if user_pwd != user_repwd:
        print("两次密码不一致")
    else:
        #对用户名、昵称、email等进行限制

        data={
            'type': 'user_register',
            'content': {
                'user_name': user_name,
                'user_pwd': user_pwd,
                'user_email': user_email,
                'user_image': user_image,
                'user_id': user_id
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        client_socket.sendall(json_data)
        back_json_data = client_socket.recv(1024)
        back_data = json.loads(back_json_data.decode('utf-8'))
        if back_data["back_data"] == "0000":
            print("Register Success")
        elif back_data["back_data"] == "0001":
            print("Register Fail, Sever Error")


if __name__ == "__main__":
    # TODO
