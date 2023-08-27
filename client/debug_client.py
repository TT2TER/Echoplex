from lib.public import shared_module
from client_fuction import Client
import socket
import json
shared_module.client = Client('127.0.0.1',12340)
client_send_filepath = "files/send_files/image.png"

# server_address = ("127.0.0.1", 12345)  # 服务器的 IP 地址和端口号
# client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# client_socket.connect(server_address)
# print(f"Connected to {server_address}")

# receiver_id = 10002
# shared_module.client.send_file_request(receiver_id,client_send_filepath)
# json_data = shared_module.client.client_socket.recv(10240)
# data = json.loads(json_data.decode('utf-8'))
# content = data['content']
# back_data = data['back_data']
# shared_module.client.send_file(back_data,content)
# shared_module.file_thread.wait()

sender_id = None
filepath = "files/None/image.jpg"
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
