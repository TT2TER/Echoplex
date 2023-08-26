

def create_table_group_member(con,table_name="group_member"):
    """
    群成员表：              （主要用于群成员界面）
    group_id : 群编号
    member_id : 成员编号
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "group_id INTEGER,"
                  "member_id INTEGER,"
                  "PRIMARY KEY(group_id,member_id))")
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
    

def insert_table_group_member(con,table_name,group_id,member_id):
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (group_id,member_id) VALUES(?,?)"
        cursor.execute(sql,(group_id,member_id))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Failed")
        con.rollback()
        return False