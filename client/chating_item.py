from PySide2.QtWidgets import QWidget
from PySide2.QtWidgets import QLabel
from PySide2.QtGui import QPixmap
from PySide2.QtCore import Signal, Qt, QRect
from ui.chating_item_ui import Ui_chating_item
from dependencies.public import shared_module
import time,os


class Chating_item(QWidget):

    itemClicked = Signal(int)  # 自定义信号，用于发出项被点击的信号

    def __init__(self, content, parent=None):
        super().__init__(parent)

        self.ui = Ui_chating_item()
        self.ui.setupUi(self)

        self.sender_id=content["sender"]

        self.chat_id=content["chat_id"]

        self.msg=content["msg"]

        timestamp=int(content["time"])
        timearray = time.localtime(timestamp)
        self.time= time.strftime("%Y-%m-%d %H:%M:%S", timearray)

        self.file_path=content["filepath"]
        self.file_size=content["filesize"]

        self.image_path = None
        if len(str(self.chat_id))==10:
            self.name=shared_module.client.find_name(self.chat_id)
            self.opp_id = shared_module.client.find_oppid(self.chat_id)
            self.find_avatar(self.opp_id)
        else:
            self.name=shared_module.client.find_group_name(self.chat_id)
            self.image_path = os.path.join(os.path.dirname(__file__), "dependencies/group.png")





        # 初始化更新姓名
        self.ui.name.setText(self.name)
        self.ui.message_time.setText(self.time)  
        # 初始化头像
        self.avatar_label = QLabel(self.ui.avatar)
        self.avatar_label.setGeometry(QRect(0, 0, 48, 48))
        self.avatar_label.setStyleSheet(
            u"background-color: transparent; border-radius: 6px;")
        image = QPixmap(self.image_path)  # 用实际的图像路径替换
        self.avatar_label.setPixmap(image)
        self.avatar_label.setScaledContents(True)  # 自适应图像大小
        self.ui.resent_message.setText(self.msg)

        self.hide_message_red()


#以下按鍵功能僅供測試時使用，測試完畢後請在這裡和ui里刪除這個按鈕
    #     self.ui.close_butt.clicked.connect(self.close)
    # def close(self):
    #     print("clicked")
    #     shared_module.main_page.del_one_list(self.chat_id)
    #     pass
#以上是測試用

    def show_message_red(self):
        self.ui.new_message.show()

    def hide_message_red(self):
        self.ui.new_message.hide()

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            print("Widget clicked")
            # 在这里可以执行选中效果的操作，例如修改颜色、样式等
            self.hide_message_red()
            #TODO: 最好選中一次後就不能再選中了，點擊到別人再不選中
            self.itemClicked.emit(self.chat_id)

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
