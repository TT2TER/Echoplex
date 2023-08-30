from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
from PySide2.QtGui import QPixmap
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import Qt
from lib.public import shared_module
from ui.register_ui import Ui_reg
import os


class Register(QWidget):

    def __init__(self):
        super().__init__()

        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui= Ui_reg()
        self.ui.setupUi(self)

        # 按下reg_confirm确认密码开始注册流程
        self.ui.reg_confirm.clicked.connect(self.start_registration)
        # 按下reg_cancel返回登陆界面
        self.ui.reg_cancel.clicked.connect(self.return_to_login)

        self.ui.close_butt.clicked.connect(self.close_win)
        self.ui.mini_butt.clicked.connect(self.minimize_win)

        #显示侧边图片
        img_path = "lib/login_back.png"
        image_path=os.path.join(os.path.dirname(__file__), img_path)
        pixmap = QPixmap(image_path)
        self.ui.side_pic.setPixmap(pixmap)
        self.ui.side_pic.setScaledContents(True)  # 图像自动拉伸

        #以下函数是移动窗口用的
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
        shared_module.app.quit()
    def minimize_win(self):
        #这个是最小化窗口函数
        self.showMinimized()
        
    def start_registration(self):
        # 以下是判断密码是否重复
        entered_password = self.ui.pwd_in.text()
        entered_password2 = self.ui.pwd_check.text()
        if entered_password == entered_password2:
            pass
        else:
            QMessageBox.warning(self, '注册失败', '两次密码不一致，请重新输入！')
            self.ui.pwd_in.clear()
            self.ui.pwd_check.clear()
            return;
        #判断密码是否合法
        if len(entered_password) > 6 and len(entered_password) < 20:
            pass
        else:
            QMessageBox.warning(self, '注册失败', '密码请大于6字符小于20字符，请重新输入。')
            self.ui.pwd_in.clear()
            self.ui.pwd_check.clear()
            return

        # 以下是用户输入的数据
        entered_name = self.ui.name_in.text()  # 姓名
        entered_mail = self.ui.mail_in.text()  # mail
        entered_password = self.ui.pwd_in.text()  # 密码
        entered_password2 = self.ui.pwd_check.text()  # 重复密码
        shared_module.client.user_register(user_name=entered_name, user_email=entered_mail, user_pwd=entered_password, user_image= "04260202")

        
    def recv_register(self, back_data, cocntent):
        if back_data == "0000": 
            print("##############################")
            QMessageBox.information(self, "注册", "注册成功，你的账号是" + str(cocntent["user_id"]))
            where=self.pos()
            #print(where)
            shared_module.login_page.move(where)
            shared_module.login_page.show()
            self.close()
        else:
            QMessageBox.information(self, "注册失败", "服务器故障，注册失败。")



    def return_to_login(self):
        # 返回登录界面的逻辑
        # 你可以关闭当前界面，打开登录界面等
        where=self.pos()
        #print(where)
        shared_module.login_page.move(where)
        shared_module.login_page.show()
        self.close()
        # shared_module.main_page = Login()


if __name__ == "__main__":
    app = QApplication([])
    register = Register()
    register.show()
    app.exec_()
