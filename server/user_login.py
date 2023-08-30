import json
import hashlib
from db.DataDB import select_table
from global_data import online_clients
from user_chat import retrieve_messages
import jwt
import datetime
import rsa
from tool_fuction import load_keys

secret_key = "FluppyFR_Asuna"  # 服务器的密钥


def get_token(user_id, user_pwd):
    payload = {
        "user_id": user_id,
        "user_pwd": user_pwd,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=3)  # 令牌有效期
    }
    # secret_key = "FluppyFR_Asuna"  # 服务器的密钥
    token = jwt.encode(payload, secret_key, algorithm="HS256")
    return token


def verify_token(request_token, secret_key):
    try:
        decoded_payload = jwt.decode(request_token, secret_key, algorithms=["HS256"])
        return decoded_payload
    except jwt.ExpiredSignatureError:
        # 令牌已过期
        return None
    except jwt.DecodeError:
        # 令牌验证失败
        return None


# 在请求中提取令牌并验证


def user_login(data, socket, address, con):
    content = data["content"]
    request_token = content["token"]
    if request_token is not None:
        decoded_payload = verify_token(request_token, secret_key)
        if decoded_payload:
            user_id = decoded_payload["user_id"]
            print(f"user_id is {user_id}")
            res = select_table(con, "user", user_id=int(user_id))
            user_pwd = decoded_payload["user_pwd"]
            print(f"Authenticated user: {user_pwd} (ID: {user_id})")
            token_login = True
            back_data = {
                "type": "user_login",
                'back_data': "0003",
                'content': {
                    'user_name': res[0][1],
                    'user_id': user_id
                }
            }
        else:
            back_data = {
                "type": "user_login",
                'back_data': "0005",
                'content': None
            }
            print("Token is invalid or expired.")
            token_login = False
    else:
        res = select_table(con, "user", user_id=int(content["user_id"]))  # id为int型
        if len(res) == 0:  # 未注册，返回空列表
            back_data = {
                "type": "user_login",
                'back_data': "0002",
                'content': None
            }
            result = "该用户未注册"
        else:
            user_pwd = content["user_pwd"]
            # hashed_user_pwd = hashlib.sha256(user_pwd.encode('utf-8')).hexdigest()
            # 用哈希加密就不能找回密码了，改成RSA加密
            pubkey, privkey = load_keys()
            # rsa生成的密文有随机性，解密了再比较
            res_pwd = rsa.decrypt(res[0][2], privkey).decode()
            # print(res[0][2])
            # print(hashed_user_pwd)
            # print(res[0][2])
            # print(rsa_pwd)
            if user_pwd == res_pwd:
                # 不能用rsa来get_token，先解码
                token = get_token(int(data["content"]["user_id"]), res_pwd)
                print(type(token))
                back_data = {
                    "type": "user_login",
                    'back_data': "0003",
                    'content': {
                        'user_id': int(data['content']['user_id']),
                        'user_name': res[0][1],
                        'token': token
                    }
                }
                result = "用户名密码登录成功"
                # 登录成功，维护在线用户表
                online_clients[int(data["content"]["user_id"])] = (socket, address)
                # retrieve_messages(content['user_id'])
            else:
                back_data = {
                    "type": "user_login",
                    'back_data': "0004",
                    'content': {
                        'user_id': int(data['content']['user_id'])
                    }
                }
                result = "密码大概是错了"
    back_json_data = json.dumps(back_data).encode('utf-8')
    socket.sendall(back_json_data)
    return result
