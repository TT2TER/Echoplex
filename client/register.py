from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module

class Register:

    def __init__(self):
        # 加载界面
        self.ui = QUiLoader().load('./client/ui/register.ui')

        #按下reg_confirm确认密码开始注册流程
        self.ui.reg_confirm.clicked.connect(self.start_registration)

        #按下reg_cancel返回登陆界面
        self.ui.reg_cancel.clicked.connect(self.return_to_login)

    def start_registration(self):
        # 这里实现注册流程
        #TODO:
        # 获取输入的用户名和密码，并进行注册逻辑
        
        # 注册完成后可以显示成功消息或错误消息
        QMessageBox.information(self.ui, "Registration", "Registration Successful")
        shared_module.login_page.ui.show()
        self.ui.close()

    def return_to_login(self):
        # 返回登录界面的逻辑
        # 你可以关闭当前界面，打开登录界面等
        shared_module.login_page.ui.show()
        self.ui.close()
        #shared_module.main_page = Login()
          

if __name__ == "__main__":
    app = QApplication([])
    register = Register()
    register.ui.show()
    app.exec_()
