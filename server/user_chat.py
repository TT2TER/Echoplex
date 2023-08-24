clients = []
message_history = []


def user_chat():
    print("TODO")


def send_message(client_socket):
    while True:
        try:
            message = client_socket.recv(1024)
            if not message:
                break
            message_history.append(message)
            broadcast(message, client_socket)
        except:
            break


def broadcast(message, sender_socket):
    for client_socket in clients:
        if client_socket != sender_socket:
            try:
                client_socket.send(message)
            except:
                clients.remove(client_socket)


def send_message_history(client_socket):
    for message in message_history:
        client_socket.send(message)
