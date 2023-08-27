import json
from collections import defaultdict
from global_data import online_clients
from db.DataDB import select_table

#好友请求处理类似于消息处理，在线直接发送请求，离线缓存在队列
#TODO:加好友请求队列需要全局设置
user_addfriendlist = defaultdict(list)

def user_addfriend(received_data, socket, address, database):
     #判断好友是否存在
    res = select_table(database, "user", user_id = int(received_data["content"]["receiver"]) )    #id为int型

    if len(res) == 0:  # 未注册，返回空列表
        back_data_addfriend = {
            "type": "ans_addfriend",
            'back_data': "0001"
        }
        json_message = json.dumps(back_data_addfriend).encode('utf-8')
        socket.sendall(json_message)
        return "好友不存在"
    else:
        try:
             content = received_data["content"]
             sender = content["sender"]
             receiver = content["receiver"]
             _time = content["time"]
             send_message(sender, receiver, _time)
            #没有数据库插入好友请求历史
            #TODO
        except Exception as e:
            print("服务端处理加好友失败: " + str(e))
        


def send_message(sender, receiver, _time):
    addfriend_msg = {
        "type": "user_addfriend",
        "back_data": None,
        "content": {
            "sender": sender,
            "receiver": receiver,
            "time": _time
        }
    }
    json_message = json.dumps(addfriend_msg).encode('utf-8')
    if receiver in online_clients:
        receiver_socket, _ = online_clients[receiver]
        receiver_socket.sendall(json_message)
    else:
        user_addfriendlist[receiver].append(json_message)



