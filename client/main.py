from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from setip import Setip
from login import Login
from window import Main_win
from register import Register

app = QApplication([])
shared_module.setip_page = Setip()
shared_module.login_page = Login()
shared_module.main_page = Main_win()
shared_module.reg_page = Register()
shared_module.setip_page.show()
if(shared_module.full_fuction):
    #shared_module.client=Client()
    pass

app.exec_()
