from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import Qt
from PySide2.QtGui import QMouseEvent,QPixmap
from dependencies.public import shared_module
from ui.setip_ui import Ui_setip
from client_fuction import Client
from backthread import BackendThread
import re, os

class Setip(QWidget):

    def __init__(self):
        # 继承父类
        super().__init__()
        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui = Ui_setip()
        self.ui.setupUi(self)

        self.ui.config_butt.clicked.connect(self.check_ip_and_port)
        self.ui.close_butt.clicked.connect(self.close_win)
        self.ui.mini_butt.clicked.connect(self.minimize_win)

        img_path = "dependencies/icon.png"
        image_path=os.path.join(os.path.dirname(__file__), img_path)
        pixmap = QPixmap(image_path)
        self.ui.icon.setPixmap(pixmap)
        self.ui.icon.setScaledContents(True)  # 图像自动拉伸

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
            shared_module.listen_thread.notify.connect(shared_module.client.back_massage_handler)
            shared_module.listen_thread.self_finished.connect(self.on_thread_finnished)
            #shared_module.listen_thread.stop()用来在任何地方终止这个线程
            shared_module.listen_thread.start()
            print("listen_thread start")
            where=self.pos()#print(where)
            shared_module.client.auto_login()
            shared_module.login_page.move(where)
            shared_module.login_page.show()
            print("在setupip这里可能出bug")
            self.close()
    def on_thread_finnished(self,e):
        shared_module.listen_thread.quit()
        shared_module.listen_thread.wait()
        if shared_module.listen_thread.isRunning():
            shared_module.listen_thread.stop()
            print("再次尝试关闭线程\n这辈子都不应该看到这句话才对，看到了这里就还是有问题")
        else:
            print("线程已经关闭")

        if e == "normal_close":
            #这里是万一有人想关闭线程但是不关闭程序...e就是返回的normal
            pass
        else: 
            #那就是断网了，直接关闭程序//可以尝试再次联网
            self.network_disconnect(e)
    def network_disconnect(self,e):
            print("您和服务器断开连接了\n")
            QMessageBox.warning(self,'已经和服务器断开连接','即将自动关闭程序，请重新启动程序\n错误代码:'+str(e))
            shared_module.app.quit()

