import socket
import json
from db.table_user import *


def user_register(data, socket, address, database):
    print('收到注册信息')
    userid = data["content"]["user_id"]
    username = data["content"]["user_name"]
    userpwd = data["content"]["user_pwd"]
    email = data["content"]["user_email"]
    image = data["content"]["user_image"]

    print('id:' + userid)
    print('pwd:' + userpwd)

    # 把数据放进数据库什么的
    try:
        # 判断和限制用户名密码等
        succ = insert_table_user(database, "user", userid, username, userpwd, email, image)
        if succ:
            back_data = {
                "back_data": "0000"
            }
            res = "Success"
        else:
            back_data = {
                "back_data": "0001"
            }
            res = "Failed"
    except:
        res = "失败"
        back_data = {
            "back_data": "0001"
        }
    finally:
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        return res
