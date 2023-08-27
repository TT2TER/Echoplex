from db.DataDB import *



def create_table_relation(con,table_name="table_relation"):
    """
    用户好友关系表：        （主要用于好友界面）
    user_id : 用户编号
    friend_id : 好友编号
    relation : 单向好友关系
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "user_id INT,"
                  "friend_id INT,"
                  "relation text,"
                  "PRIMARY KEY(user_id,friend_id))")
        con.commit()
        print("table "+table_name+" is created")
        return True
    except:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        if result:
            print("table "+table_name+" is already exists")
        else:
            print("Create Table Failed")
        return False


def insert_table_relation(con,user_id,friend_id,relation,table_name="table_relation"):
    """
    添加好友关系：
    user_id : 用户ID
    friend_id : 好友ID
    relation : 关系
    """
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+"(user_id,friend_id,relation) VALUES(?,?,?)"
        cursor.execute(sql,(user_id,friend_id,relation))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Failed")
        con.rollback()
        return False

def update_table_relation(con,table_name,user_id,friend_id,relation):
    cursor=con.cursor()
    try:
        sql="UPDATE "+table_name+" set relation =? where user_id=? AND friend_id=?"
        cursor.execute(sql,(relation,user_id,friend_id))
        con.commit()
        print("Successfully Update")
        return True
    except:
        print("Update Failed")
        con.rollback()
        return False

def search_relation(con,user_id,relation,table_name="table_relation"):
    """
    拉取用户关系
        input : 
            user_id : 本用户ID
            relation : 与该用户的关系
        output :
            ret : 与该用户具有该关系的好友的所有信息
    """
    cursor=con.cursor()
    try:
        information=[]
        rela=select_table(con,table_name,relation=relation,user_id=user_id)
        for user_id,friend_id,r in rela:
            ret=select_table(con,table_name="user",user_id=friend_id)
            information=information+ret
        return ret
    except Exception as e:
        print("Search Failed")
        print(e)
        return None

