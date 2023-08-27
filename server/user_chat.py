import json
from global_data import online_clients
from global_data import user_mailboxes
from db.DataDB import search_member, search_all_user


def user_chat(received_data, socket, address, database):
    try:
        content = received_data["content"]
        msg_type = content["msg_type"]
        content["type"] = msg_type

        if msg_type == "friend_chat":
            receivers = [content["receiver"], content["sender"]]

        elif msg_type == "broadcast":
            receivers = search_all_user(database, "user")

        elif msg_type == "group_chat":
            group_id = content["group_id"]
            receivers = search_member(database, "chat", group_id)

        elif msg_type == "private_group_chat":
            pass
    except json.JSONDecodeError:
        pass
    finally:
        json_message = json.dumps(received_data).encode('utf-8')
        for receiver in receivers:
            if receiver in online_clients:
                receiver_socket, _ = online_clients[receiver]
                receiver_socket.send(json_message)
            else:
                user_mailboxes[receiver].append(json_message)


# 在客户端拉取消息的请求到达时调用这个函数，把消息发送给客户端
def retrieve_messages(received_data, socket, address, database):
    client_id = received_data['content']['sender']
    try:
        if client_id in user_mailboxes:
            mailbox = user_mailboxes[client_id]
            while mailbox:
                json_message = mailbox.pop(0)  # 从队列头中取出一条消息
                try:
                    socket, _ = online_clients[client_id]  # 发送消息
                    socket.sendall(json_message)
                except Exception as e:
                    print(f"Error sending message to client {client_id}: {e}")
            # user_mailboxes[client_id] = []  # 清空该用户的邮件箱
    except Exception as e:
        print(f"Error retrieving messages: {e}")
