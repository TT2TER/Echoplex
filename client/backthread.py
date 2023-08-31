from PySide2.QtCore import QThread, Signal, QDateTime
from PySide2.QtWidgets import QApplication, QDialog, QLineEdit
import json
from dependencies.public import shared_module
import queue


class BackendThread(QThread):
    # 通过类成员对象定义信号对象  
    notify = Signal(dict)
    self_finished = Signal(str)
    is_running = True
    e = None


    def parse_received_data_with_brackets(self, received_data):
        recv_queue = queue.Queue()
        current_json = ""
        open_brackets = 0
        for char in received_data.decode('utf-8'):
            current_json += char
            if char == '{':
                open_brackets += 1
            elif char == '}':
                open_brackets -= 1
            if open_brackets == 0:
                try:
                    json_obj = json.loads(current_json)
                    recv_queue.put(json_obj)  # 将消息放入队列
                    print("成功将消息放入队列", json_obj)
                    size = recv_queue.qsize()
                    print(f"队列中当前有{size}项")
                    current_json = ""
                except json.JSONDecodeError:
                    print("JSON decoding failed for:", current_json)
        return recv_queue

    # 处理要做的业务逻辑
    def run(self):

        while self.is_running:
            try:
                data = shared_module.client.client_socket.recv(10240)
                if not data:
                    print("接收线程断开连接")
                    break
                recv_queue = self.parse_received_data_with_brackets(data)
                while not recv_queue.empty():
                    try:
                        recv_data = recv_queue.get()
                        self.notify.emit(recv_data)
                        print("收到服务端消息：", recv_data)
                    except Exception as e:
                        print("向主线程发送信号时候退出" + str(e))

            except Exception as e:
                self.e = e
                print(str(self.e))
                self.is_running = False
        self.self_finished.emit(str(self.e))

    def stop(self):
        # 这个函数用来从外界终止这个线程
        self.is_running = False
        self.e = "normal_close"


if __name__ == '__main__':
    print("调试线程\n")
