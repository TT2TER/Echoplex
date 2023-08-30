from PySide2.QtWidgets import QWidget, QMessageBox, QApplication
from ui.video_config_ui import Ui_video_config
from lib.public import shared_module
from video_chat_thread import VideoChatThread


class Video_request_dialog(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_video_config()
        self.ui.setupUi(self)

        self.id = None
        self.ip = None
        self.content = None

        self.ui.yes.clicked.connect(self.yes)
        self.ui.no.clicked.connect(self.no)

        self.update_info_label(self.id, self.ip, self.content)

    def update_info_label(self, id, ip, content):
        info_text = str(id) + "\n地址：" + str(ip) + "\n向您发送视频请求"
        self.ui.info.setText(info_text)
        self.content = content

    def yes(self):
        # 这里写同意视频请求后待发送的消息
        ans = "yes"
        self.ans_video_chat(ans, self.content)
        print("同意视频通话")
        ip = self.content['ip']
        shared_module.video_thread = VideoChatThread(ip)
        shared_module.video_thread.start()
        print(f"receiver开始与{ip}视频聊天啦")
        self.close()

    def no(self):
        # 这里写拒绝视频请求后待发送的消息
        ans = "no"
        self.ans_video_chat(ans, self.content)
        print("拒绝视频通话")
        self.close()


if __name__ == "__main__":
    import sys

    app = QApplication(sys.argv)
    ip = "10.0.0.1"
    id = 10005
    window = Video_request_dialog()
    window.show()
    sys.exit(app.exec_())
