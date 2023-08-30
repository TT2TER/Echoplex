from PySide2.QtWidgets import QApplication, QMessageBox
from PySide2.QtUiTools import QUiLoader
from lib.public import shared_module
from setip import Setip
from login import Login
from window import Main_win
from add_friend import Add_friend
from new_friend import New_friends
from register import Register
from progress_bar import Progress_bar
from new_group import New_group
from manage_group import Manage_group
from video_request_dialog import Video_request_dialog

shared_module.app = QApplication([])
shared_module.setip_page = Setip()
shared_module.login_page = Login()
shared_module.main_page = Main_win()
shared_module.reg_page = Register()
shared_module.add_friend=Add_friend()
shared_module.new_friends=New_friends()
shared_module.progress_bar = Progress_bar()
shared_module.new_group= New_group()
shared_module.manage_group = Manage_group()
shared_module.video_page = Video_request_dialog()
screen_geometry = shared_module.app.desktop().screenGeometry()
setip_geometry = shared_module.setip_page.geometry()
center_x = (screen_geometry.width() - setip_geometry.width()) / 2
center_y = (screen_geometry.height() - setip_geometry.height()) / 2
shared_module.setip_page.move(center_x, center_y)
# Show the setip_page
shared_module.setip_page.show()
shared_module.setip_page.show()
if(shared_module.full_fuction):
    #shared_module.client=Client()
    pass

shared_module.app.exec_()
