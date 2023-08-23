import sqlite3 as sql
from sqlite3 import Error
# from table_user import *
# from table_user_friend import *
# from table_user_chat import *


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



def create_table_group(con,table_name="group"):
    """
    群聊表：
    group_id : 群聊编号
    group_name : 群聊名
    group_leader_id : 群主编号
    group_image : 群头像

    return:
    True : 创建成功    False : 创建失败
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
        return True
    except:
        print("table "+table_name+" is already exists")
        return False


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
        return True
    except:
        print("table "+table_name+" is already exists")
        return False

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
        return True
    except:
        print("table "+table_name+" is already exists")
        return False


def insert_table_group(con,table_name,id,name,image,leader_id):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (group_id,group_name,group_leader_id,create_time,group_image) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(id,name,image,leader_id))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Error")
        con.rollback()
        return False

def select_table(con,table_name,**kwargs):
    """
    任意表查询：
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
            sql=sql+key+"="+str(value)
            flag=1
        cursor.execute(sql)
        ret=cursor.fetchall()
        return ret
    except:
        print("Select Failed")
        return None
    
def delete_table_index(con,table_name,**kwargs):
    """
    任意表的元组删除：
    table_name : 需要删除元组所在表
    **kwargs : 删除条件
    """
    cursor=con.cursor()
    try:
        sql="DELETE FROM "+table_name+" WHERE "
        flag=0
        for key,value in kwargs.items():
            if flag==1:
                sql=sql+" AND "
            print(key,value)
            sql=sql+key+"="+str(value)
            flag=1
        cursor.execute(sql)
        con.commit()
        print("Successfully Deleted")
        return True
    except:
        print("Delete Failed")
        con.rollback()
        return False


def delete_table(con,table_name):
    """
    任意表的删除：
    table_name : 需要删除的表
    """
    cursor=con.cursor()
    try:
        sql="DROP TABLE "+table_name
        cursor.execute(sql)
        con.commit()
        print("Table "+table_name+" is deleted")
        return True
    except:
        print("Deleted Failed")
        con.rollback()
        return False

'''

insert_table_user(con,table_name,id=1004,name="xa",pwd="123456",email="12@qq.com",image="path/to/image")
select_table(con,table_name,user_name="'xa'",user_id=1004)
delete_table_index(con,table_name,user_id=1004,user_name="'xa'")

#insert_table_user(con,table_name,id=1002,name="xa",pwd="123456",email="12@qq.com",image="path/to/image")
update_table_user(con,table_name=table_name,id=1002,index='user_email',value='1234@qq.com')
a=select_table_user(con,table_name,user_name="'xa'",user_id=1002)
print(a)
con=sql_connection()
table_name="user_friend"
#create_table_user_friend(con,table_name)
#insert_table_user_friend(con,table_name,user_id=1002,friend_id=1004,chat_id=1000002)
ret=select_table(con,table_name,user_id=1005)
print(ret)
if ret:
    print("chat")
else:
    print("no")
con.close()

'''

