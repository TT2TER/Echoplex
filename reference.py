import socket
import threading
import json

# 创建 socket 对象
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# 绑定地址和端口
server_address = ('localhost', 12345)
server_socket.bind(server_address)

# 监听连接
server_socket.listen(5)
print("服务器等待连接...")

clients = []

def handle_client(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if not data:
                break
            
            received_data = json.loads(data.decode('utf-8'))
            print("收到消息:", received_data)
            
            # 广播消息给所有客户端
            for client in clients:
                if client != client_socket:
                    client.sendall(data)
        except:
            break
    
    clients.remove(client_socket)
    client_socket.close()

while True:
    client_socket, client_address = server_socket.accept()
    print("连接来自:", client_address)
    
    clients.append(client_socket)
    
    client_handler = threading.Thread(target=handle_client, args=(client_socket,))
    client_handler.start()