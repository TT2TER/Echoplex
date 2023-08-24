import socket
import json
import threading
import sqlite3
from db.DataDB import select_table
from global_data import online_clients

def user_login(data, socket, address, con):

    res = select_table(con, "user", user_id = int(data["content"]["user_id"]) )    #id为int型
    if len(res) == 0:        #未注册，返回空列表
        back_data = {
            'back_data': "0003"
            }
        result = "Failed"
    else:
        if data["content"]["user_pwd"] == res[2]:
            back_data = {
                'back_data': "0002"
                }
            result = "Successful"
            online_clients[int(data["content"]["user_id"])] = socket
        else:
            back_data = {
                'back_data': "0003"
                }
            result = "Failed"
    back_json_data = json.dumps(back_data).encode('utf-8')
    socket.sendall(back_json_data)
    return result

        

   
