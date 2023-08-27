from db import *
from datetime import datetime



con=sql_connection()
cursor=con.cursor()
table_name1="user"
table_name2="relation"
create_table_user(con,table_name1)
create_table_relation(con,table_name2)

insert_table_user(con,table_name1,user_id=1001,user_name="xa",user_email="123456@qq.com",user_pwd="123456",user_image="/path/to/image")
insert_table_user(con,table_name1,user_id=1002,user_name="xb",user_email="123456@qq.com",user_pwd="123456",user_image="/path/to/image")
insert_table_user(con,table_name1,user_id=1003,user_name="xc",user_email="123456@qq.com",user_pwd="123456",user_image="/path/to/image")

sqlc="SELECT * FROM user WHERE user_id=?"
cursor.execute(sqlc,(1001,))
r=cursor.fetchall()
print(r)


insert_table_relation(con,table_name=table_name2,user_id=1001,friend_id=1002,relation="star")
insert_table_relation(con,table_name=table_name2,user_id=1001,friend_id=1003,relation="bad")
ret=search_relation(con,user_id=1001,relation="bad",table_name=table_name2)
print(ret)

delete_table(con,table_name1)
delete_table(con,table_name2)

