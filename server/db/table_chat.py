

def create_table_chat(con,table_name="chat"):
    """
    聊天表：                    （包括群聊和私聊）
    chat_id : 聊天表编号
    sender_id : 信息发送者编号
    chat_time : 信息发送时间
    chat_content : 信息内容


    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "sender_id INT,"
                  "chat_id INT,"
                  "chat_time datetime,"
                  "chat_content text,"
                  "PRIMARY KEY(sender_id,chat_id,chat_time))")
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
    

def insert_table_chat(con,table_name,sender_id,chat_id,chat_time,chat_content):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (sender_id,chat_id,chat_time,chat_content) VALUES(?,?,?,?)"
        cursor.execute(sql,(sender_id,chat_id,chat_time,chat_content))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Error")
        con.rollback()
        return False