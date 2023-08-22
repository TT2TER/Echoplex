import socket
import json
import threading


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                received_data = json.loads(data.decode('utf-8'))
                print("收到消息:", received_data)
        except:
            break


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 13579)
client_socket.connect(server_address)

receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
receive_thread.start()

while True:
    # group_id = input("输入群聊ID: ")
    # sender = input("输入您的用户名: ")
    content = input("输入消息内容: ")
    # visible_to = input("输入可见的用户名列表，以逗号分隔: ").split(',')

    message = {
        "type": "message",
        # "timestamp": "2023-08-22T12:34:56",
        # "sender": sender,
        # "group_id": group_id,
        "content": content,
        # "visible_to": visible_to
    }

    json_data = json.dumps(message).encode('utf-8')
    client_socket.sendall(json_data)
