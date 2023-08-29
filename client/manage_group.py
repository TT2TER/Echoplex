from PySide2.QtWidgets import QWidget, QMessageBox
from ui.manage_group_ui import Ui_manage_group
from lib.public import shared_module
import re

class Manage_group(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_manage_group()
        self.ui.setupUi(self)

        
        self.ui.add_member_butt.clicked.connect(self.add_new_member)
        self.ui.del_group_butt.clicked.connect(self.del_group)

    def add_new_member(self):
        """这里写调用发送创建群组请求的函数以及消息内容的处理"""
        member_ids=self.ui.group_member_list.toPlainText()
        print(member_ids)
        #以下是正確性驗證
        pattern = r'^1\d{4}(;1\d{4})*$'
        if re.match(pattern, member_ids)== None:
            QMessageBox.warning(self,"成員不合法","請滿足以下要求：\n1:由若干1开头的五位用戶id组成\n2:两个数之间用英文符號;分隔")
            return


        #自己写分开member_id 的函数吧
        #調用發送請求，member_ids是“10001;10002;10005”這樣的
        #自己写分开member_id 的函数吧
        self.ui.group_member_list.clear()

        pass

    def del_group(self):
        """這裡寫刪除group的操作
        
        可能需要從shared_module.main_page.cur_id中獲取當前群聊chat_id
        """
        print("刪除群聊")
        #這裡添加刪除群聊的函數和邏輯
        pass