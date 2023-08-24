import sqlite3 as sql
from sqlite3 import Error
from table_user import *
from table_user_friend import *
from table_user_chat import *
from table_group import *
from table_group_member import *
from table_group_chat import *

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

def select_table(con,table_name,**kwargs):
    """
    任意表查询：
    table_name : 需要查询的表
    **kwargs : 查询条件（例如：user_name="'xa'"和user_id=1002）

    返回 一个用户所有信息
    如果查询错误或者SQL语句错误   返回None
    如果返回[]   则代表查询成功但无结果
    [] 中是一个个元组
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


#create_table_user_friend(con,table_name)
#insert_table_user_friend(con,table_name,user_id=1002,friend_id=1004,chat_id=1000002)

print(ret)
if ret:
    print("chat")
else:
    print("no")
con.close()
con=sql_connection()
con1=sql_connection()
con2=sql_connection()
table_name="user_friend"
ret=select_table(con2,table_name,user_id=1002)
print(ret)
'''
