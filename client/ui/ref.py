import sys
import socket
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QTextEdit, QLineEdit, QPushButton, QLabel, QHBoxLayout, QGridLayout
from PySide2.QtCore import QThread, Signal

class UdpChatClient(QThread):
    messageReceived = Signal(str)

    def __init__(self, ip, send_port, receive_port):
        super(UdpChatClient, self).__init__()
        self.ip = ip
        self.send_port = send_port
        self.receive_port = receive_port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.socket.bind(('', self.receive_port))

    def run(self):
        while True:
            data, addr = self.socket.recvfrom(1024)
            message = data.decode()
            sender_info = f"{addr[0]}:{addr[1]}"
            self.messageReceived.emit(f"{sender_info}: {message}")

    def send_message(self, message):
        self.socket.sendto(message.encode(), (self.ip, self.send_port))

class ChatWindow(QWidget):
    def __init__(self):
        super(ChatWindow, self).__init__()
        self.setWindowTitle("聊天室")
        self.layout = QVBoxLayout()

        # Chat window
        self.chat_hist = QTextEdit()
        self.layout.addWidget(self.chat_hist)

        # Message input and send button
        self.msg_layout = QHBoxLayout()

        self.msg_input = QLineEdit()
        self.msg_layout.addWidget(self.msg_input)

        self.send_btn = QPushButton("发送")
        self.send_btn.clicked.connect(self.send_message)
        self.msg_layout.addWidget(self.send_btn)

        self.layout.addLayout(self.msg_layout)

        # Configuration fields
        self.config_layout = QHBoxLayout()

        self.send_port_lbl = QLabel("发送端口:")
        self.send_port_edit = QLineEdit()
        self.config_layout.addWidget(self.send_port_lbl)
        self.config_layout.addWidget(self.send_port_edit)

        self.ip_lbl = QLabel("IP 地址:")
        self.ip_edit = QLineEdit()
        self.config_layout.addWidget(self.ip_lbl)
        self.config_layout.addWidget(self.ip_edit)

        self.recv_port_lbl = QLabel("接收端口:")
        self.recv_port_edit = QLineEdit()
        self.config_layout.addWidget(self.recv_port_lbl)
        self.config_layout.addWidget(self.recv_port_edit)

        self.save_btn = QPushButton("保存")
        self.save_btn.clicked.connect(self.start_chat)
        self.config_layout.addWidget(self.save_btn)

        self.layout.addLayout(self.config_layout)

        self.setLayout(self.layout)

        self.client = None

    def start_chat(self):
        ip = self.ip_edit.text()
        send_port = int(self.send_port_edit.text())
        receive_port = int(self.recv_port_edit.text())

        self.client = UdpChatClient(ip, send_port, receive_port)
        self.client.messageReceived.connect(self.display_message)
        self.client.start()

    def display_message(self, message):
        self.chat_hist.append(message)

    def send_message(self):
        message = self.msg_input.text()
        if self.client is not None:
            self.client.send_message(message)
            self.display_message(f"我: {message}")
        self.msg_input.clear()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ChatWindow()
    window.show()
    sys.exit(app.exec_())
