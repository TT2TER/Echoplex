from db.view_chat import search_sequence
import json
import socket


def init_msg_list(received_data, socket, address, database):
    user_id = received_data["content"]["user_id"]
    list = search_sequence(database, user_id, )
    print(list)
    data = {
        "type": "init_msg_list",
        "back_data": "0000",
        "content": {
            "list": list
        }
    }
    json_data = json.dumps(data).encode('utf-8')
    socket.sendall(json_data)
