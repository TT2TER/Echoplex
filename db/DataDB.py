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
    user_pwd : 用户密码
    user_email : 邮箱
    user_image : 用户头像路径
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "user_id INT PRIMARY KEY,"
                  "user_name text,"
                  "user_pwd text,"
                  "user_email text,"
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
    group_image : 群头像
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
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
    chat_id : 用户单聊天编号
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "user_id INT,"
                  "friend_id INT,"
                  "chat_id INT)")
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
        cursor.execute("CREATE TABLE "+ table_name+" ("
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
        cursor.execute("CREATE TABLE "+ table_name+" ("
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
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "group_id INTEGER,"
                  "member_id INTEGER)")
        con.commit()
        print("table is created")
    except:
        print("table "+table_name+" is already exists")


def insert_table_user(con,table_name,id,name,pwd,email,image):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (user_id,user_name,user_pwd,user_email,user_image) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(id,name,pwd,email,image))
        con.commit()
        print("Successfully Insert")
    except:
        print("Insert Error")
        con.rollback()

def insert_table_group(con,table_name,id,name,image,leader_id):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (group_id,group_name,group_leader_id,create_time,group_image) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(id,name,image,leader_id))
        con.commit()
        print("Successfully Insert")
    except:
        print("Insert Error")
        con.rollback()

def insert_table_user_friend(con,table_name,user_id,friend_id,chat_id):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+"(user_id,friend_id,chat_id) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(user_id,friend_id,chat_id))
        con.commit()
        print("Successfully Insert")
    except:
        print("Insert Failed")
        con.rollback()


def update_table_user(con,table_name,id,index, value):
    """
    用户表更新            输入：
    table_name : 操作的表名
    id : 需要更新信息的用户的ID
    index : 需要更新的选项（例如pwd和email）    注：前面需要加uer_
    value : 更新的值
    """
    cursor=con.cursor()
    try:
        sql="UPDATE "+ table_name +" set "+index+"=? where user_id=?"
        cursor.execute(sql,(value,id))
        con.commit()
        print("Successfully Update")
    except:
        print("Update Failed")
        con.rollback()

def select_table_user(con,table_name,**kwargs):
    """
    用户表查询：
    table_name : 需要查询的表
    **kwargs : 查询条件（例如：user_name="'xa'"和user_id=1002）

    返回 一个用户所有信息
    """
    cursor=con.cursor()
    try:
        sql="SELECT * FROM "+table_name+" WHERE "
        flag=0
        for key,value in kwargs.items():
            if flag==1:
                sql=sql+" AND "
            print(key,value)
            sql=sql+key+"="+str(value)
            flag=1
        print(sql)
        cursor.execute(sql)
        ret=cursor.fetchone()
        return ret
    except:
        print("Select Failed")
        return None
#def select_table_user(con,)
'''
con=sql_connection()
table_name="user"
create_table_user(con,table_name)
#insert_table_user(con,table_name,id=1002,name="xa",pwd="123456",email="12@qq.com",image="path/to/image")
update_table_user(con,table_name=table_name,id=1002,index='user_email',value='1234@qq.com')
a=select_table_user(con,table_name,user_name="'xa'",user_id=1002)
print(a)
con.close()
'''

