from PySide2.QtWidgets import QApplication, QMessageBox, QWidget
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from ui.window_ui import Ui_chat

class Main_win(QWidget):

    def __init__(self):
        super().__init__()
        self.ui= Ui_chat()
        self.ui.setupUi(self)
        #TODO:
