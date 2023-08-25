def recv_friend_message(back_data, content):
    print(content)


def recv_group_message(back_data, content):
    sender = content['sender']
    msg = content['msg']
    time = content['time']
    group_id = content['group_id']


