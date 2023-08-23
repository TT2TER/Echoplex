

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
                  "chat_time datatime,"
                  "chat_content text)")
        con.commit()
        print("table is created")
        return True
    except:
        print("table "+table_name+" is already exists")
        return False


def insert_table_user_chat(con,table_name,chat_id,sender_id,reciever_id,chat_time,chat_content):
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
