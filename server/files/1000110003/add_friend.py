from PySide2.QtWidgets import QWidget, QMessageBox
from ui.add_friend_ui import Ui_add_friend
from lib.public import shared_module

class Add_friend(QWidget):
    def __init__(self):
        # 继承父类
        super().__init__()
        self.ui = Ui_add_friend()
        self.ui.setupUi(self)

        
        self.ui.add_fri_butt.clicked.connect(self.add_friend)

    def add_friend(self):
        opp_id=self.ui.id_in.text()
        opp_id=int(opp_id)
        ret=shared_module.client.user_addfriend(opp_id)
        if ret ==0:
            self.close()
        else :
            QMessageBox.warning(self,"请求发送失败","请稍后再试")