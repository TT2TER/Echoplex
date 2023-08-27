import json
from db.DataDB import *
from db.table_user_friend import *
from db.table_relation import *

def user_del_friend(received_data, socket, address, database):
    try:
        friend_id = received_data["content"]['friend_id']
        user_id = received_data["content"]['user_id']
        delete_table_index(database,"user_friend",user_id=min(user_id,friend_id),friend_id=max(friend_id,user_id))
        delete_table_index(database,"relation",user_id=user_id,friend_id=friend_id)  
        delete_table_index(database,"relation",user_id=friend_id,friend_id=user_id)   
        print("删除好友成功") 
    except Exception as e:
        print("删除数据库好友信息失败 " + str(e))