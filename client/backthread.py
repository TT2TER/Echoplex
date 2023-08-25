from PySide2.QtCore import QThread ,  Signal,  QDateTime 
from PySide2.QtWidgets import QApplication,  QDialog,  QLineEdit

class BackendThread(QThread):
    # 通过类成员对象定义信号对象  
	nofify = Signal(dict)
	
    # 处理要做的业务逻辑
	def run(self):
		while True:

			#以下是emit样例
			your_message= {
    			'first_name': 'John',
    			'last_name': 'Doe',
    			'age': 30,
    			'city': 'New York',
    			'email': 'john.doe@example.com'
			}
			#发射信号样例,发射信号会传到主进程，被shared_module.client.back_massage_handler处理掉
			self.nofify.emit(your_message)
			


if __name__ == '__main__':
	print("调试线程\n")