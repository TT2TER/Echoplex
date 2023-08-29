import socket
import threading
import json
import os

def user_receive_file(received_data, _socket, address, database):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.bind(("127.0.0.1", 0))
    ip, port = send_socket.getsockname()
    send_socket.listen(1)
    print(f"File server listening on {ip}:{port}")
    filepath = received_data['content']['filepath']
    is_avatar = received_data['content']['is_avatar']
    chat_id = received_data['content']['chat_id']
    sender = received_data['content']['sender']


    def send_file():
        try:
            with open(filepath, 'rb') as file:
                filesize = os.path.getsize(filepath)
                message = {
                    "type": "user_receive_file",
                    "back_data": "0000",
                    "content": {
                        "sender_ip": ip,
                        "port": port,
                        "filepath": filepath,
                        "filesize": filesize,
                        "is_avatar": is_avatar,
                        "chat_id": chat_id,
                        "sender": sender
                    }
                }
                json_message = json.dumps(message).encode('utf-8')
                _socket.sendall(json_message)

                client_socket, client_address = send_socket.accept()
                print(f"已经连接上'{client_address}'，准备发送文件")

                total_sent = 0
                while total_sent < filesize:
                    data = file.read(4096)
                    if not data:
                        break
                    sent = client_socket.send(data)
                    total_sent += sent

                print(f"文件 '{filepath}' 已发送")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            send_socket.close()

    send_thread = threading.Thread(target=send_file)
    send_thread.start()
