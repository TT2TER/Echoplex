import socket
import threading
import json
from collections import defaultdict
from global_data import online_clients

# Create a defaultdict to store user mailboxes (offline messages)
user_mailboxes = defaultdict(list)


# user_mailboxes["user1"].append(("user2", "Hello!"))
# user_mailboxes["user1"].append(("user3", "How are you?"))


def user_chat(received_data, socket, address, database):
    try:
        message = json.loads(received_data)
        content = message["content"]
        msg_type = content["msg_type"]

        if msg_type == "friend_chat":
            sender = content["sender"]
            receiver = content["receiver"]
            msg = content["msg"]
            time = content["time"]
            send_message(sender, receiver, msg)

        elif msg_type == "group_chat":
            sender = content["sender"]
            group_id = content["group_id"]
            msg = content["msg"]
            time = content["time"]
            send_group_message(sender, group_id, msg)

        elif msg_type == "private_group_chat":
            sender = content["sender"]
            group_id = content["group_id"]
            msg = content["msg"]
            time = content["time"]
            receiver = content["receiver"]
            # create_group()
            # send_group_message()

        # Add other message types here

    except json.JSONDecodeError:
        pass


def send_message(sender, receiver, msg):
    if receiver in online_clients:
        receiver_socket = online_clients[receiver]
        message = {
            "type": "new_message",
            "content": {
                "sender": sender,
                "msg": msg
            }
        }
        receiver_socket.send(json.dumps(message).encode('utf-8'))
    else:
        user_mailboxes[receiver].append((sender, msg))


def send_group_message(sender, group_id, msg):
    # receiver = SQL TODO
    receiver = [100001, 100002]
    if receiver in online_clients:
        receiver_socket = online_clients[receiver]
        message = {
            "type": "new_message",
            "content": {
                "sender": sender,
                "msg": msg
            }
        }
        receiver_socket.send(json.dumps(message).encode('utf-8'))
    else:
        user_mailboxes[receiver].append((sender, msg, group_id))


def send_secret_group_message(sender, group_id, msg, receiver = [100001, 100002]):
    # receiver = SQL TODO
    if receiver in online_clients:
        receiver_socket = online_clients[receiver]
        message = {
            "type": "new_message",
            "content": {
                "sender": sender,
                "msg": msg
            }
        }
        receiver_socket.send(json.dumps(message).encode('utf-8'))
    else:
        user_mailboxes[receiver].append((sender, msg))


def get_username_by_socket(socket):
    for username, user_socket in user_sockets.items():
        if user_socket == socket:
            return username
    return None
