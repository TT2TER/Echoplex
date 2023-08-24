from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from client_fuction import Client


class Register:

    def __init__(self):
        # 加载界面
        self.ui = QUiLoader().load('./ui/register.ui')

        # 按下reg_confirm确认密码开始注册流程
        self.ui.reg_confirm.clicked.connect(self.start_registration)

        # 按下reg_cancel返回登陆界面
        self.ui.reg_cancel.clicked.connect(self.return_to_login)

    def start_registration(self):
        # 以下是判断密码是否重复
        entered_password = self.ui.pwd_in.text()
        entered_password2 = self.ui.pwd_check.text()
        if entered_password == entered_password2:
            pass
        else:
            QMessageBox.warning(self.ui, '注册失败', '两次密码不一致，请重新输入！')
            self.ui.pwd_in.clear()
            self.ui.pwd_check.clear()
            return;

        # 以下是用户输入的数据
        entered_name = self.ui.name_in.text()  # 姓名
        entered_ID = self.ui.num_in.text()  # id
        entered_mail = self.ui.mail_in.text()  # mail
        entered_password = self.ui.pwd_in.text()  # 密码
        entered_password2 = self.ui.pwd_check.text()  # 重复密码

        result = shared_module.client.user_register(user_id=entered_ID, user_name=entered_name, user_email=entered_mail, user_pwd=entered_password, user_image= "04260202")

        if result == 0:
            QMessageBox.information(self.ui, "注册", "注册成功")
            shared_module.login_page.ui.show()
            self.ui.close()
        elif result == 1:
            QMessageBox.information(self.ui, "注册失败", "服务器故障，注册失败。")
        elif result == 2:
            QMessageBox.information(self.ui, "注册失败", "用户名需要小于15字符。")
        elif result ==3:
            QMessageBox.information(self.ui, "注册失败", "密码需要大于6字符，小于15字符。")



    def return_to_login(self):
        # 返回登录界面的逻辑
        # 你可以关闭当前界面，打开登录界面等
        shared_module.login_page.ui.show()
        self.ui.close()
        # shared_module.main_page = Login()


if __name__ == "__main__":
    app = QApplication([])
    register = Register()
    register.ui.show()
    app.exec_()
