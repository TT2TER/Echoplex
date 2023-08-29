import sys
from PySide2.QtWidgets import QApplication, QWidget, QVBoxLayout, QProgressBar, QPushButton

class Progress_bar(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Progress Bar Example")
        self.setGeometry(100, 100, 300, 150)

        self.layout = QVBoxLayout(self)

        self.progress_bar = QProgressBar(self)
        self.layout.addWidget(self.progress_bar)

        self.update_button = QPushButton("返回,但不终止文件传输", self)
        self.layout.addWidget(self.update_button)
        self.update_button.clicked.connect(self.close())

        self.percentage = 0

    def update_percentage(self,percentage):

        self.progress_bar.setValue(self.percentage)
        self.percentage_show(self.percentage)
        print(percentage)

    def percentage_show(self, percentage):
        print(f"Current Percentage: {percentage}%")

    def close_progress_bar(self):
        self.close()
def main():
    app = QApplication(sys.argv)
    widget = Progress_bar()
    widget.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
