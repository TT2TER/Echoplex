import socket
import json
from db.table_user import *


def user_register(data, client_socket, address, database):
    print('收到注册信息')
    userid = data["content"]["userid"]
    username = data["content"]["username"]
    userpwd = data["content"]["userpwd"]
    email = data["content"]["email"]


    print('id:' + userid)
    print('pwd:' + userpwd)

    # 把数据放进数据库什么的
    insert_table_user(database, "user", userid, username, userpwd, email,)

    back_data = {
        "register_back": "0000"
    }
    json_back_data = json.dumps(back_data).encode('utf-8')
    client_socket.sendall(json_back_data)
    return 0
