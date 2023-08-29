from db import *
from datetime import datetime
from time import sleep
con=sql_connection()
def time():
    now=datetime.now()
    return datetime.timestamp(now)
"""
delete_table(con,"chat")
delete_view(con,"view_chat")
delete_table(con,"user_friend")
delete_table(con,"group")
delete_table(con,"group_member")

create_table_chat(con,"chat")
create_view_chat(con,)
create_table_user_friend(con,)
create_table_group(con,)
create_table_group_member(con,)



insert_table_user_friend(con,"user_friend",10001,10002,1000110002)
insert_table_group(con,"group",20001,"xx",10001,time(),"")
insert_table_group_member(con,"group_member",20001,10001)
insert_table_group_member(con,"group_member",20002,10001)

insert_table_chat(con,10001,1000110002,time(),"aaaa",table_name="chat")
sleep(0.2)
insert_table_chat(con,10001,20002,time(),"bbbb",table_name="chat")
sleep(0.2)
insert_table_chat(con,10001,20001,time(),"cccc",table_name="chat")

ret=search_sequence(con,10001,)
print(ret)

delete_view(con,"view_chat")
"""



create_table_file(con,"file")
insert_table_file(con,"file",10001,20001,time(),"/path/to/file",100*1024*1024)

delete_table(con,"file")
