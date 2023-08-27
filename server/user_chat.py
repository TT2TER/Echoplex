import json
from global_data import online_clients
from global_data import user_mailboxes


def user_chat(received_data, socket, address, database):
    try:
        content = received_data["content"]
        msg_type = content["msg_type"]

        if msg_type == "friend_chat":
            sender = content["sender"]
            receiver = content["receiver"]
            msg = content["msg"]
            time = content["time"]
            filepath = content["filepath"]
            filesize = content["filepath"]
            send_message(sender, receiver, msg, time, filepath, filesize)
            # 需要向数据库中插入数据、需要向客户端返回数据
            # TODO:

        elif msg_type == "group_chat":
            sender = content["sender"]
            group_id = content["group_id"]
            msg = content["msg"]
            time = content["time"]
            filepath = content["filepath"]
            filesize = content["filesize"]
            send_group_message(sender, group_id, msg, time, filepath, filesize)

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


def send_message(sender, receiver, msg, time, filepath, filesize):
    message = {
        "type": "friend_chat",
        # "back_data": True,
        "content": {
            "sender": sender,
            "msg": msg,
            "time": time,
            "filepath": filepath,
            "filesize": filesize
        }
    }
    json_message = json.dumps(message).encode('utf-8')
    # 发给sender，若reveiver也在线就发，不在线加进mailbox内
    sender_socket, _ = online_clients[sender]
    sender_socket.sendall(json_message)
    if receiver in online_clients:
        receiver_socket, _ = online_clients[receiver]
        receiver_socket.sendall(json_message)
    else:
        user_mailboxes[receiver].append(json_message)


def send_group_message(sender, group_id, msg, time, filepath, filesize):
    message = {
    "type": "new_message",
    "content": {
        "sender": sender,
        "group_id": group_id,
        "msg": msg,
        "time": time,
        "filepath": filepath,
        "filesize": filesize
        }
    }
    json_message = json.dumps(message).encode('utf-8')
    # receivers = SQL TODO
    for receiver in receivers:
        if receiver in online_clients:
            receiver_socket, _ = online_clients[receiver]
            receiver_socket.sendall(json_message)
        else:
            user_mailboxes[receiver].append((sender, msg, group_id))

# TODO 小团体 代码是错的 还做吗这功能
def send_secret_group_message(sender, group_id, msg, receiver=[100001, 100002]):
    # receiver = SQL TODO
    if receiver in online_clients:
        receiver_socket, _ = online_clients[receiver]
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


# 在客户端拉取消息的请求到达时调用这个函数，把消息发送给客户端
def retrieve_messages(received_data, socket, address, database):
    client_id = received_data['content']['sender']
    try:
        if client_id in user_mailboxes:
            mailbox = user_mailboxes[client_id]
            while mailbox:
                json_message = mailbox.pop(0)  # 从队列头中取出一条消息
                try:
                    socket, _ = online_clients[client_id] # 发送消息
                    socket.sendall(json_message)
                except Exception as e:
                    print(f"Error sending message to client {client_id}: {e}")
            # user_mailboxes[client_id] = []  # 清空该用户的邮件箱
    except Exception as e:
        print(f"Error retrieving messages: {e}")
