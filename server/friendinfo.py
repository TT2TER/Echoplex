import socket
import json
from .db.DataDB import *

def friendinfo(data, socket, address, con):
    res = select_table(con, "user", user_id = int(data["content"]["user_id"]) )    #id为int型
    if len(res) == 0:        #未注册，返回空列表
        back_data = {
            'back_data': "0003"
            }
        result = "Failed"
    else:
        back_data = {
         'back_data': "0002",
         'friendinfo': [res[0],res[1],res[3]]  #返回好友信息,分别是id,name,email
         }
        result = "Successful"
        
    back_json_data = json.dumps(back_data).encode('utf-8')
    socket.sendall(back_json_data)

    return result
  