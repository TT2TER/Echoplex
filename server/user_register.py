import socket
import json
from db.table_user import *


def user_register(data, socket, address, database):
    print('收到注册信息')
    userid = data["content"]["userid"]
    username = data["content"]["username"]
    userpwd = data["content"]["userpwd"]
    email = data["content"]["email"]
    image = data["content"]["image"]

    print('id:' + userid)
    print('pwd:' + userpwd)

    # 把数据放进数据库什么的
    try:
        # 判断和限制用户名密码等
        data = data["content"]
        succ = insert_table_user(database, "user_info", userid, username, userpwd, email, image)
        if succ:
            back_data = {
                "back_data": "0000"
            }
        else:
            back_data = {
                "back_data": "0001"
            }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        res = "成功"
    except:
        res = "失败"
    finally:
        return res
