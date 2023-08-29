from PySide2.QtWidgets import QWidget, QMessageBox
from ui.manage_group_ui import Ui_manage_group
from lib.public import shared_module

class Manage_group(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_manage_group()
        self.ui.setupUi(self)

        
        self.ui.add_group_butt.clicked.connect(self.add_new_member)

    def add_new_member(self):
        """这里写调用发送创建群组请求的函数以及消息内容的处理"""
        member_id=self.ui.group_member_list.toPlainText()

        #自己写分开member_id 的函数吧