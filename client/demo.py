from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide2.QtGui import QPixmap, QPainter, QBrush, QColor
from PySide2.QtCore import Qt
import sys,os

class CircularAvatarLabel(QLabel):
    def __init__(self, image_path, parent=None):
        super().__init__(parent)
        self.setFixedSize(48, 48)
        self.setStyleSheet("border-radius: 24px; border: 1px solid #AAAAAA;")
        self.setPixmap(self.create_round_avatar(image_path))

    def create_round_avatar(self, image_path):
        pixmap = QPixmap(image_path)
        rounded_pixmap = QPixmap(48, 48)
        rounded_pixmap.fill(Qt.transparent)

        painter = QPainter(rounded_pixmap)
        painter.setRenderHint(QPainter.Antialiasing)
        brush = QBrush(pixmap)
        painter.setBrush(brush)
        painter.drawEllipse(0, 0, 48, 48)
        painter.end()

        return rounded_pixmap

if __name__ == "__main__":
    app = QApplication(sys.argv)

    widget = QWidget()
    layout = QVBoxLayout()
    img_path = "lib/login_back.png"
    image_path=os.path.join(os.path.dirname(__file__), img_path)
    avatar_label = CircularAvatarLabel(image_path)  # 替换为实际图像路径
    layout.addWidget(avatar_label)

    widget.setLayout(layout)
    widget.show()

    sys.exit(app.exec_())
