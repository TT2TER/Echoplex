from db import *
import json

def group_list(received_data, socket, address, database):
    print(received_data)
    user_id=received_data['content']['owner']

    results=select_table(database,"group_member",member_id=user_id)
    re=[]
    if results:
        for group_id,member_id in results:
            ret=select_table(database,"[group]",group_id=group_id)
            re.append((group_id,ret[0][1]))

        back_data={
            'type':"group_list",
            'back_data':"0012",
            'content':{
                'group_list_info':re,
            }
        }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        print("群组列表获取成功")

    else:
        back_data = {
            'type': "group_list",
            'back_data': "0013",
            'content': {
                'group_list_info': []
            }
        }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        print("No group found for user", user_id)
