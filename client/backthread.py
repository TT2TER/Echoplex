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
                print("断网了" + str(e))

                print("my在这里加一个断网弹窗的函数")
                #TODO：

                break


if __name__ == '__main__':
    print("调试线程\n")
