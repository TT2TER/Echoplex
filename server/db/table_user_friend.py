
"""
面向用户好友表
操作：创建表、插入值
无更新操作
"""

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
                  "chat_id INT,"
                  "PRIMARY KEY(user_id,friend_id))")
        con.commit()
        print("table is created")
        return True
    except:
        print("table "+table_name+" is already exists")
        return False


def insert_table_user_friend(con,table_name,user_id,friend_id,chat_id):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+"(user_id,friend_id,chat_id) VALUES(?,?,?)"
        cursor.execute(sql,(user_id,friend_id,chat_id))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Failed")
        con.rollback()
        return False

