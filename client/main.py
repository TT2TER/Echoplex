from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from setip import Setip

app = QApplication([])
shared_module.setip_page = Setip()
shared_module.setip_page.show()
if(shared_module.full_fuction):
    #shared_module.client=Client()
    pass

app.exec_()
