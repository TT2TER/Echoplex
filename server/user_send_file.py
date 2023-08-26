import socket
import os
import threading
import json
from user_chat import user_chat

def user_send_file(received_data, _socket, address, database):
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receive_socket.bind(('0.0.0.0', 0))
    ip, port = receive_socket.getsockname()
    receive_socket.listen(1)
    print(f"File server listening on {ip}:{port}")
    filepath = received_data['content']['filepath']

    def receive_file():
        message = {
            "type": "user_send_file",
            "back_data": "0000",
            "content": {
                "sender_ip": ip,
                "port": port,
                "filepath": filepath
            }
        }
        json_message = json.dumps(message).encode('utf-8')
        _socket.senall(json_message)
        client_socket, client_address = receive_socket.accept()
        print(f"已经连接上'{client_address}'，准备收取文件")
        try:
            os.makedirs(os.path.dirname(filepath), exist_ok=True)  # 创建文件夹路径
            with open(filepath, 'xb') as file:
                while True:
                    data = client_socket.recv(10240)
                    if not data:
                        break
                    file.write(data)
            print(f"File '{filepath}' received and saved")
        except FileExistsError:
            print(f"File '{filepath}' already exists")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            user_chat(received_data, _socket, address, database)
            receive_socket.close()

    send_thread = threading.Thread(target=receive_file, args=(_socket, filepath))
    send_thread.start()

    # client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # client_socket.connect((ip, port))
    # with open(filepath, 'rb') as file:
    #     while True:
    #         data = file.read(4096)
    #         if not data:
    #             break
    #         client_socket.send(data)
    # client_socket.shutdown(socket.SHUT_WR)
    # print(f"File '{filepath}' sent")
    # client_socket.close()
