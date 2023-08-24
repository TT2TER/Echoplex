import json
from db.table_user import *

global new_userid


# Save new_userid to a file
def save_new_userid(new_userid):
    with open("new_userid.txt", "w") as file:
        file.write(str(new_userid))


# Load new_userid from the file
def load_new_userid():
    try:
        with open("new_userid.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 10000  # Default starting value if the file doesn't exist


def user_register(data, socket, address, database):
    print('收到注册信息')
    global new_userid
    new_userid = load_new_userid() + 1
    userid = new_userid
    username = data["content"]["user_name"]
    userpwd = data["content"]["user_pwd"]
    email = data["content"]["user_email"]
    image = data["content"]["user_image"]

    print('id:' + str(userid))
    print('pwd:' + userpwd)

    # 把数据放进数据库什么的
    try:
        # 判断和限制用户名密码等
        succ = insert_table_user(database, "user", userid, username, userpwd, email, image)
        if succ:
            back_data = {
                "type": "user_register",
                "back_data": True,
                "user_id": userid
            }
        else:
            new_userid -= 1
            back_data = {
                "type": "user_register",
                "back_data": False,
            }
        save_new_userid(new_userid)
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        res = "成功"
    except:
        res = "失败"
    finally:
        return res
