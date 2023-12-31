from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import Qt
from dependencies.public import shared_module
from ui.login_ui import Ui_Login
from time import sleep
import os

class Login(QWidget):

    def __init__(self):
        # 继承父类
        super().__init__()
        # 加载界面
        #   self.ui = QUiLoader().load('./ui/login.ui')
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_Login()
        self.ui.setupUi(self)
        # 按下登录按钮或回车键执行登录过程
        self.ui.pwd_in.returnPressed.connect(self.login)
        self.ui.login_butt.clicked.connect(self.login)

        # 按下切换昼夜按钮切换黑夜模式
        self.ui.remember_butt.clicked.connect(self.remember_pwd)

        # 按下注册按钮跳转到注册界面
        self.ui.reg_butt.clicked.connect(self.show_registration_page)

        #按下按钮弹出找回密码成功
        self.ui.forgot_pwd_butt.clicked.connect(self.get_pwd)

        self.ui.close_butt.clicked.connect(self.close_win)
        self.ui.mini_butt.clicked.connect(self.minimize_win)

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

    def close_win(self):
        self.close()
        shared_module.app.quit()
    def minimize_win(self):
        #这个是最小化窗口函数
        self.showMinimized()

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
            #在这里调起人脸识别的功能
            #TODO: aym

            #在这里结束调起人脸识别的功能
            QMessageBox.about(self, '登录成功', '欢迎进入系统！')
            if shared_module.token_enabled == True:
                print("尝试写入token")
                token = content['token']
                savepath = "files/token/token.txt"
                # 如果savepath不存在，创建savepath
                os.makedirs(os.path.dirname(savepath), exist_ok=True)
                # 如果token.txt不存在，创建它。往token.txt中写入token
                with open(savepath, 'w') as token_file:
                    token_file.write(token)
                print("Token saved to token.txt")
            shared_module.client.user_id = content['user_id']
            shared_module.main_page.show_my_avatar(True)
            shared_module.client.user_name = content['user_name']
            shared_module.client.pull_friendlist()
            shared_module.client.pull_grouplist()
            shared_module.client.pull_message()
            shared_module.client.pull_msg_list()
            # 创建主界面窗口

            screen_geometry = shared_module.app.desktop().screenGeometry()
            setip_geometry = shared_module.main_page.geometry()
            center_x = (screen_geometry.width() - setip_geometry.width()) / 2
            center_y = (screen_geometry.height() - setip_geometry.height()) / 2
            shared_module.main_page.move(center_x, center_y)
            shared_module.main_page.show()
            sleep(0.2)
            #shared_module.main_page.init_chat_list()
            # 关闭自身窗口
            print("登录窗口要关闭啦！")
            self.close()
        elif back_data == "0005":
            print("token已经过期or没有token")
        else:
            QMessageBox.warning(self, '登录失败', '用户名或密码错误')
            return

    def remember_pwd(self):
    # Get the state of the radio button
        remember_state = self.ui.remember_butt.isChecked()

        if remember_state:
            # If the radio button is checked, remember the password
            # For example, you can store the password in a class variable
            # self.remembered_password = self.ui.pwd_in.text()
            shared_module.token_enabled = True
            # print("Password remembered:", self.remembered_password)
        else:
            # If the radio button is unchecked, forget the password
            # Clear the stored password
            # self.remembered_password = None
            shared_module.token_enabled = False
            print("Password forgotten")

    def show_registration_page(self):
        # 创建注册窗口
        screen_geometry = shared_module.app.desktop().screenGeometry()
        setip_geometry = shared_module.reg_page.geometry()
        center_x = (screen_geometry.width() - setip_geometry.width()) / 2
        center_y = (screen_geometry.height() - setip_geometry.height()) / 2
        shared_module.reg_page.move(center_x, center_y)
        shared_module.reg_page.show()
        # 关闭自身窗口
        self.close()

    def get_pwd(self):
        entered_ID=self.ui.num_in.text()
        if entered_ID==None:
            QMessageBox.warning(self,"没有id","请先填写正确的用户id")
        elif len(str(entered_ID)) == 5 and str(entered_ID).startswith('1'):
            QMessageBox.information(self,"忘记密码","重置成功，请查收您的邮箱")
            #TODO:
            #在elif这里放你重置密码的东西
            shared_module.client.retrieve_password_request(entered_ID)
        else:
            QMessageBox.warning(self,"id不合法","请先填写正确的用户id")



if __name__ == "__main__":
    app = QApplication([])
    login = Login()
    login.show()
    app.exec_()