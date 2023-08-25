from PySide2.QtWidgets import QWidget, QListWidgetItem
from PySide2.QtCore import Signal, Qt
from PySide2.QtGui import QMouseEvent
import sys
from ui_listtemplate import Ui_ListTemplate  # Assuming your UI file is named "ui_listtemplate.py"

class MsgItem(QWidget):
    signal_selected = Signal(QWidget)
    signal_delete = Signal(QWidget)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_MsgItem()
        self.ui.setupUi(self)
        self.ui.btnDelete.clicked.connect(self.on_btnDeleteClicked)
        self.ui.widget.clicked.connect(self.mousePressEvent)
        self.m_header = ""
        self.m_uuid = ""

    def msg(self):
        return self.ui.labelMsg.text()

    def setMsg(self, msg):
        self.ui.labelMsg.setText(msg)

    def header(self):
        return self.m_header

    def setHeader(self, header):
        self.m_header = header

    def uuid(self):
        return self.m_uuid

    def setUuid(self, uuid):
        self.m_uuid = uuid

    def name(self):
        return self.ui.labelName.text()

    def setName(self, name):
        self.ui.labelName.setText(name)

    def datetime(self):
        return self.ui.labelDatetime.text()

    def setDatetime(self, datetime):
        self.ui.labelDatetime.setText(datetime)

    def count(self):
        return int(self.ui.labelCount.text())

    def setCount(self, count):
        self.ui.labelCount.setText(str(count))

    def setData(self, msg, nick, header, name, time):
        self.setMsg(msg)
        self.setName(nick)
        self.setHeader(header)
        self.setUuid("")
        self.setDatetime(time)

    def selected(self, selected):
        self.ui.widget.setSelected(selected)

    def mousePressEvent(self, event):
        self.signal_selected.emit(self)

    def on_btnDeleteClicked(self):
        self.signal_delete.emit(self)


class ListTemplate(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = Ui_ListTemplate()
        self.ui.setupUi(self)
        self.ui.btnAdd.clicked.connect(self.on_btnAddClicked)
        self.ui.listWidget.itemClicked.connect(self.on_listWidgetClicked)
        self.m_pCurrentItem = None
        self.m_pCurrent = None

    def AddWidgetMsgItem(self):
        msg_item = MsgItem()
        list_item = QListWidgetItem(self.ui.listWidget)
        list_item.setSizeHint(msg_item.sizeHint())
        self.ui.listWidget.setItemWidget(list_item, msg_item)
        msg_item.signal_selected.connect(self.slot_selected)
        msg_item.signal_delete.connect(self.slot_delete)

    # ... (slot_selected, slot_delete, on_listWidgetClicked, on_btnAddClicked remain the same)

if __name__ == "__main__":
    from PySide2.QtWidgets import QApplication
    app = QApplication(sys.argv)
    window = ListTemplate()
    window.show()
    sys.exit(app.exec_())