import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout,QPushButton, QProgressBar
from PySide2.QtCore import Qt, Signal, QRect
from ui.chat_bubble_opp_ui import Ui_chat_bubble_opp
from ui.chat_bubble_me_ui import Ui_chat_bubble_me
from ui.file_bubble_ui import Ui_file_bubble
from PySide2.QtGui import QTextDocument, QPixmap
from datetime import datetime
from dependencies.public import shared_module
import os
import time

class Message_bubble(QWidget):
    # 只用来定义 message_bubble 的行为
    selected = Signal(str)

    def __init__(self, content):
        super().__init__()

        self.sender_id=content["sender"]
        self.chat_id=content["chat_id"]
        self.msg=content["msg"]
        timestamp=int(content["time"])
        timearray = time.localtime(timestamp)
        self.time= time.strftime("%Y-%m-%d %H:%M:%S", timearray)
        self.file_path=content["filepath"]
        self.file_size=content["filesize"]

        self.sender_name=None

        self.image_path=None
        self.find_avatar(self.sender_id)
        #這個是消息框最大長度
        self.max_leth=0
        #是不是文件
        self.is_file=False
        #這裡是標記這個文件是否需要接收
        self.need_recive=False
        #这里标记这个文件是需要进度条
        self.need_progress=None

        if self.file_path == None:
            self.max_leth=500
            self.is_file=False
            #如果是文字消息
            if self.sender_id== shared_module.client.user_id:
                #如果發件人是自己
                self.sender_name=shared_module.client.user_name
                self.ui = Ui_chat_bubble_me()
                self.ui.setupUi(self)
            else :
                #如果發件人是對方
                if len(str(self.chat_id))==10:
                    self.sender_name=shared_module.client.find_name(self.chat_id)
                else:
                    self.sender_name=str(self.sender_id)
                self.ui = Ui_chat_bubble_opp()
                self.ui.setupUi(self)
        else:
            #如果是文件消息
            self.is_file=True
            self.max_leth=300
            self.ui=Ui_file_bubble()
            self.ui.setupUi(self)
            if self.sender_id== shared_module.client.user_id:
                self.sender_name=shared_module.client.user_name
                #不需要接收
                self.need_recive=False
                if shared_module.main_page.is_old:
                    self.need_progress=False
                else:
                    self.need_progress=True
            else :
                if len(str(self.chat_id)) == 10 :
                    self.sender_name=shared_module.client.find_name(self.chat_id)
                    #需要接受
                    self.need_recive=True
                    #这里如果能加一个本地是否有这个文件的判断就好了，现在暂时认为所有文件都没有，所以要有进度条
                    self.need_progress=True
                else:
                    self.sender_name = str(self.sender_id)
                    self.need_recive = True
                    self.need_progress = True
        #如果是文件改變消息內容
        if self.is_file:
            if self.need_recive:
                self.msg="收到"+self.sender_name+"發送的文件："+self.file_path+"點擊右側接收"
                self.file_button = QPushButton("接收文件", self)
                self.file_button.setGeometry(480, 100, 111, 41)
                self.file_button.setStyleSheet('''
                    QPushButton {
                        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #D988FF, stop:1 #AF7AC5);
                        color: white;
                        border: 1px solid #8e44ad;
                        border-radius: 5px;
                        padding: 5px 10px;
                    }
                    QPushButton:hover {
                        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #AF7AC5, stop:1 #8E44AD);
                        border: 1px solid #8e44ad;
                    }
                    QPushButton:pressed {
                        background: qlineargradient(spread:pad, x1:0, y1:0, x2:1, y2:0, stop:0 #7D3C98, stop:1 #6C3483);
                        border: 1px solid #6c3483;
                    }
                ''')
                # 连接按钮点击事件到 self.receive_file 函数
                self.file_button.clicked.connect(self.receive_file)

            else:
                self.msg="發送的文件："+self.file_path+"發送成功"

        if self.is_file and self.need_progress and not self.need_recive:
            self.progress_bar = QProgressBar(self)
            self.progress_bar.setGeometry(480, 150, 111, 20)  # 调整进度条位置和大小
            self.progress_bar.setRange(0, 100)  # 设置进度范围
            self.progress_bar.setValue(0)  # 初始进度值

        # if self.is_file and self.need_progress and self.need_recive:
        #     shared_module.main_page.add_percentage_bar("test")


        self.padding=10#如果在样式表里更改了，记得改这里
        self.ui.message_bubble.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.ui.message_bubble.setWordWrap(True)  # 自动换行
        self.ui.message_bubble.setText(self.msg)
        
        
        # 计算文本在最大宽度下的矩形区域
        # 使用字体度量来获取文本在给定宽度内的渲染区域，考虑到自动换行和内边距的影响
        content_rect = self.ui.message_bubble.fontMetrics().boundingRect(0, 0, self.max_leth - (2 * self.padding), 0, Qt.TextWordWrap, self.msg)
        # 计算适合的宽度，考虑了内边距的影响
        content_width = min(content_rect.width() + (2 * self.padding), self.max_leth)+ (2 * self.padding)
        # 获取文本在上述宽度下的实际高度
        content_height = content_rect.height()
        # 计算消息气泡的总高度，考虑了内边距
        total_content_height = content_height + (2 * self.padding)+ 10
        # 设置气泡的最终大小，考虑内边距和一些额外的高度余量
        self.ui.message_bubble.setFixedSize(content_width , total_content_height )

        #设置外框大小
        self.ui.widgetMain.setFixedSize(800,total_content_height+100)
        #self.ui.setFixedSize(content_width+10,total_content_height+10)

        #显示发消息时间
        self.ui.cur_time.setText(self.time)
        self.ui.cur_time.setFixedSize(self.ui.cur_time.fontMetrics().width(self.time)+20,30)

        #显示头像
        self.avatar_label = QLabel(self.ui.avatar)
        self.avatar_label.setGeometry(QRect(1, 1, 48, 48))
        image = QPixmap(self.image_path)  # 用实际的图像路径替换
        self.avatar_label.setPixmap(image)
        self.avatar_label.setScaledContents(True)  # 自适应图像大小

        #顯示發件人
        self.ui.who.setText(str(self.sender_name))

        self.ui.message_bubble.mousePressEvent = self.toggle_selection  # 替换点击事件

    # def find_avartar(self,id):
    #     """这里写一个找头像路径的函数，下面先用测试路径"""
    #     self.img_path = "dependencies/login_back.png"
    #     self.image_path=os.path.join(os.path.dirname(__file__), self.img_path)
    #     pass
    def find_avatar(self, id):
        """Find the avatar path based on the given ID."""
        supported_extensions = ['jpg', 'jpeg', 'png']
        
        # Search for avatar files with supported extensions
        for ext in supported_extensions:
            avatar_filename = f"{id}.{ext}"
            avatar_path = os.path.join(os.path.dirname(__file__), "files/avatar/", avatar_filename)
            
            if os.path.exists(avatar_path):
                self.image_path=avatar_path
            else:
                # If no avatar found, return a default avatar path
                self.image_path = os.path.join(os.path.dirname(__file__), "dependencies/login_back.png")


    def toggle_selection(self, event):
        if self.ui.message_bubble.property("selected") == "true":
            self.ui.message_bubble.setProperty("selected", "false")
        else:
            self.ui.message_bubble.setProperty("selected", "true")
        self.ui.message_bubble.style().unpolish(self.ui.message_bubble)
        self.ui.message_bubble.style().polish(self.ui.message_bubble)
        self.ui.message_bubble.update()
    
    def receive_file(self):
        print("接收文件函数被调用了")
        shared_module.client.receive_file_request(self.chat_id,self.file_path)
        if self.is_file and self.need_progress and self.need_recive:
            shared_module.main_page.add_percentage_bar("test")
        pass

    



    def update_progress(self, percentage):
        if self.is_file :
            self.progress_bar.setValue(percentage)
        
if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 获取当前时间
    current_time = datetime.now()

    # 格式化为字符串
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    img_path = "dependencies/login_back.png"
    image_path=os.path.join(os.path.dirname(__file__), img_path)
    
    who="others"
    demo = Message_bubble(who,image_path, time_string, "这是一条测试消息，长消息测试哈啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后")
    demo.show()
    sys.exit(app.exec_())
