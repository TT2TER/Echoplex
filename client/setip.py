from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.setip_ui import Ui_setip
import re
from client_fuction import Client
from backthread import BackendThread
from login import Login

class Setip(QWidget):

    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_setip()
        self.ui.setupUi(self)

        self.ui.config_butt.clicked.connect(self.check_ip_and_port)

    def check_ip_and_port(self):
        ip = self.ui.ip_in.text()
        port = self.ui.port_in.text()

        # 验证IPv4地址格式
        ip_pattern = r"^(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.(25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)$"
        if not re.match(ip_pattern, ip):
            print("Invalid IP address.")
            QMessageBox.warning(self, 'IP地址不合法', '请输入正确的ipv4地址')
            return

        # 验证端口号范围
        try:
            port_num = int(port)
            if port_num < 0 or port_num > 65535:
                print("Port number out of valid range.")
                QMessageBox.warning(self, '端口号不合法', '请输入0-65535之间的数字')
                return
            else:
                print("IP and port are valid.")
        except ValueError:
            print("Invalid port number.")
            QMessageBox.warning(self, '端口号不合法', '请输入数字')
            return
        
        try:
            shared_module.client=Client(ip,port)
        except :
            print("连接错误")
            QMessageBox.warning(self, '连接异常', '请检查配置正确性或远程服务器工作状态')
        else:
            shared_module.listen_thread=BackendThread()
            shared_module.listen_thread.nofify.connect(shared_module.client.back_massage_handler)
            shared_module.listen_thread.start()
            shared_module.login_page=Login()
            shared_module.login_page.show()

