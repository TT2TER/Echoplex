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