

def create_table_group(con,table_name="[group]"):
    """
    群聊表：                                    注：group为关键字，需要输入[group]
    group_id : 群聊编号
    group_name : 群聊名
    group_leader_id : 群主编号
    group_image : 群头像的路径

    return:
    True : 创建成功    False : 创建失败
    """

    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "group_id INT PRIMARY KEY,"
                  "group_name text,"
                  "group_leader_id INT UNIQUE,"
                  "create_time FLOAT,"
                  "group_image text)")
        con.commit()
        print("table is created")
        return True
    except Exception as e:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name=?", (table_name,))
        result = cursor.fetchone()
        if result:
            print("table "+table_name+" is already exists")
        else:
            print("Create Table Failed")
            print(e)
        return False
    


def insert_table_group(con,table_name,group_id,group_name,group_leader_id,create_time,group_image):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (group_id,group_name,group_leader_id,create_time,group_image) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(group_id,group_name,group_leader_id,create_time,group_image))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Failed")
        con.rollback()
        return False
    

def update_table_group(con,table_name,id,index, value):
    """
    群聊表更新            输入：
    table_name : 操作的表名
    id : 需要更新信息的群聊的ID
    index : 需要更新的选项（例如pwd和email）    注：前面需要加uer_
    value : 更新的值
    """
    cursor=con.cursor()
    try:
        sql="UPDATE "+ table_name +" set "+index+"=? where user_id=?"
        cursor.execute(sql,(value,id))
        con.commit()
        print("Successfully Update")
        return True
    except:
        print("Update Failed")
        con.rollback()
        return False