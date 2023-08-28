import sys
from PySide2.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout
from PySide2.QtCore import Qt, Signal, QRect
from ui.chat_bubble_opp_ui import Ui_chat_bubble_opp
from ui.chat_bubble_me_ui import Ui_chat_bubble_me
from PySide2.QtGui import QTextDocument, QPixmap
from datetime import datetime
from lib.public import shared_module
import os

class Message_bubble(QWidget):
    # 只用来定义 message_bubble 的行为
    selected = Signal(str)

    def __init__(self, sender_id,name,avatar_path, time, msg):
        super().__init__()
        
        if sender_id== shared_module.client.user_id:
            self.ui = Ui_chat_bubble_me()
            self.ui.setupUi(self)
        else :
            self.ui = Ui_chat_bubble_opp()
            self.ui.setupUi(self)
            
        self.time = time
        self.msg = msg
        self.name = name


        self.padding=10#如果在样式表里更改了，记得改这里
        self.ui.message_bubble.setAlignment(Qt.AlignLeft | Qt.AlignTop)
        self.ui.message_bubble.setWordWrap(True)  # 自动换行
        self.ui.message_bubble.setText(self.msg)
        
        
        # 计算文本在最大宽度下的矩形区域
        # 使用字体度量来获取文本在给定宽度内的渲染区域，考虑到自动换行和内边距的影响
        content_rect = self.ui.message_bubble.fontMetrics().boundingRect(0, 0, 500 - (2 * self.padding), 0, Qt.TextWordWrap, self.msg)
        # 计算适合的宽度，考虑了内边距的影响
        content_width = min(content_rect.width() + (2 * self.padding), 500)+ (2 * self.padding)
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
        image = QPixmap(avatar_path)  # 用实际的图像路径替换
        self.avatar_label.setPixmap(image)
        self.avatar_label.setScaledContents(True)  # 自适应图像大小

        #顯示發件人
        self.ui.who.setText(str(self.name))

        self.ui.message_bubble.mousePressEvent = self.toggle_selection  # 替换点击事件


    def toggle_selection(self, event):
        if self.ui.message_bubble.property("selected") == "true":
            self.ui.message_bubble.setProperty("selected", "false")
        else:
            self.ui.message_bubble.setProperty("selected", "true")
        self.ui.message_bubble.style().unpolish(self.ui.message_bubble)
        self.ui.message_bubble.style().polish(self.ui.message_bubble)
        self.ui.message_bubble.update()

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # 获取当前时间
    current_time = datetime.now()

    # 格式化为字符串
    time_string = current_time.strftime("%Y-%m-%d %H:%M:%S")
    
    img_path = "lib/login_back.png"
    image_path=os.path.join(os.path.dirname(__file__), img_path)
    
    who="others"
    demo = Message_bubble(who,image_path, time_string, "这是一条测试消息，长消息测试哈啊哈哈哈哈哈哈哈哈哈哈哈哈哈哈皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后皇后")
    demo.show()
    sys.exit(app.exec_())
