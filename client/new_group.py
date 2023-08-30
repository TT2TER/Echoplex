from PySide2.QtWidgets import QWidget, QMessageBox
from ui.new_group_ui import Ui_new_group
from lib.public import shared_module


class New_group(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_new_group()
        self.ui.setupUi(self)

        self.ui.creat_group_butt.clicked.connect(self.creat_new_group)

    def creat_new_group(self):
        """这里是点击创建新群聊后调用的函数
        
        写调用发送创建群组请求的函数以及消息内容的处理"""
        group_name=self.ui.new_group_name.text()
        member_ids=self.ui.group_member_list.toPlainText()
        print(group_name,member_ids)
        #群名合法性
        if group_name=="":
            QMessageBox.warning(self,"群名不能为空","请填写群名")
        #群成員合法性
        members = member_ids.split(';')
        valid_count = 0
        for num in members:
            if len(num) == 5 and num.isdigit() and num.startswith('1'):
                valid_count += 1
        if valid_count >= 2:
            print("字符串满足要求")
            pass
        else:
            print("字符串不满足要求")
            QMessageBox.warning(self,"群成員不合法","請滿足以下要求：\n1:由若干1开头的五位用戶id组成\n2:两个数之间用英文符號;分隔")
            return


        #調用發送請求，member_ids是“10001;10002;10005”這樣的,members是拆開的
        shared_module.client.create_group(members,group_name,image_path="")


        #以下是清空文本框
        self.ui.new_group_name.clear()
        self.ui.group_member_list.clear()