import socket
import json
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 13579)
client_socket.connect(server_address)


def user_register():
    username = input("Username: ")
    userpwd = input("Password: ")
    user_repwd = input("Retype Password: ")
    if userpwd != user_repwd:
        print("两次密码不一致")
    else:
        data={
            'type': 'user_register',
            'content': {
                'username': username,
                'userpwd': userpwd
            }
        }
        json_data = json.dumps(data).encode('utf-8')
        client_socket.sendall(json_data)
        back_json_data = client_socket.recv(1024)
        back_data = json.loads(back_json_data.decode('utf-8'))
        if back_data["register_back"] == "0000":
            print("Register Success")


if __name__ == "__main__":
    user_register()
    # TODO
