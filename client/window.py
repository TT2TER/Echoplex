from PySide2.QtWidgets import QApplication, QMessageBox, QWidget, QListWidgetItem
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.chatroom_ui import Ui_chatroom
from chating_item import Chating_item
import os
class Main_win(QWidget):

    def __init__(self):
        super().__init__()
        self.ui= Ui_chatroom()
        self.ui.setupUi(self)
        #TODO:

        self.ui.send_butt.clicked.connect(self.send)
        self.ui.send_butt.clicked.connect(self.add_list)
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

    def handle_item_clicked(self,value):
        print("Item clicked with value:", value)


    def add_list(self):
        self.img_path = "lib/login_back.png"
        self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
        test=Chating_item(self.image_path,"name","message")
        list_item=QListWidgetItem(self.ui.chat_list_view)
        list_item.setSizeHint(test.sizeHint())
        self.ui.chat_list_view.setItemWidget(list_item,test)
        test.itemClicked.connect(self.handle_item_clicked)

if __name__ == "__main__":
    app = QApplication([])
    login = Main_win()
    login.show()
    app.exec_()