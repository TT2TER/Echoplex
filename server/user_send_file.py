import socket
import os, time
import threading
import json
from user_chat import user_chat
from tool_fuction import find_userid_by_socket
import platform
from global_data import server_ip



def user_send_file(received_data, _socket, address, database):
    receive_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    receive_socket.bind((server_ip, 0))
    ip, port = receive_socket.getsockname()
    receive_socket.listen(1)
    print(f"File server listening on {ip}:{port}")
    content = received_data['content']
    filepath = content['filepath']
    filesize = content['filesize']
    is_avatar = content['is_avatar']
    chat_id = content['chat_id']

    def receive_file(ip, port, filepath, _socket, receive_socket, filesize, is_avatar):
        message = {
            "type": "user_send_file",
            "back_data": "0000",
            "content": {
                "sender_ip": ip,
                "port": port,
                "filepath": filepath,
                "filesize": filesize,
                "is_avatar": is_avatar,
            }
        }
        json_message = json.dumps(message).encode('utf-8')
        _socket.sendall(json_message)
        client_socket, client_address = receive_socket.accept()
        print(f"已经连接上'{client_address}'，准备收取文件")
        try:
            # 分离文件名字、创建目录、根据大小接受文件
            filename = os.path.basename(filepath)
            # user_id = find_userid_by_socket(_socket)
            user_id = content['sender']
            system_name = platform.system()
            received_data['type'] = "user_chat"
            file_extension = os.path.splitext(filename)[1]
            if is_avatar:
                savepath = "files/" + "avatar/" + str(user_id) + file_extension
            elif chat_id is not None:
                savepath = "files/" + str(chat_id) + "/" + filename
            # linux_savepath = windows_savepath.replace("\\", "/")
            # if system_name == "Windows":
            #     savepath = windows_savepath
            # elif system_name == "Linux":
            #     savepath = linux_savepath
            content['filepath'] = savepath
            if chat_id is not None:
                user_chat(received_data, _socket, address, database)
            os.makedirs(os.path.dirname(savepath), exist_ok=True)  # 创建文件夹路径
            recv_data = 0
            with open(savepath, 'wb') as file:
                while True:
                    data = client_socket.recv(10240)
                    if not data:
                        # print("我break了")
                        break
                    file.write(data)
                recv_data += len(data)

            print(recv_data)
            print(f"File '{savepath}' received and saved")
            if is_avatar:
                user_chat(received_data, _socket, address, database)
        except FileExistsError:
            print(f"File '{savepath}' already exists")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            receive_socket.close()

    send_thread = threading.Thread(target=receive_file,
                                   args=(ip, port, filepath, _socket, receive_socket, filesize, is_avatar))
    send_thread.start()

