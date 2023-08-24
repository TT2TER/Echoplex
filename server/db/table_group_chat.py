


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
    


def insert_table_group_chat(con,table_name,sender_id,group_id,chat_time,chat_content):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (sender_id,group_id,chat_time,chat_content) VALUES(?,?,?,?)"
        cursor.execute(sql,(sender_id,group_id,chat_time,chat_content))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Error")
        con.rollback()
        return False