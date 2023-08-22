import sqlite3 as sql
from sqlite3 import Error

def sql_connection(database_name="testDB.db"):
    """
    链接数据库：
    database_name : 需要被连接的数据库
    """
    try:
        con=sql.connect(database_name)
        print("Connection is established")
    except Error:
        print(Error)
    return con

def create_table_user(con, table_name="user"):
    """
    用户表：
    user_id : 用户编号
    user_name : 用户姓名
    user_image : 用户头像路径
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE"+ table_name+"("
                  "user_id INT PRIMARY KEY,"
                  "user_name text,"
                  "user_image text)")
        con.commit()
        print("table is created")
    except:
        print("table "+table_name+" is already exists")

def create_table_group(con,table_name="group"):
    """
    群聊表：
    group_id : 群聊编号
    group_name : 群聊名
    group_leader_id : 群主编号
    create_time : 建群时间
    group_image : 群头像
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE"+ table_name+"("
                  "group_id INT PRIMARY KEY,"
                  "group_name text,"
                  "group_leader_id INT UNIQUE,"
                  "create_time datatime,"
                  "group_image text)")
        con.commit()
        print("table is created")
    except:
        print("table "+table_name+" is already exists")

def create_table_user_friend(con,table_name="user-group"):
    """
    用户好友关系表：        （主要用于好友界面）
    user_id : 用户编号
    friend_id : 好友编号
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE"+ table_name+"("
                  "user_id INT"
                  "friend_id INT)")
        con.commit()
        print("table is created")
    except:
        print("table "+table_name+" is already exists")

def create_table_user_chat(con,table_name="user-chat"):
    """
    用户聊天表：
    sender_id : 信息发送者编号
    reciewer_id : 信息接受者编号
    chat_time : 信息发送时间
    chat_content : 信息内容
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE"+ table_name+"("
                  "sender_id INT, "
                  "reciewer_id INT, "
                  "chat_time datatime,"
                  "chat_content text,")
        con.commit()
        print("table is created")
    except:
        print("table "+table_name+" is already exists")

def create_table_group_chat(con,table_name="group-chat"):
    """
    群聊天表：
    sender_id : 信息发送者编号
    group_id : 信息所在群编号
    chat_time : 信息发送时间
    chat_content : 信息内容 
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE"+ table_name+"("
                  "sender_id INTEGER ,"
                  "group_id INTEGER,"
                  "chat_time datatime,"
                  "chat_content text")
        con.commit()
        print("table is created")
    except:
        print("table "+table_name+" is already exists")

def create_table_group_member(con,table_name="group-member"):
    """
    群成员表：              （主要用于群成员界面）
    group_id : 群编号
    member_id : 成员编号
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE"+ table_name+"("
                  "group_id INTEGER,"
                  "member_id INTEGER)")
        con.commit()
        print("table is created")
    except:
        print("table "+table_name+" is already exists")
"""
con=sql_connection()
table_name="user"
create_table_user(con,table_name)


con.close()
"""
