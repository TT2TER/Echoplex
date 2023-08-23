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
        #以下是判断密码是否重复
        entered_password=self.ui.pwd_in.text()
        entered_password2=self.ui.pwd_check.text()
        if entered_password==entered_password2:
             pass
        else :
            QMessageBox.warning(self.ui,'注册失败','两次密码不一致，请重新输入！')
            self.ui.pwd_in.clear()
            self.ui.pwd_check.clear()
            return;
                

        # 以下是用户输入的数据
        entered_name=self.ui.name_in.text()#姓名
        entered_ID=self.ui.num_in.text()#id
        entered_mail=self.ui.mail_in.text()#mail
        entered_password=self.ui.pwd_in.text()#密码
        entered_password2=self.ui.pwd_check.text()#重复密码

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
