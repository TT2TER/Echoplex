import socket
import threading
import json
import sys
from time import sleep
sys.path.append("..")
from global_config import *

def handle_client(socket, address):
    try:
        sleep(5)
        back_data={
            'type': "user_register",
            'back_data': '0000',
            'content': {
                'user_id': 10001
            }
        }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        sleep(5)
        back_data={
            'type':"user_register",
            "back_data": '0001'
        }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        sleep(5)
        back_data={
            'type': 'user_login',
            'back_data': '0003'
        }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        sleep(5)
        socket.close()
        print("测试结束")
    except:
        print("EEEERRRRROOOOORRRRR")



if __name__ == "__main__":
    try:
        # 创建TCPsocket对象
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定地址和端口
        server_address = (get_value('server_address'), get_value('server_port'))
        server_socket.bind(server_address)
        print("TCP Server is listening on {}:{}".format(server_address[0], server_address[1]))
        # 创建UDPsocket对象
        # chat_server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        # chat_server_address = ('127.0.0.1', 13578)
        # chat_server_socket.bind(chat_server_address)
        # print("UDP Server is listening on {}:{}".format(chat_server_address[0], chat_server_address[1]))
        # TCP 监听
        # backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量s
        backlog = 20
        server_socket.listen(backlog)
        print("服务器等待连接？O.o")
        while True:
            new_socket, client_address = server_socket.accept()
            print("服务器连接上了客户端" + str(client_address) + "，准备干活！")
            client_handler = threading.Thread(target=handle_client, args=(new_socket, client_address))
            client_handler.start()
    except Exception as e:
        print("服务器socket寄了，原因是：" + str(e))
