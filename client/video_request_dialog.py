from PySide2.QtWidgets import QWidget, QMessageBox, QApplication
from ui.video_config_ui import Ui_video_config
from lib.public import shared_module

class Video_request_dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_video_config()
        self.ui.setupUi(self)

        self.id = None
        self.ip = None

        self.ui.yes.clicked.connect(self.yes)
        self.ui.no.clicked.connect(self.no)

        self.update_info_label(self.id, self.ip)

    def update_info_label(self, id, ip):
        info_text = str(id) + "\n地址：" + str(ip) + "\n向您发送视频请求"
        self.ui.info.setText(info_text)

    def yes(self):
        #这里写同意视频请求后待发送的消息

        print("同意视频通话")
        self.close()

    def no(self):
        #这里写拒绝视频请求后待发送的消息

        print("拒绝视频通话")
        self.close()

if __name__ == "__main__":
    import sys
    app = QApplication(sys.argv)
    ip="10.0.0.1"
    id= 10005
    window = Video_request_dialog()
    window.show()
    sys.exit(app.exec_())
