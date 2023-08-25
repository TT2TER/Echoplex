from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from login import Login
from client_fuction import Client
from backthread import BackendThread

app = QApplication([])
if(shared_module.full_fuction):
    shared_module.client=Client()
    shared_module.listen_thread=BackendThread()
    shared_module.listen_thread.nofify.connect(shared_module.client.back_massage_handler)
    shared_module.listen_thread.start()
shared_module.login_page = Login()
shared_module.login_page.show()
app.exec_()
