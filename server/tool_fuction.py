from global_data import online_clients


def find_userid_by_socket(socket_to_find):
    for socket, userid in online_clients.items():
        if socket == socket_to_find:
            return userid
    return None  # 如果没找到对应的userid，返回None
