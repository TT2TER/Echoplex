import sys
import time
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QThread, Signal, QObject
from video_chat import Video_Server, Video_Client, Audio_Server, Audio_Client


# 选中Remote，按Esc退出！！！
class VideoChatThread(QThread):
    finished = Signal()

    def __init__(self, ip, port=15423, level=1, version=4):
        super().__init__()
        try:
            print("开始初始化")
            self.ip = ip
            self.port = port
            self.version = version
            self.level = level
            print("初始化完成")
        except Exception as e:
            print("file_thread初始化寄了" + str(e))

    def run(self):
        vclient = Video_Client(self.ip, self.port, self.level, self.version)
        vserver = Video_Server(self.port, self.version)
        aclient = Audio_Client(self.ip, self.port + 1, self.version)
        aserver = Audio_Server(self.port + 1, self.version)

        vclient.start()
        aclient.start()
        time.sleep(1)  # make delay to start server
        vserver.start()
        aserver.start()

        while vserver.is_running:
            time.sleep(1)
            if not vserver.is_alive() or not vclient.is_alive() or \
                    not aserver.is_alive() or not aclient.is_alive():
                break

# def on_thread_finished():
#     print("Thread finished")
#     sys.exit(0)


# class App(QObject):
#     def __init__(self, ip, port=15423, level=1, version=4):
#         super().__init__()
#         self.thread = VideoChatThread(ip, port, level, version)
#         self.thread.finished.connect(on_thread_finished)
#         self.thread.start()


# if __name__ == '__main__':
#     ip = '127.0.0.1'
#     print("test1")
#     vt = VideoChatThread(ip)
#     print("test2")
#     vt.start()
#     print("test3")
#     vt.wait()
