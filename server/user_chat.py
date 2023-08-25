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
            # 需要向数据库中插入数据、需要向客户端返回数据
            # TODO:
            
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
    message = {
        "type": "friend_chat",
        # "back_data": True,
        "content": {
            "sender": sender,
            "msg": msg
        }
    }
    json_message = json.dumps(message).encode('utf-8')
    if receiver in online_clients:
        receiver_socket = online_clients[receiver]
        receiver_socket.sendall(json_message)
    else:
        user_mailboxes[receiver].append(json_message)


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


def send_secret_group_message(sender, group_id, msg, receiver=[100001, 100002]):
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


def get_userip_by_userid(_userid):
    for userid, userip in online_clients.items():
        if userid == _userid:
            return userip
    return None


# 在客户端拉取消息的请求到达时调用这个函数，把消息发送给客户端
def retrieve_messages(client_id):
    try:
        if client_id in user_mailboxes:
            mailbox = user_mailboxes[client_id]
            while mailbox:
                json_message = mailbox.pop(0)  # 从队列头中取出一条消息
                try:
                    online_clients[client_id].sendall(json_message)  # 发送消息
                except Exception as e:
                    print(f"Error sending message to client {client_id}: {e}")
            # user_mailboxes[client_id] = []  # 清空该用户的邮件箱
    except Exception as e:
        print(f"Error retrieving messages: {e}")
