import socket
import json
import threading

def user_register(data, client_socket, address, database):
    print('收到注册信息')
    print('id'+ data["content"]["username"])
    print('pwd'+ data["content"]["userpwd"])
    #把数据放进数据库什么的

    back_data={
        "register_back": "0000"
    }
    json_back_data=json.dumps(back_data).encode('utf-8')
    socket.sendall(json_back_data)
    return 0