import socket
import json
import threading
from db.table_user import insert_table_user

def user_register(data, client_socket, address, database):
    res = ""
    try:
        #判断和限制用户名密码等
        data = data["content"]
        insert_table_user(database, "user_info", data["id"], data["name"], data["pwd"], data["email"], data["image"])

        back_data={
            "back_data": "0000"
        }
        back_json_data=json.dumps(back_data).encode('utf-8')
        client_socket.sendall(back_json_data)
        res = "0000"
    except:
        res = "0001"
    finally:
        return res
