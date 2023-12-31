import socket
import threading
import json
from user_register import user_register
from user_login import user_login
from user_send_file import user_send_file
from user_receive_file import user_receive_file
from user_addfriend import user_addfriend
from ans_addfriend import ans_addfriend
from init_msg_list import init_msg_list
from user_friendlist import user_friendlist
from db import *
import sys
from user_chat import user_chat, retrieve_messages
from global_data import online_clients, server_address
import queue
import platform
from group_management import create_group, delete_group, add_new_member
from group_list import group_list
from user_video_chat import user_video_chat
from ans_video_chat import ans_video_chat
from retrieve_password import retrieve_password

socket_queue_dict = {}


def parse_received_data_with_brackets(socket, received_data):
    current_json = ""
    open_brackets = 0

    for char in received_data.decode('utf-8'):
        current_json += char
        if char == '{':
            open_brackets += 1
        elif char == '}':
            open_brackets -= 1
        if open_brackets == 0:
            try:
                json_obj = json.loads(current_json)
                socket_queue_dict[socket].put(json_obj)  # 将消息放入队列
                print("成功将消息放入队列", json_obj)
                size = socket_queue_dict[socket].qsize()
                print(f"队列中当前有{size}项")
                current_json = ""
            except json.JSONDecodeError:
                print("JSON decoding failed for:", current_json)


def handle_client(socket, address):
    try:
        database = sql_connection()
        print("数据库打开成功，好耶")
    except:
        print("handle_client获取数据库连接失败，小艾的锅")
        return
    while True:
        try:
            # bufsize 指定要接收的最大数据量
            received_data = socket.recv(10240)
            if not received_data:
                print("对方已断开连接")
                break
            print(received_data)
            parse_received_data_with_brackets(socket, received_data)
        except Exception as e:
            print(f"{address}已经下线或者收消息过程中寄了，自己看报错吧：" + str(e))
            break
        while not socket_queue_dict[socket].empty():
            try:
                received_data = socket_queue_dict[socket].get()
                print("处理ing……")
                message_handlers = {
                    'user_register': user_register,
                    'user_login': user_login,
                    'user_chat': user_chat,
                    'user_send_file': user_send_file,
                    'user_receive_file': user_receive_file,
                    'user_addfriend': user_addfriend,
                    'ans_addfriend': ans_addfriend,
                    'pull_message': retrieve_messages,
                    'init_msg_list': init_msg_list,
                    'pull_friendlist': user_friendlist,
                    'pull_group_list': group_list,
                    'create_group': create_group,
                    'delete_group': delete_group,
                    'add_new_member': add_new_member,
                    'user_video_chat': user_video_chat,
                    'ans_video_chat': ans_video_chat,
                    'retrieve_password': retrieve_password
                }
                handler = message_handlers.get(received_data['type'])
                if handler:
                    print(f"处理来自{client_address}的请求")
                    print("handler为" + getattr(handler, "__name__", "unknown_function"))
                    succ = handler(received_data, socket, address, database)
                    print("处理结果：" + str(succ))
                else:
                    print("收到了服务器不认识的消息类型欸")
                    break
            except Exception as e:
                print(str(address) + " 连接异常，准备断开: " + str(e))
                break
            finally:
                print("服务器完工，等待下一个请求oVo")
    try:
        # 简单地维护在线用户字典，可能会有问题
        # 遍历字典中的项
        for user_id, (_socket, _address) in online_clients.items():
            if _socket == socket:
                # 找到匹配的项，删除它
                del online_clients[user_id]
    except:
        pass


def init_server(database):
    system_name = platform.system()
    if system_name == "Windows":
        print("当前操作系统是 Windows")
    elif system_name == "Linux":
        print("当前操作系统是 Linux")
    else:
        print("当前操作系统是", system_name)
    # 划了红色下划线，但是能跑。python，很神奇吧？
    create_table_user(database, "user")
    create_table_user_friend(database, "user_friend")
    create_table_relation(database, "table_relation")
    create_table_group(database, "[group]")
    create_table_group_member(database, "group_member")
    create_table_chat(database, "chat")
    create_view_chat(database, "view_chat")
    create_table_file(database, table_name="file")


if __name__ == "__main__":
    try:
        database = sql_connection()
        print("数据库打开成功，好耶")
        # c = database.cursor()
    except Exception as e:
        print("数据库连接失败了，呜呜呜：" + str(e))
    try:
        init_server(database)
    except Exception as e:
        print("服务器初始化失败:" + str(e))
        sys.exit()
    try:
        # 创建TCPsocket对象
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 绑定地址和端口
        server_socket.bind(server_address)
        print("TCP Server is listening on {}:{}".format(server_address[0], server_address[1]))
        # TCP 监听
        # backlog 指定在拒绝连接之前，操作系统可以挂起的最大连接数量s
        backlog = 20
        server_socket.listen(backlog)
        print("服务器等待连接？O.o")
        while True:
            new_socket, client_address = server_socket.accept()
            print("服务器连接上了客户端" + str(client_address) + "，准备干活！")
            server_queue = queue.Queue()
            socket_queue_dict[new_socket] = server_queue
            client_handler = threading.Thread(target=handle_client, args=(new_socket, client_address))
            # message_receiver = threading.Thread(target=receive_and_parse, args=(new_socket, client_address))
            # message_receiver.daemon = True
            client_handler.daemon = True
            # message_receiver.start()
            client_handler.start()
    except Exception as e:
        print("服务器socket寄了，原因是：" + str(e))
