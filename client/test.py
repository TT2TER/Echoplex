from PySide2.QtWidgets import QApplication, QWidget
from PySide2.QtGui import QPixmap,QPaintEvent, QPainter
from PySide2.QtCore import Qt
import os

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.img_path = "lib/login_back.png"  # Replace with the actual path to your image
        self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
    def paintEvent(self, event: QPaintEvent):
        painter = QPainter(self)
        painter.setRenderHint(QPainter.Antialiasing)

        pixmap = QPixmap(self.image_path)
        scaled_pixmap = pixmap.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        x_offset = (self.width() - scaled_pixmap.width()) / 2
        y_offset = (self.height() - scaled_pixmap.height()) / 2
        painter.drawPixmap(x_offset, y_offset, scaled_pixmap)

    def resizeEvent(self, event):
        self.update()
        super().resizeEvent(event)

if __name__ == "__main__":
    app = QApplication([])
    window = MyWindow()
    window.show()
    app.exec_()
