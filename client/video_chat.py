import cv2
from socket import *
import threading
import pyaudio
import zlib
import struct
import pickle
import time


def show_myself():
    cap = cv2.VideoCapture(0)  # 打开摄像头，参数0表示默认摄像头
    while True:
        ret, frame = cap.read()  # 读取摄像头捕捉的帧
        if not ret:
            print("无法捕获帧，可能摄像头未连接或不可用")
            break
        cv2.imshow('Camera', frame)  # 显示帧内容
        # 按下ESC键退出循环
        if cv2.waitKey(1) & 0xFF == 27:
            break
    cap.release()  # 释放摄像头
    cv2.destroyAllWindows()  # 关闭所有窗口


class Video_Server(threading.Thread):
    def __init__(self, port, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.ADDR = ('', port)
        if version == 4:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = socket(AF_INET6, SOCK_STREAM)

    def __del__(self):
        self.sock.close()
        try:
            cv2.destroyAllWindows()
        except:
            pass

    def run(self):
        print("VIDEO server starts...")
        self.sock.bind(self.ADDR)
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        print("remote VIDEO client success connected...")
        data = "".encode("utf-8")
        payload_size = struct.calcsize("L")  # 结果为4
        cv2.namedWindow('Remote', cv2.WINDOW_NORMAL)
        while True:
            while len(data) < payload_size:
                data += conn.recv(81920)
            packed_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_size)[0]
            while len(data) < msg_size:
                data += conn.recv(81920)
            zframe_data = data[:msg_size]
            data = data[msg_size:]
            frame_data = zlib.decompress(zframe_data)
            frame = pickle.loads(frame_data)
            cv2.imshow('Remote', frame)
            # show_myself()
            if cv2.waitKey(1) & 0xFF == 27:
                break


class Video_Client(threading.Thread):
    def __init__(self ,ip, port, level, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.ADDR = (ip, port)
        if level <= 3:
            self.interval = level
        else:
            self.interval = 3
        self.fx = 1 / (self.interval + 1)
        if self.fx < 0.3:	# 限制最大帧间隔为3帧
            self.fx = 0.3
        if version == 4:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = socket(AF_INET6, SOCK_STREAM)
        self.cap = cv2.VideoCapture(0)

    def __del__(self) :
        self.sock.close()
        self.cap.release()

    def run(self):
        print("VIDEO client starts...")
        while True:
            try:
                self.sock.connect(self.ADDR)
                break
            except:
                time.sleep(3)
                continue
        print("VIDEO client connected...")

        cv2.namedWindow('Client', cv2.WINDOW_NORMAL)  # 创建一个窗口

        while self.cap.isOpened():
            ret, frame = self.cap.read()

            if not ret:
                print("无法捕获帧，可能摄像头未连接或不可用")
                break

            # 显示摄像头捕捉的实时内容
            # cv2.imshow('Client', frame)

            sframe = cv2.resize(frame, (0,0), fx=self.fx, fy=self.fx)
            cv2.imshow('Client', sframe)
            data = pickle.dumps(sframe)
            zdata = zlib.compress(data, zlib.Z_BEST_COMPRESSION)
            try:
                self.sock.sendall(struct.pack("L", len(zdata)) + zdata)
            except:
                break
            for i in range(self.interval):
                self.cap.read()

            if cv2.waitKey(1) & 0xFF == 27:
                break

        cv2.destroyAllWindows()  # 关闭窗口



CHUNK = 1024
FORMAT = pyaudio.paInt16  # 格式
CHANNELS = 2  # 输入/输出通道数
RATE = 44100  # 音频数据的采样频率
RECORD_SECONDS = 0.5  # 记录秒


class Audio_Server(threading.Thread):
    def __init__(self, port, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.ADDR = ('', port)
        if version == 4:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = socket(AF_INET6, SOCK_STREAM)
        self.p = pyaudio.PyAudio()  # 实例化PyAudio,并于下面设置portaudio参数
        self.stream = None

    def __del__(self):
        self.sock.close()  # 关闭套接字
        if self.stream is not None:
            self.stream.stop_stream()  # 暂停播放 / 录制
            self.stream.close()  # 终止流
        self.p.terminate()  # 终止会话

    def run(self):
        print("Video server starts...")
        self.sock.bind(self.ADDR)
        self.sock.listen(1)
        conn, addr = self.sock.accept()
        print("remote Video client success connected...")
        data = "".encode("utf-8")
        payload_size = struct.calcsize("L")  # 返回对应于格式字符串fmt的结构，L为4
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  output=True,
                                  frames_per_buffer=CHUNK
                                  )
        while True:
            while len(data) < payload_size:
                data += conn.recv(81920)
            packed_size = data[:payload_size]
            data = data[payload_size:]
            msg_size = struct.unpack("L", packed_size)[0]
            while len(data) < msg_size:
                data += conn.recv(81920)
            frame_data = data[:msg_size]
            data = data[msg_size:]
            frames = pickle.loads(frame_data)
            for frame in frames:
                self.stream.write(frame, CHUNK)


class Audio_Client(threading.Thread):
    def __init__(self, ip, port, version):
        threading.Thread.__init__(self)
        self.setDaemon(True)
        self.ADDR = (ip, port)
        if version == 4:
            self.sock = socket(AF_INET, SOCK_STREAM)
        else:
            self.sock = socket(AF_INET6, SOCK_STREAM)
        self.p = pyaudio.PyAudio()
        self.stream = None
        print("AUDIO client starts...")

    def __del__(self):
        self.sock.close()
        if self.stream is not None:
            self.stream.stop_stream()
            self.stream.close()
        self.p.terminate()

    def run(self):
        while True:
            try:
                self.sock.connect(self.ADDR)
                break
            except:
                time.sleep(3)
                continue
        print("AUDIO client connected...")
        self.stream = self.p.open(format=FORMAT,
                                  channels=CHANNELS,
                                  rate=RATE,
                                  input=True,
                                  frames_per_buffer=CHUNK)
        while self.stream.is_active():
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = self.stream.read(CHUNK)
                frames.append(data)
            senddata = pickle.dumps(frames)
            try:
                self.sock.sendall(struct.pack("L", len(senddata)) + senddata)
            except:
                break
