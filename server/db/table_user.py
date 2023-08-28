

def create_table_user(con, table_name="user"):
    """
    用户表：
    user_id : 用户编号
    user_name : 用户姓名
    user_pwd : 用户密码
    user_email : 邮箱
    user_image : 用户头像二进制文件
    """
    cursor=con.cursor()
    try:
        cursor.execute("CREATE TABLE "+ table_name+" ("
                  "user_id INT PRIMARY KEY,"
                  "user_name text,"
                  "user_pwd text,"
                  "user_email text,"
                  "user_image text)")
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


def insert_table_user(con,table_name,user_id,user_name,user_pwd,user_email,user_image):
    """
    用户表添加：
    user_id : 用户ID
    user_name : 用户名
    user_pwd : 用户密码
    user_email : 用户邮箱
    user_iamge : 用户头像图片路径
    """
    cursor=con.cursor()
    try:
        sql="INSERT INTO "+table_name+" (user_id,user_name,user_pwd,user_email,user_image) VALUES(?,?,?,?,?)"
        cursor.execute(sql,(user_id,user_name,user_pwd,user_email,user_image))
        con.commit()
        print("Successfully Insert")
        return True
    except:
        print("Insert Error")
        con.rollback()
        return False

def update_table_user(con,table_name,id,index, value):
    """
    用户表更新            输入：
    table_name : 操作的表名
    id : 需要更新信息的用户的ID
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

