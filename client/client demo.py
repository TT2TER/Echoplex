import socket
import threading
import json


def receive_messages():
    while True:
        try:
            data = client_socket.recv(1024).decode('utf-8')
            if not data:
                break
            handle_message(data)
        except:
            break


def handle_message(data):
    try:
        message = json.loads(data)
        msg_type = message["type"]
        content = message["content"]

        if msg_type == "new_message":
            sender = content["sender"]
            msg = content["msg"]
            print(f"New message from {sender}: {msg}")

        # Add other message types handling here

    except json.JSONDecodeError:
        pass


def send_messages():
    while True:
        msg_type = input("Enter message type (friend_chat/group_chat): ")
        if msg_type not in ["friend_chat", "group_chat"]:
            print("Invalid message type")
            continue

        sender = input("Enter your username: ")
        msg = input("Enter message: ")

        if msg_type == "friend_chat":
            receiver = input("Enter receiver's username: ")
            message = {
                "type": msg_type,
                "content": {
                    "sender": sender,
                    "receiver": receiver,
                    "msg": msg
                }
            }
        elif msg_type == "group_chat":
            group_id = input("Enter group ID: ")
            message = {
                "type": msg_type,
                "content": {
                    "sender": sender,
                    "group_id": group_id,
                    "msg": msg
                }
            }

        client_socket.send(json.dumps(message).encode('utf-8'))


client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(('127.0.0.1', 12345))

receive_thread = threading.Thread(target=receive_messages)
receive_thread.start()

send_thread = threading.Thread(target=send_messages)
send_thread.start()

send_thread.join()
client_socket.close()
