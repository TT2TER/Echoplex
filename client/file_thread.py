from PySide2.QtCore import QThread, Signal, QDateTime
from PySide2.QtWidgets import QApplication, QDialog, QPlainTextEdit, QMessageBox
import json
import socket
from dependencies.public import shared_module
import sys, os
from tool_function import get_file_extension
import time


# 发文件线程
class FileSendThread(QThread):
    # 通过类成员对象定义信号对象  
    notify = Signal(dict)
    percentage=Signal(int)

    def __init__(self, ip, port, file_path, filesize, is_avatar):
        super().__init__()
        try:
            print("开始初始化")
            self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.server_address = (ip, port)
            # self.socket.connect(("127.0.0.1", port))
            self.socket.connect(self.server_address)
            self.file_path = file_path
            self.filesize = filesize
            self.sent_percentage = 0
            self.is_avatar = is_avatar
            print("初始化完成")
        except Exception as e:
            print("file_thread初始化寄了" + str(e))

    # 处理要做的业务逻辑
    def run(self):
        # 发送文件
        buff_size = 10240
        # 根据文件大小发送文件

        #下面這行代碼不要刪除，否則會出現進度條加載錯誤
        time.sleep(1)
        #上面這行代碼不要刪除，否則會出現進度條加載錯誤
        print("Begin sending……")
        with open(self.file_path, 'rb') as file:
            data_sent = 0
            while data_sent < self.filesize:
                data = file.read(buff_size)
                print("read file")
                if not data:
                    break
                self.socket.sendall(data)
                data_sent += len(data)
                self.sent_percentage = data_sent * 100 / self.filesize
                #在这里emit进度条
                if not self.is_avatar:
                    self.percentage.emit(self.sent_percentage)
        print(f"Sent file '{self.file_path}' of size {self.filesize} bytes.")
        print("文件发送完毕,准备关闭线程socket")
        self.socket.close()
        # 发送结束，向主线程发送信号
        emit_data = {
            'type': 'user_send_file',
            'back_data': '0000'
        }
        self.send_file_handler(emit_data)


    def send_file_handler(self,emit_data):
        # 处理发射回来的信号
        try:
            back_data = emit_data.get('back_data', None)
            if back_data == '0000':
                print("文件发送成功")
                #QMessageBox.information(self,"文件发送成功","在"+emit_data.get('filepath', None))
                print("文件发送成功,在",emit_data.get('filepath', None))

        except Exception as e:
            print("结束发送文件时候寄了，在file_thread这send_file_handler里头:" + str(e))
            #弹窗失败
            #QMessageBox.warning(self,"文件发送失败","文件发送失败")
        finally:
            print("处理完一个发送文件请求了")


class FileReceiveThread(QThread):
    # 通过类成员对象定义信号对象  
    notify = Signal(dict)
    percentage=Signal(int)
    def __init__(self, content):
        super().__init__()
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print(content)
        self.server_address = (content["sender_ip"], content["port"])
        self.socket.connect(self.server_address)
        self.filepath = content["filepath"]
        self.filesize = content["filesize"]
        self.is_avatar = content["is_avatar"]
        self.sender_id = content["sender"]
        self.received_percentage = 0
        self.chat_id = content["chat_id"]
        print("FileReceiveThread初始化成功")

    # 接收文件
    def run(self):
        # 接收文件
        buff_size = 10240
        time.sleep(1)
        print("开始收到文件啦")
        try:
            filename = os.path.basename(self.filepath)
            if self.is_avatar:
                file_extension = get_file_extension(self.filepath)
                savepath = "files/avatar/" + str(self.sender_id) + file_extension
                print("here")
            elif self.chat_id:
                savepath = "files/chat_files/" + str(self.chat_id) + "/" + filename
            os.makedirs(os.path.dirname(savepath), exist_ok=True)  # 创建文件夹路径
            with open(savepath, 'wb') as file:
                received_size = 0
                while received_size < self.filesize:
                    data = self.socket.recv(4096)
                    received_size += len(data)
                    file.write(data)
                    self.received_percentage = received_size * 100 / self.filesize
                    if not self.is_avatar:
                        #在这里emit进度条
                        self.percentage.emit(self.received_percentage)

            print(f"File '{self.filepath}' received and saved")
        except FileExistsError:
            print(f"File '{self.filepath}' already exists")
        except Exception as e:
            print("An error occurred:", e)
        finally:
            self.socket.close()
        # 接收结束，向主线程发送信号
        emit_data = {
            'type': 'user_receive_file',
            'back_data': '0000',
            'filepath': self.filepath
        }
        self.notify.emit(emit_data)


def receive_file_handler(emit_data):
    # 处理接收文件线程发射回来的信号
    try:
        back_data = emit_data.get('back_data', None)
        if back_data == '0000':
            print("文件接收成功，路径是" + emit_data.get('filepath', None))
            shared_module.main_page.del_percentage_bar()
            #shared_module.progress_bar.close_progress_bar()
            #QMessageBox.information("文件接受成功,在",emit_data.get('filepath', None))

    except Exception as e:
        print("结束接收文件时候寄了，在file_thread这receive_file_handler里头:" + str(e))
    finally:
        print("处理完一个接收文件请求了")
