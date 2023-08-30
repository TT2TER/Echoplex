from tool_fuction import find_friend_id
from global_data import online_clients
from db.DataDB import *
import json


def user_video_chat(received_data, socket, address, database):
    """
    收到的data
    data = {
            "type": "user_video_chat",
            "content": {
                "user_id": self.user_id,
                "chat_id": chat_id,
                "time": timestamp
            }
        }
    """
    content = received_data['content']
    user_id = content['user_id']
    chat_id = content['chat_id']
    receiver_id = find_friend_id(user_id, chat_id)
    content['receiver_id'] = receiver_id
    _, user_address = online_clients[user_id]
    user_ip, _ = user_address
    content['user_ip'] = user_ip
    """
    data = {
            "type": "user_video_chat",
            "content": {
                "user_id": self.user_id,
                "chat_id": chat_id,
                "time": timestamp,
                "receiver_id":,
                "receiver_ip":,
                "user_ip":,
                "username"
            }
        }
    """
    # 如果对方在线，给对方发
    if receiver_id in online_clients:
        receiver_socket, receiver_address = online_clients[receiver_id]
        receiver_ip, _ = receiver_address
        ret = select_table(database, "user", user_id=user_id)
        if len(ret) != 0:
            content['username'] = ret[0][1]
            content['receiver_ip'] = receiver_ip
            data = {
                "type": "user_video_chat",
                "back_data": "0000",
                "content": content
            }
        json_data = json.dumps(data).encode('utf-8')
        receiver_socket.sendall(json_data)
    # 不在线，给聊天发起者发
    else:
        # 对方不在线或者该用户不存在
        data = {
            "type": "user_video_chat",
            "back_data": "0001",
            "content": None
        }
        json_data = json.dumps(data).encode('utf-8')
        socket.sendall(json_data)


