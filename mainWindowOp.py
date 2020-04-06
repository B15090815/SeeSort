from PyQt5.QtWidgets import QMainWindow

from mainWindow import Ui_MainWindow
from showGroundOp import showGroundOp


class MainWindowOp(QMainWindow, Ui_MainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)

        self.widget = None
        self.ensure.clicked.connect(self.click_ensure)

    def click_ensure(self):
        sort_num = self.sort_range.text()
        if sort_num is None or sort_num == '':
            sort_num = 50
        else:
            sort_num = int(sort_num)
        index = self.sort_combo.currentIndex()
        self.widget = showGroundOp(index, sort_num, 0.1)
        self.widget.show()
