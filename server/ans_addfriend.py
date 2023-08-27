import json
from collections import defaultdict
from global_data import online_clients, user_mailboxes
from db.DataDB import select_table
from db.table_user_friend import insert_table_user_friend
from db.table_relation import insert_table_relation

#好友请求应答处理类似于消息处理，在线直接发送请求，离线缓存在队列
#TODO:好友应答队列需要全局设置

ans_addfriendlist = defaultdict(list)

def ans_addfriend(received_data, socket, address, database):
    try:
        content = received_data["content"]
        sender = content["sender"]
        receiver = content["receiver"]
        time = content["time"]
        ans = content["ans"]
        partition = content["partition"]
        name = content["name"]
        send_message(ans, sender, receiver, time, name)
            #没有数据库插入好友请求回应
            #TODO：
    except Exception as e:
        print("服务端处理好友请求回应出错: " + str(e))
     #更新好友列表数据库
    try:
        if ans == "yes":
            #更新user_friend表
            concatenated_str = str(min(sender,receiver)) + str(max(sender, receiver))
            chatid = int(concatenated_str)
            insert_table_user_friend(database, "user_friend", min(sender,receiver),max( receiver,sender), chatid)
            #更新table_relation表
            insert_table_relation(database,sender,receiver,partition,"table_relation")
            insert_table_relation(database,receiver,sender,"default","table_relation")
    except Exception as e:
        print("服务端更新好友列表数据库出错: " + str(e))


def send_message(ans,sender, receiver, time, name):
    back_data_addfriend = {
        "type": "ans_addfriend",
        "back_data": "0000",
        "content": {
            "ans": ans,
            "sender": sender,
            "time": time,
            "name": name
        }
    }
    json_message = json.dumps(back_data_addfriend).encode('utf-8')
    if receiver in online_clients:
            receiver_socket, _ = online_clients[receiver]
            receiver_socket.sendall(json_message)
    else:
        user_mailboxes[receiver].append((sender, json_message))
        print("好友请求回应已缓存")