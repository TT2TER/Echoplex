from user_send_file import *
from user_receive_file import *
import socket
# from server.db import *
from db.DataDB import *

database = sql_connection()
server_address = ('127.0.0.1', 12340)
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind(server_address)
server_socket.listen(5)
print(f"Server is listening on {server_address}")
client_socket, client_address = server_socket.accept()
print(f"Connected to client {client_address}")

# json_data = client_socket.recv(10240)
# received_data = json.loads(json_data.decode('utf-8'))
# # client_socket.sendall(json_data)
# user_send_file(received_data,client_socket,client_address,database)

json_data = client_socket.recv(10240)
received_data = json.loads(json_data.decode('utf-8'))

user_receive_file(received_data, client_socket, client_address, database)
