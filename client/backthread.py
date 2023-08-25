from PySide2.QtCore import QThread, Signal, QDateTime
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit
import json
from lib.public import shared_module


class BackendThread(QThread):
    # 通过类成员对象定义信号对象  
    nofify = Signal(dict)

    # 处理要做的业务逻辑
    def run(self):
        while True:
            try:
                data = shared_module.client.client_socket.recv(10240)
                received_data = json.loads(data.decode('utf-8'))
                print("收到服务端消息：", received_data)
                self.nofify.emit(received_data)
            except Exception as e:
                print("服务端寄了或者收消息寄了：" + str(e))
                break


if __name__ == '__main__':
    print("调试线程\n")
