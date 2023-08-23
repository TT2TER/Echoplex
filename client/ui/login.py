from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from window import Main_win
from register import Register

class Login:

    def __init__(self):
        # 加载界面
        self.ui = QUiLoader().load('./client/ui/login.ui')

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

#TODO:
        # 在此以下完成逻辑部分
        # 下一行是测试用假设正确的密码是 "password123"
        correct_password = "password123"

        #以下部分是信息反馈
        if entered_password == correct_password:
            QMessageBox.about(self.ui, '登录成功', '欢迎进入系统！')
            # 创建主界面窗口
            shared_module.main_page = Main_win()
            shared_module.main_page.ui.show()
            # 关闭自身窗口
            self.ui.close()
        else:
            QMessageBox.warning(self.ui, '登录失败', '密码错误，请重试。')#待修改错误原因部分
            return;

    def toggle_day_night_mode(self):
        # 这里可以添加切换日夜模式的逻辑
        #TODO:
        # 切换界面的颜色、主题等
        pass

    def show_registration_page(self):
        # 创建主界面窗口
        shared_module.reg_page = Register()
        shared_module.reg_page.ui.show()
        # 关闭自身窗口
        self.ui.close()

