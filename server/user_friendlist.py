import json
from db.DataDB import *
from db.table_user_friend import *
import sqlite3 as sql
from sqlite3 import Error
from db.table_user import *

def user_friendlist(received_data, socket, address, database):
    #获取好友列表
    user_id = received_data['content']['user_id']
    #cursor = database.cursor()
    #sql = "SELECT friend_id FROM user_friend WHERE user_id = ? OR SELECT user_id FROM user_friend WHERE friend_id = ?"
    # 查询给定用户的所有好友
    #cursor.execute(sql, (user_id,user_id))
    #results = cursor.fetchall()
    results = search_firend(database,user_id,"user_friend")
    
    if results:
        #friend_ids = [row[0] for row in results]
        #查询id对应的昵称，将返回值组织成一个（id，name）的list
        newre = []
        for i in results:
             re = select_table(database,"user",user_id=i)
             name = re[0][1]
             newre[i]=(i,name)
        #查询id对应的分组，将返回值组织成一个（id,name,partition)的list
        
        for j in results:
            re = select_table(database,"table_relation",user_id=j)
            partition = re[0][2]
            newre[j] = (j,name,partition)
        back_data = {
            'type': "user_friendlist",
            'back_data': "0012",
            'content': {
                'friend_ids': newre
            }
        }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        print("好友列表获取成功")
    else:
        back_data = {
            'type': "user_friendlist",
            'back_data': "0013",
            'content': {
                'friend_ids': []
            }
        }
        back_json_data = json.dumps(back_data).encode('utf-8')
        socket.sendall(back_json_data)
        print("No friends found for user", user_id)


