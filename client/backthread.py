from PySide2.QtCore import QThread, Signal, QDateTime
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit
import json
from lib.public import shared_module


class BackendThread(QThread):
    # 通过类成员对象定义信号对象  
    notify = Signal(dict)
    self_finished =Signal(str)
    is_running = True
    e=None
    # 处理要做的业务逻辑
    def run(self):
        
        while self.is_running :
            try:
                data = shared_module.client.client_socket.recv(10240)
                received_data = json.loads(data.decode('utf-8'))
                print("收到服务端消息：", received_data)
                self.notify.emit(received_data)
            except Exception as e:
                self.e=e
                print(str(self.e))
                self.is_running=False 
        self.self_finished.emit(str(self.e))
    def stop(self):
        #这个函数用来从外界终止这个线程
        self.is_running=False  
        self.e= "normal_close" 

if __name__ == '__main__':
    print("调试线程\n")
