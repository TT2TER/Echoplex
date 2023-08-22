from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
import socket
import json
import threading


def receive_messages(client_socket):
    while True:
        try:
            data = client_socket.recv(1024)
            if data:
                received_data = json.loads(data.decode('utf-8'))
                print("收到消息:", received_data)
        except:
            break

class sendtest:

    def __init__(self):
        # 从文件中加载UI定义

        # 从 UI 定义中动态 创建一个相应的窗口对象
        # 注意：里面的控件对象也成为窗口对象的属性了
        # 比如 self.ui.button , self.ui.textEdit
        self.ui = QUiLoader().load('chatui.ui')


        self.ui.sendingbut.clicked.connect(self.send)

    def send(self):
        info = self.ui.sendingbox.toPlainText()

        client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_address = ('127.0.0.1', 13579)
        client_socket.connect(server_address)
        receive_thread = threading.Thread(target=receive_messages, args=(client_socket,))
        receive_thread.start()

        while True:
            content = info

            message = {
            "type": "message",
            "content": content,
            }
            json_data = json.dumps(message).encode('utf-8')
            client_socket.sendall(json_data)
            QMessageBox.about(self.ui,
                    '发送成功'
                    )

app = QApplication([])
sendtest = sendtest()
sendtest.ui.show()
app.exec_()