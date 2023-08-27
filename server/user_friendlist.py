import json
from db.DataDB import *
from db.table_user_friend import *
import sqlite3 as sql
from sqlite3 import Error

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
        back_data = {
            'type': "user_friendlist",
            'back_data': "0012",
            'content': {
                'friend_ids': results
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


