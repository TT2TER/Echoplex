from db.table_group import *
from db.table_group_chat import *
from db.table_group_member import *
import json


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
    try:
        content = data['content']
        group_manager = content['group_manager']
        group_name = content['group_name']
        group_member = content['group_member']

        new_groupid = load_new_groupid() + 1
        group_id = new_groupid
        group_table_name = "group" + str(group_id)
        group_chat_table_name = "group_chat" + str(group_id)
        group_member_table_name = "group_member" + str(group_id)

        succ = create_table_group(database, group_table_name)
        if not succ:
            print("创建群表" + group_table_name + "失败")
        succ = create_table_group_chat(database, group_chat_table_name)
        if not succ:
            print("创建群聊天表" + group_chat_table_name + "失败")
        succ = create_table_group_member(database, group_member_table_name)
        if not succ:
            print("创建群成员表" + group_member_table_name + "失败")
        for member_id in group_member:
            if succ:
                succ = insert_table_group_member(database, group_member_table_name, group_id, member_id)
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
                "back_data": "0000",
            }
            save_new_groupid(new_groupid)
            back_json_data = json.dumps(back_data).encode('utf-8')
            socket.sendall(back_json_data)
        else:
            new_groupid -= 1
            back_data = {
                "type": "create_group",
                "back_data": "0001",
            }
            save_new_groupid(new_groupid)
            back_json_data = json.dumps(back_data).encode('utf-8')
            socket.sendall(back_json_data)


def delete_group(data, socket, address, database):
    try:
        content = data['content']
    except:
        pass

def add_new_member(data, socket, address, database):
    try:
        content = data['content']
        group_id = data['group_id']
        member_id = data['member_id']
        group_member_table_name = "group_member" + str(group_id)
        insert_table_group_member(database,group_member_table_name, group_id, member_id)
    except:
        pass
    finally:
        pass
