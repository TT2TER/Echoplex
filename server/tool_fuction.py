from global_data import online_clients


def find_userid_by_socket(socket_to_find):
    for socket, userid in online_clients.items():
        if socket == socket_to_find:
            return userid
    return None  # 如果没找到对应的userid，返回None


def find_friend_id(user_id, chat_id):
    print("尝试通过chat_id和user_id找到friend_id……")
    if len(chat_id) == 10:
        first_five = int(chat_id[:5])
        last_five = int(chat_id[5:])
        if first_five == user_id:
            friend_id = last_five
            return friend_id
        elif last_five == user_id:
            friend_id = first_five
            return friend_id
        else:
            print("无法确定 receiver_id，可能存在错误。")
            return -1
    else:
        print("chat_id不是十位数，不是私聊chat_id")
        return -2
