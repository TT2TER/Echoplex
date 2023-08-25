from PySide2.QtCore import QThread, Signal, QDateTime
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit
import time
import sys

class BackendThread(QThread):
    update_date = Signal(str)
    
    def run(self):
        while True:
            data = QDateTime.currentDateTime()
            currTime = data.toString("yyyy-MM-dd hh:mm:ss")
            
            self.update_date.emit(str(currTime))
            time.sleep(1)

class Window(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        self.setWindowTitle('PyQt5界面实时更新例子')
        self.resize(400, 100)
        self.input = QLineEdit(self)
        self.input.resize(400, 100)
        self.initUI()

    def initUI(self):
        self.backend = BackendThread()
        self.backend.update_date.connect(self.handleDisplay)  # 修正连接的槽函数名
        self.backend.start()

    def handleDisplay(self, data):
        self.input.setText(data)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    win = Window()
    win.show()
    sys.exit(app.exec_())
