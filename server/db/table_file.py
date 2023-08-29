

def create_table_file(con,table_name="file"):
    """
    文件表：                    （包括群聊和私聊）
    chat_id : 聊天表编号
    sender_id : 文件发送者编号
    chat_time : 文件发送时间    datetime.now()
    filepath : 传输的文件
    filesize : 文件大小
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "sender_id INT,"
                  "chat_id INT,"
                  "chat_time FLOAT,"
                  "filepath text,"
                  "filesize INT,"
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



def insert_table_file(con,table_name,sender_id,chat_id,chat_time,filename,filesize):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (sender_id,chat_id,chat_time,filepath,filesize) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(sender_id,chat_id,chat_time,filename,filesize))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Error")
        con.rollback()
        return False