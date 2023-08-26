from PySide2.QtCore import QThread, Signal, QDateTime
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit
import json
import socket
from lib.public import shared_module

#发文件线程
class FileSendThread(QThread):
    # 通过类成员对象定义信号对象  
    notify = Signal(dict)
    
    def __init__(self, ip, port, file_path):
        super().__init__()
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip, port)
        self.socket.connect(self.server_address)
        self.file_path=file_path


    # 处理要做的业务逻辑
    def run(self):
        #发送文件
        buff_size=10240
        with open(self.file_path,'rb') as f:
            while True:
                data=f.read(buff_size)
                if not data:
                    break
                self.socket.sendall(data)
        print("文件发送完毕,准备关闭线程socket")
        self.socket.close()
        #发送结束，向主线程发送信号
        emit_data = {
            'type': 'user_send_file',
            'back_data': '0000'
        }
        self.notify.emit(emit_data)


def send_file_handler(emit_data):
    # 处理发射回来的信号
    try:
        back_data = emit_data.get('back_data', None)
        if back_data == '0000':
            print("文件发送成功")
            # 文件发送成功的UI交互

    except Exception as e:
        print("结束发送文件时候寄了，在file_thread这send_file_handler里头:" + str(e))
    finally:
        print("处理完一个发送文件请求了")
    





class FileReceiveThread(QThread):
    # 通过类成员对象定义信号对象  
    notify = Signal(dict)
    
    def __init__(self, ip, port):
        super().__init__()
        self.socket=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.server_address = (ip, port)
        self.socket.connect(self.server_address)


    # 接收文件
    def run(self):
        #接收文件
        buff_size=10240
        print("收到文件名："+file_name)
        file_path=shared_module.client_file_path+"/"+file_name
        with open(file_path,'wb') as f:
            while True:
                data=self.socket.recv(buff_size)
                if not data:
                    break
                f.write(data)
        print("文件接收完毕,准备关闭线程socket")
        self.socket.close()
        #接收结束，向主线程发送信号
        emit_data = {
            'type': 'user_receive_file',
            'back_data': '0000'
        }
        self.notify.emit(emit_data)
        


