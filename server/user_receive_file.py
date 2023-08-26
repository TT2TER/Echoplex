import socket
import threading
import json


def user_receive_file(received_data, _socket, address, database):
    send_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    send_socket.bind(('0.0.0.0', 0))
    ip, port = send_socket.getsockname()
    send_socket.listen(1)
    print(f"File server listening on {ip}:{port}")
    filepath = received_data['content']['filepath']

    def send_file():
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
        client_socket, client_address = send_socket.accept()
        print(f"已经连接上'{client_address}'，准备收取文件")
        try:
            with open(filepath, 'rb') as file:
                while True:
                    data = file.read(4096)
                    if not data:
                        break
                    client_socket.sendall(data)

            print(f"文件 '{filepath}' 已发送")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            send_socket.close()

    send_thread = threading.Thread(target=send_file, args=(_socket, filepath))
    send_thread.start()
