from db.table_group import *
from db.table_chat import *
from db.table_group_member import *
from db.DataDB import *
import json
from global_data import online_clients,user_mailboxes

# from global_data import online_clients

def save_new_groupid(new_groupid):
    with open("new_groupid.txt", "w") as file:
        file.write(str(new_groupid))


# Load new_groupid from the file
def load_new_groupid():
    try:
        with open("new_groupid.txt", "r") as file:
            return int(file.read())
    except FileNotFoundError:
        return 20000  # Default starting value if the file doesn't exist


def create_group(data, socket, address, database):

    print("##########")

    try:
        content = data['content']
        group_manager = content['group_manager']
        group_name = content['group_name']
        group_member = content['group_member']
        group_create_time=content['group_create_time']
        group_image=content['group_image']

        if group_manager not in group_member:
            group_member.append(group_manager)

        new_groupid = load_new_groupid() + 1
        group_id = new_groupid
        group_table_name = "[group]"
        group_member_table_name = "group_member"
        print(group_id)
        succ = insert_table_group(database, group_table_name,group_id,group_name,group_manager,group_create_time,group_image)
        if not succ:
            print("创建群表" + group_table_name + "失败")
        
        for member_id in group_member:
            if succ:
                succ=insert_table_group_member(database,group_member_table_name,group_id,member_id)
            else:
                print("插入群成员" + str(member_id) + "失败")
                break

    except KeyError as e:
        print("Error: Missing key in data content -", e)
        # You might want to send an error response back to the client/socket here.
    except Exception as e:
        print("An error occurred:", e)
        # Handle any other unexpected exceptions here.
    else:
        print("Group creation successful")
    finally:
        if succ:
            back_data = {
                "type": "create_group",
                "back_data": "0000",    #0000代表成功
                'content':{
                    'succ':succ,
                    'group_id':group_id,
                    'group_name':group_name,
                    'group_manager':group_manager,
                    'group_member':group_member,    #List
                }
            }
            save_new_groupid(new_groupid)
            back_json_data = json.dumps(back_data).encode('utf-8')
            socket.sendall(back_json_data)
#            receivers = search_member(database, "chat", group_id)
            print("----------------")
            for receiver in group_member:
                if receiver in online_clients:
                    receiver_socket, _ = online_clients[receiver]
                    receiver_socket.send(back_json_data)
#                else:
#                    user_mailboxes[receiver].append(back_json_data)
        else:
            new_groupid -= 1
            back_data = {
                "type": "create_group",
                "back_data": "0001",    #0001代表失败
                'content':{
                    'succ':succ,
                }
            }
            save_new_groupid(new_groupid)
            back_json_data = json.dumps(back_data).encode('utf-8')
            socket.sendall(back_json_data)


def delete_group(data, socket, address, database):
    try:
        content = data['content']
        group_id=content['group_id']
        sender_id=content['sender']
        manager_id=select_table(database,"[group]",group_id=group_id)[0][2]
        members=search_member(database,"group_member",group_id=group_id)
        if sender_id==manager_id:
            succ=delete_table_index(database,"[group]",group_id=group_id)
            delete_table_index(database,"group_member",group_id=group_id)
            delete_table_index(database,"chat",chat_id=group_id)
        else:
            succ=False
            print("非管理员无法解散群")
    except Exception as e:
        print("An error occurred:", e)
    finally:
        if succ == True:
            back_data={
                'type':'delete_group',
                'back_data':"0002",
                'content':{
                    'succ':succ,
                    'group_id':group_id,
                    'sender_id':sender_id,
                }
            }
            back_json_data = json.dumps(back_data).encode('utf-8')
            for member_id in members:
                if member_id in online_clients:
                    receiver_socket, _ = online_clients[member_id]
                    receiver_socket.send(back_json_data)
        
        else:
            back_data={
                'type':'delete_group',
                'back_data':"0003",
                'content':{
                    'succ':succ,
                    'group_id':group_id,
                    'sender_id':sender_id,
                }
            }
            back_json_data = json.dumps(back_data).encode('utf-8')
            socket.sendall(back_json_data)

def add_new_member(data, socket, address, database):
    try:
        content = data['content']
        group_id = content['group_id']
        member_id = content['member_id']
#        group_name=content['group_name']
        ret=select_table(database,"[group]",group_id=group_id)
        group_name=ret[0][1]
        for i in member_id:
            succ = insert_table_group_member(database,"group_member", group_id, i)

    except Exception as e:
        print("An error occurred:", e)
    finally:
        if succ:
            back_data={
                'type':'add_new_member',
                'back_data':"0000",
                'content':{
                    'group_id':group_id,
                    'group_name':group_name,
                }
            }
            back_json_data = json.dumps(back_data).encode('utf-8')
#            socket.sendall(back_json_data)
            for member_id in member_id:
                if member_id in online_clients:
                    receiver_socket, _ = online_clients[member_id]
                    receiver_socket.send(back_json_data)                    
        else:
            pass


