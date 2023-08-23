import socket
import json
import threading

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('127.0.0.1', 13579)
client_socket.connect(server_address)


def user_register():
    print("写了个寄吧")
    # TODO


if __name__ == "__main__":
    print("写了个寄吧")
    # TODO
