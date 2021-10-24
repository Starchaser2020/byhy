from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore
from ui_main import Ui_main
from ui_sign import Ui_sign
from lib.share import SI
import requests


class WinMain(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_main()
        self.ui.setupUi(self)
        self.ui.actionExit.triggered.connect(self.exit)

    def exit(self):
        SI.mainWin.close()
        SI.loginWin.show()
        SI.loginWin.ui.lineEdit_2.clear()


class WinLogin(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_sign()
        self.ui.setupUi(self)
        self.ui.buttonSign.clicked.connect(self.sign)

    def sign(self):
        url = 'http://192.168.56.103/api/sign'
        re = requests.post(url, json={
            "action": "signin",
            "username": "byhy",
            "password": "sdfsdf"
        })
        if re.json()['ret'] == 0:
            SI.loginWin.close()
            SI.mainWin.show()
        else:
            QMessageBox.critical(
                self,
                '登陆失败',
                re.json()['msg'])


app = QApplication()
# app.setStyle('Fusion')
SI.mainWin = WinMain()
SI.loginWin = WinLogin()
SI.loginWin.show()
app.exec()
