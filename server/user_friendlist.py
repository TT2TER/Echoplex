import json
from db.DataDB import select_table
from db.table_user_friend import *
import sqlite3 as sql
from sqlite3 import Error

def user_friendlist(received_data, socket, address, database):
    #获取好友列表
    select_table(database,"user_friend",user_id=received_data["user_id"])
    
    #TODO:
