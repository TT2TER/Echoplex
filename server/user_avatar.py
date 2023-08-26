import threading
from global_data import server_address
from user_send_file import user_send_file



def user_avatar(received_data, socket, address, database):
    user_send_file(received_data, socket, address, database)


def handle_client(client_socket):
    with open('received_avatar.jpg', 'wb') as f:
        while True:
            data = client_socket.recv(1024)
            if not data:
                break
            f.write(data)
    client_socket.close()
