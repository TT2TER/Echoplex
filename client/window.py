from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.chatroom_ui import Ui_chatroom

class Main_win(QWidget):

    def __init__(self):
        super().__init__()
        self.ui= Ui_chatroom()
        self.ui.setupUi(self)
        #TODO:

        self.ui.send_butt.clicked.connect(self.send)

    def send(self):
        # 获取发送框中的文本
        message = self.ui.text_in.toPlainText()

        # 在这里添加发送的功能

        
        if message:
            # 将文本添加到 view_box 中
            item = QListWidgetItem(message)
            self.ui.view_box.addItem(item)

            # 清空发送框
            self.ui.text_in.clear()