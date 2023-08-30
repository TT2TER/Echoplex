import socket
import json
from datetime import datetime


def send_request(request_data):
    host = '127.0.0.1'
    port = 12345
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client_socket.connect((host, port))
    client_socket.sendall(json.dumps(request_data).encode('utf-8'))

    response = client_socket.recv(1024)
    if response:
        print("Server response:", response.decode('utf-8'))

    client_socket.close()


def main():
    now = datetime.now()
    timestamp = datetime.timestamp(now)
    request_data = {
        "type": "create_group",
        "content": {
            "group_manager": 10001,
            "group_member": [10001, 10002],
            "group_name": "group_name",
            "group_create_time": timestamp,
            "group_image": "path_to_image.jpg"
        }
    }
    send_request(request_data)


if __name__ == '__main__':
    main()
