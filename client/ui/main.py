from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from login import Login

app = QApplication([])
shared_module.login_page = Login()
shared_module.login_page.ui.show()
app.exec_()
