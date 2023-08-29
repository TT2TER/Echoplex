from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.login_ui import Ui_Login
from time import sleep

class Login(QWidget):

    def __init__(self):
        # 继承父类
        super().__init__()
        # 加载界面
        #   self.ui = QUiLoader().load('./ui/login.ui')
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        # 按下登录按钮或回车键执行登录过程
        self.ui.pwd_in.returnPressed.connect(self.login)
        self.ui.login_butt.clicked.connect(self.login)

        # 按下切换昼夜按钮切换黑夜模式
        self.ui.dark_mode_butt.clicked.connect(self.toggle_day_night_mode)

        # 按下注册按钮跳转到注册界面
        self.ui.reg_butt.clicked.connect(self.show_registration_page)

    def login(self):

        #获取输入的账号
        entered_ID=self.ui.num_in.text()
        # 获取输入的密码
        entered_password = self.ui.pwd_in.text()
        #entered_ID和entered_password分别为输入的用户名和密码字符串
        def isinteger(string):
            try:
                int(string)
                return True
            except ValueError:
                return False
        if not isinteger(entered_ID) or len(entered_ID) != 5:
            QMessageBox.warning(self, '登录失败', '请输入五位数字账号。')
            return
        
        shared_module.client.user_login(user_id=entered_ID, user_pwd=entered_password)

    
    def recv_login(self,back_data, content):
        #以下部分是信息反馈
        if back_data == "0003":
            QMessageBox.about(self, '登录成功', '欢迎进入系统！')

            shared_module.client.user_id = content['user_id']
            shared_module.client.user_name = content['user_name']
            shared_module.client.pull_friendlist()
            shared_module.client.pull_message()
            shared_module.client.pull_msg_list()
            # 创建主界面窗口
            shared_module.main_page.show()
            sleep(0.2)
            shared_module.main_page.init_chat_list()
            # 关闭自身窗口
            self.close()
        else:
            QMessageBox.warning(self, '登录失败', '用户名或密码错误。')
            return

    def toggle_day_night_mode(self):
        # 这里可以添加切换日夜模式的逻辑
        print("pushed")
        
        # 切换界面的颜色、主题等
        pass

    def show_registration_page(self):
        # 创建注册窗口
        where=self.pos()
        #print(where)
        shared_module.reg_page.move(where)
        shared_module.reg_page.show()
        # 关闭自身窗口
        self.close()



if __name__ == "__main__":
    app = QApplication([])
    login = Login()
    login.show()
    app.exec_()