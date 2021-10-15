from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from ui_main import Ui_main
from ui_sign import Ui_sign
from lib.share import SI


class WinMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)


app = QApplication()
app.setStyle('Fusion')
SI.mainWin = WinMain()
SI.mainWin.show()
app.exec()
