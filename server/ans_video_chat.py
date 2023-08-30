import json
from global_data import online_clients


# 视频请求应答处理类似于好友请求，在线直接发送请求，离线不管


def ans_video_chat(received_data, socket, address, database):
    content = received_data["content"]
    back_data_video_chat = {
        "type": "ans_video_chat",
        "back_data": None,
        "content": content
    }
    user_id = content['user_id']
    json_message = json.dumps(back_data_video_chat).encode('utf-8')
    if user_id in online_clients:
        user_socket, _ = online_clients[user_id]
        user_socket.sendall(json_message)
    else:
        # 发起视频的人下线，此贴终结
        pass
