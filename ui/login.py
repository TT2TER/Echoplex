from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module

class Login:

    def __init__(self):
        # 加载界面
        self.ui = QUiLoader().load('/login.ui')

        # 按下登录按钮或回车键执行登录过程
        self.ui.passwordEdit.returnPressed.connect(self.login)
        self.ui.sendingbut.clicked.connect(self.login)

        # 按下切换昼夜按钮切换黑夜模式
        self.ui.toggleDayNightButton.clicked.connect(self.toggle_day_night_mode)

        # 按下注册按钮跳转到注册界面
        self.ui.registerButton.clicked.connect(self.show_registration_page)

    def login(self):
        # 获取输入的密码
        entered_password = self.ui.passwordEdit.text()

        # 这里可以添加实际的登录逻辑
        # 假设正确的密码是 "password123"
        correct_password = "password123"

        if entered_password == correct_password:
            QMessageBox.about(self.ui, '登录成功', '欢迎进入系统！')
        else:
            QMessageBox.warning(self.ui, '登录失败', '密码错误，请重试。')#待修改错误原因部分
            return;

    def toggle_day_night_mode(self):
        # 这里可以添加切换日夜模式的逻辑
        # 切换界面的颜色、主题等
        pass

    def show_registration_page(self):
        # 这里可以添加跳转到注册界面的逻辑
        # 可能需要创建新的窗口或切换界面等
        pass

app = QApplication([])
shared_module.login_page = Login()
shared_module.login_page.ui.show()
app.exec_()
