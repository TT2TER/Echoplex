import sys
import os
import subprocess
from PySide2.QtWidgets import QApplication, QMainWindow, QPushButton, QFileDialog, QTextBrowser
from PySide2.QtCore import Qt

class FileDialogExample(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setGeometry(100, 100, 300, 200)
        self.setWindowTitle('File Dialog Example')

        self.button = QPushButton('Open File', self)
        self.button.setGeometry(100, 50, 100, 30)
        self.button.clicked.connect(self.show_file_dialog)

        self.text_browser = QTextBrowser(self)
        self.text_browser.setGeometry(20, 100, 260, 60)
        self.text_browser.setOpenExternalLinks(True)
        self.text_browser.setAlignment(Qt.AlignCenter)
        self.text_browser.setOpenExternalLinks(True)
        self.text_browser.setOpenLinks(True)
        self.text_browser.setReadOnly(True)

    def show_file_dialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly

        file_name, _ = QFileDialog.getOpenFileName(self, 'Open File', '', 'All Files (*)', options=options)

        if file_name:
            print('Selected File:', file_name)
            base_name = os.path.basename(file_name)
            file_extension = os.path.splitext(base_name)[1]
            dir_name = os.path.dirname(file_name)  # 获取文件所在目录
            display_text = (
                f'文件名：{base_name}<br>'
                f'文件类型：{file_extension}<br>'
                f'<a href="dir:{dir_name}">打开文件所在路径</a>'
            )
            self.update_label(display_text)

    def update_label(self, text):
        self.text_browser.setHtml(text)

    def open_directory(self, link):
        if link.startswith('dir:'):
            dir_path = link[4:]  # 去除 "dir:" 前缀
            if sys.platform.startswith('win'):
                os.startfile(dir_path)  # 适用于Windows系统
            elif sys.platform.startswith('darwin'):
                os.system(f'open "{dir_path}"')  # 适用于macOS系统
            else:
                try:
                    subprocess.run(['xdg-open', dir_path])
                except FileNotFoundError:
                    print("No suitable command found to open directory.")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = FileDialogExample()
    ex.show()
    sys.exit(app.exec_())
