import socket
import json
import threading
import sqlite3
from db.DataDB import select_table
from global_data import online_clients
from user_chat import retrieve_messages


def user_login(data, socket, address, con):
    content = data["content"]
    res = select_table(con, "user", user_id=int(content["user_id"]))  # id为int型
    if len(res) == 0:  # 未注册，返回空列表
        back_data = {
            "type": "user_login",
            'back_data': "0002"
        }
        result = "该用户未注册"
    else:
        if content["user_pwd"] == res[0][2]:
            back_data = {
                "type": "user_login",
                'back_data': "0003"
            }
            result = "成功"
            # 登录成功，维护在线用户表
            online_clients[int(data["content"]["user_id"])] = (socket, address)
            # retrieve_messages(content['user_id'])
        else:
            back_data = {
                "type": "user_login",
                'back_data': "0004"
            }
            result = "密码大概是错了"
    back_json_data = json.dumps(back_data).encode('utf-8')
    socket.sendall(back_json_data)
    return result
