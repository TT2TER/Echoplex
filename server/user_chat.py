import json
from global_data import online_clients
from global_data import user_mailboxes
from db.DataDB import search_member, search_all_user, sql_connection
from db.table_chat import insert_table_chat
from db.table_file import insert_table_file
from tool_fuction import find_friend_id


def user_chat(received_data, socket, address, database):
    # user_chat可能被user_send_file在别的线程调用，要重新建一个
    database = sql_connection()
    try:
        content = received_data["content"]
        chat_id = content["chat_id"]
        time = content["time"]
        msg = content["msg"]
        sender_id = content["sender"]
        filepath = content["filepath"]
        filesize = content['filesize']
        if chat_id is not None:
            chat_id = str(chat_id)

        # 广播
        if chat_id is None:
            receivers = []
            receivers_all = search_all_user(database, "user")
            for receiver_all in receivers_all:
                receiver = receiver_all[0]
                receivers.append(receiver)
            print("broadcast找到的receivers:")
            print(receivers)
        # 私聊
        elif len(chat_id) == 10:
            # 一个是发送者，一个是接收者，但不知道是哪个
            sender_id = content["sender"]
            filepath = content["filepath"]
            receiver_id = find_friend_id(sender_id, chat_id)
            content["receiver"] = receiver_id
            receivers = [sender_id, receiver_id]

        # 群聊
        elif len(chat_id) == 5:
            receivers = search_member(database, "group_member", chat_id)
            print(receivers)
        else:
            print(f"chat_id:{chat_id}不符合格式，请检查")
    except Exception as e:
        print("user_chat寄了，看报错吧", e)
    finally:
        if not filepath:
            insert_table_chat(database, sender_id, chat_id, chat_time=time, chat_content=msg, table_name="chat")
        else:
            insert_table_file(database, "file", sender_id, chat_id, time, filepath, filesize)
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
