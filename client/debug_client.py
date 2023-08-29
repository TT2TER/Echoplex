from lib.public import shared_module
from client_fuction import Client
import socket
import json


# 这一段用来测试文件相关功能
shared_module.client = Client('127.0.0.1', 12340)
client_send_filepath = "files/send_files/image.png"

# 更换头像
# shared_module.client.change_avatar_request(client_send_filepath)
# json_data = shared_module.client.client_socket.recv(10240)
# data = json.loads(json_data.decode('utf-8'))
# print(data)
# content = data['content']
# back_data = data['back_data']
# shared_module.client.send_file(back_data, content)
# shared_module.file_thread.wait()

# 这一段测试用户发送文件
# receiver_id = 10002
# shared_module.client.send_file_request(receiver_id, client_send_filepath)
# json_data = shared_module.client.client_socket.recv(10240)
# data = json.loads(json_data.decode('utf-8'))
# print(data)
# content = data['content']
# back_data = data['back_data']
# shared_module.client.send_file(back_data, content)
# shared_module.file_thread.wait()


# 这一段测试用户接收文件
sender_id = None
filepath = "files/None/image.png"
shared_module.client.receive_file_request(sender_id, filepath)
json_data = shared_module.client.client_socket.recv(10240)
data = json.loads(json_data.decode('utf-8'))
content = data['content']
back_data = data['back_data']
shared_module.client.receive_file(back_data,content)
shared_module.file_thread.wait()


# shared_module.client.receive_file()
# shared_module.client.receive_file_request()
# shared_module.client.send_file()
# shared_module.client.send_file_request()
