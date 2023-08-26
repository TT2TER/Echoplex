

def create_table_user_chat(con,table_name="user-chat"):
    """
    用户聊天表：
    chat_id : 聊天表编号
    sender_id : 信息发送者编号
    reciever_id : 信息接受者编号
    chat_time : 信息发送时间
    chat_content : 信息内容
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "chat_id INT,"
                  "sender_id INT, "
                  "reciever_id INT, "
                  "chat_time datetime,"
                  "chat_content text)")
        con.commit()
        print("table is created")
        return True
    except:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        if result:
            print("table "+table_name+" is already exists")
        else:
            print("Create Table Failed")
        return False


def insert_table_user_chat(con,table_name,chat_id,sender_id,reciever_id,chat_time,chat_content):
    """
    添加聊天信息：
    chat_id : 聊天框ID
    sender_id : 信息发送者ID
    reciever_id : 信息接收者ID
    chat_time : 发送时间
    chat_content : 信息内容

    """
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (chat_id,sender_id,reciever_id,chat_time,chat_content) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(chat_id,sender_id,reciever_id,chat_time,chat_content))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Error")
        con.rollback()
        return False
