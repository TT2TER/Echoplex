from PySide2.QtWidgets import QWidget, QMessageBox
from ui.new_group_ui import Ui_new_group
from lib.public import shared_module

class New_group(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_new_group()
        self.ui.setupUi(self)

        print("新建群聊窗口已经打开……")
        self.ui.creat_group_butt.clicked.connect(self.creat_new_group)

    def creat_new_group(self):
        """这里是点击创建新群聊后调用的函数
        
        写调用发送创建群组请求的函数以及消息内容的处理"""
        group_name=self.ui.new_group_name.text()
        member_id=self.ui.group_member_list.toPlainText()

        if group_name==None:
            QMessageBox.warning(self,"群名不能为空","请填写群名")
        #请帮我写一段python代码，用来判断一串字符串的合法性，这串字符串应该满足以下要求：1，由若干1开头的五位数组成。2.五位数个数大于等于两个。3.两个数之间用;分隔
        #自己写分开member_id 的函数吧