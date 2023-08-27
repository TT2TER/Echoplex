from db.DataDB import *

def create_view_chat(con,view_name="view_chat"):
    """
    创建视图
    """
    
    cursor=con.cursor()
    sql="CREATE VIEW "+view_name+" (chat_id,sender_id,chat_time,chat_content) AS SELECT chat_id,sender_id,MAX(chat_time),chat_content FROM table_chat GROUP BY chat_id ORDER BY MIN(chat_time) DESC"
    try:
        cursor.execute(sql)
        con.commit()
        print("view is created")
        return True
    except:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='view' AND name=?", (view_name,))
        result = cursor.fetchone()
        if result:
            print("table "+view_name+" is already exists")
        else:
            print("Create Table Failed")
        return False
    


def search_sequence(con,user_id,view_name="view_chat"):
    """
    拉取聊天列表：
        input:
            user_id : 用户ID
        output : 按时间从后到先的顺序输出一个列表chat
            chat : (chat_id,sender_id,chat_time,chat_content)
    """
    
    chat_id_list=[]
    friend1=select_table(con,table_name="user_friend",user_id=user_id)
    if friend1:
        for user_id,friend_id,chat_id in friend1:
            chat_id_list.append(chat_id)
    friend2=select_table(con,table_name="user_friend",friend_id=user_id)
    if friend2:
        for user_id,friend_id,chat_id in friend2:
            chat_id_list.append(chat_id)
    g=select_table(con,table_name="group_member",member_id=user_id)
    if g:
        for group_id,member_id in g:
            chat_id_list.append(group_id)
    cursor=con.cursor()
    print(chat_id_list)
    sql="SELECT * FROM "+view_name+" WHERE chat_id="
    try:
        chat=[]
        for chat_id in chat_id_list:
            print(sql+str(chat_id))
            cursor.execute(sql+str(chat_id))
            ret=cursor.fetchone()
            if ret:
                chat.append(ret)
        return chat
    except:
        print("Search Failed")
        return None
