from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from login import Login
from client_fuction import Client
import threading

app = QApplication([])
if(shared_module.full_fuction):
    shared_module.client=Client()
shared_module.login_page = Login()
shared_module.login_page.show()

server_handler = threading.Thread(target=shared_module.client.server_handler(), args=(new_socket, client_address))
server_handler.start()

app.exec_()
