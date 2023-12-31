
       
from PySide2.QtGui import QMouseEvent
from PySide2.QtCore import Qt


        self.setWindowFlags(Qt.FramelessWindowHint)
        self.ui.close_butt.clicked.connect(self.close_win)
        self.ui.mini_butt.clicked.connect(self.minimize_win)


        #以下函数是移动窗口用的
    def mousePressEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = True
            self.offset = event.globalPos() - self.pos()

    def mouseMoveEvent(self, event: QMouseEvent):
        if self.dragging:
            self.move(event.globalPos() - self.offset)

    def mouseReleaseEvent(self, event: QMouseEvent):
        if event.button() == Qt.LeftButton:
            self.dragging = False

    #以下是关窗口函数
    def close_win(self):
        self.close()
        shared_module.app.quit()
    def minimize_win(self):
        #这个是最小化窗口函数
        self.showMinimized()


        where=self.pos()
        #print(where)
        shared_module.reg_page.move(where)

        screen_geometry = shared_module.app.desktop().screenGeometry()
            setip_geometry = shared_module.main_page.geometry()
            center_x = (screen_geometry.width() - setip_geometry.width()) / 2
            center_y = (screen_geometry.height() - setip_geometry.height()) / 2
            shared_module.main_page.move(center_x, center_y)