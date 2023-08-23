from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module

class Main_win:

    def __init__(self):
        # 加载界面
        self.ui = QUiLoader().load('./client/ui/window.ui')
        #TODO:
