from PySide2 import QtWidgets
from PySide2.QtGui import QIcon

class Window(QtWidgets.QMainWindow):

    def __init__(self):

        super().__init__()
        self.resize(600,200)

        # 创建 菜单栏QMenuBar 对象 并返回
        menuBar = self.menuBar()

        # 一级菜单
        fileMenu = menuBar.addMenu("文件")
        editMenu = menuBar.addMenu("编辑")
        helpMenu = menuBar.addMenu("帮助")
        # 一级Action
        actionHomePage = menuBar.addAction('主页')
        actionHomePage.triggered.connect(self.actionHomePageClicked)

        # 一级菜单的 action项
        actionAddNode = fileMenu.addAction(QIcon("./Images/folder.png"),"添加")
        fileMenu.addSeparator() # 分隔符
        actionDelNode = fileMenu.addAction("删除")
        actionAddNode.triggered.connect(self.actionAddNodeClicked)
        actionDelNode.triggered.connect(self.actionDelNodeClicked)

        # 二级菜单
        edit_1 = editMenu.addMenu("插入图表")
        edit_2 = editMenu.addMenu("插入图片")

        # 二级菜单的 action项
        action1 = edit_1.addAction("action1")
        action2 = edit_1.addAction("action2")

    def actionHomePageClicked(self):
        print('actionHomePageClicked')

    def actionAddNodeClicked(self):
        print('actionAddNodeClicked')

    def actionDelNodeClicked(self):
        print('actionDelNodeClicked')


app = QtWidgets.QApplication([])
ex = Window()
ex.show()
app.exec_()