from PySide2.QtWidgets import QWidget, QMessageBox
from ui.new_group_ui import Ui_new_group
from dependencies.public import shared_module
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import Qt


class New_group(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_new_group()
        self.ui.setupUi(self)

        self.ui.creat_group_butt.clicked.connect(self.creat_new_group)

        self.ui.close_butt.clicked.connect(self.close_win)
        self.ui.mini_butt.clicked.connect(self.minimize_win)
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    #以下是关窗口函数
    def close_win(self):
        self.close()
    def minimize_win(self):
        #这个是最小化窗口函数
        self.showMinimized()

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
            QMessageBox.warning(self,"群成員不合法","請滿足以下要求：\n1:由若干1开头的五位用戶id组成\n2:两个数之间用英文符號;分隔\n3:至少要填兩個id")
            return
        

        #調用發送請求，member_ids是“10001;10002;10005”這樣的,members是拆開的
        mem = []
        for num in members:
            mem.append(int(num))
        shared_module.client.create_group(mem, group_name, image_path="")
        QMessageBox.information(self,"创建群聊成功","群名为："+group_name)
        #以下是清空文本框
        self.ui.new_group_name.clear()
        self.ui.group_member_list.clear()
        self.close()