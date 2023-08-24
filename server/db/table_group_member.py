

def create_table_group_member(con,table_name="group-member"):
    """
    群成员表：              （主要用于群成员界面）
    group_id : 群编号
    member_id : 成员编号
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "group_id INTEGER,"
                  "member_id INTEGER)")
        con.commit()
        print("table is created")
        return True
    except:
        print("table "+table_name+" is already exists")
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