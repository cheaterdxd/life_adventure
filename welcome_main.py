import sys
from PyQt5 import QtWidgets, uic

class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui,self).__init__()
        uic.loadUi('welcome_screen_gui.ui',self)
        self.start_bt.setText("text changed")
        self.show()



app = QtWidgets.QApplication(sys.argv)
windows = Ui()
app.exec_()