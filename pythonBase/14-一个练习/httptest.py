import traceback

from PySide6.QtWidgets import QApplication, QMainWindow, QPushButton, QPlainTextEdit, QMessageBox
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal,QObject
import re
import requests
from threading import Thread

class MySignals(QObject):
    text_print = Signal(QPlainTextEdit,str)


global_ms = MySignals()
class HTTPTest:
    def __init__(self):
        self.ui = QUiLoader().load('httptest.ui')
        self.ui.button.clicked.connect(self.sendrequest)
        self.ui.button_2.clicked.connect(self.addheader)
        self.ui.button_3.clicked.connect(self.subheader)
        self.ui.table.cellChanged.connect(self.cfgItemChanged)
        global_ms.text_print.connect(self.printInfo)
    def sendrequest(self):

        method = self.ui.comboBox.currentText()
        url = self.ui.lineEdit.text()
        data = self.ui.textEdit_2.toPlainText()

        headers = {}
        rowNumber = self.ui.table.rowCount()
        for i in range(rowNumber):
            headers[self.ui.table.item(i, 0).text()] = self.ui.table.item(i, 1).text()

        req = requests.Request(method,
                             url,
                             data=data,
                             headers=headers)


        thread = Thread(target= self.threadSend,
                        args=(req,headers,data,method))
        thread.start()
    def addheader(self):
        addRowNumber = self.ui.table.currentRow() + 1
        self.ui.table.insertRow(addRowNumber)

    def subheader(self):
        self.ui.table.removeRow(self.ui.table.currentRow())

    def cfgItemChanged(self, row, column):
        cfgName = self.ui.table.item(row, 0).text()  # 首列为配置名称
        cfgValue = self.ui.table.item(row, column).text()

    def threadSend(self,req,headers,data,method):
        self.ui.button.setEnabled(False)


        self.ui.button.setEnabled(True)
    def printInfo(self,s,prepared,method,headers,data):
        try:
            r = s.send(prepared)
            methods = method + " " + str(r.status_code) + " " + r.url + '\n'
            reheader = ''
            for key, value in r.headers.items():
                reheader += key + ":" + value + '\n'
            r.encoding = 'utf8'
            self.ui.textEdit.setPlainText(f"-----请求消息-----\n{headers}\n{data}\n-----返回消息-----\n{methods}{reheader}{r.text}")
        except:
            self.ui.textEdit.setPlainText(f"-----请求消息-----\n{headers}\n{data}\n-----返回消息-----\n{traceback.format_exc()}")
app = QApplication([])
app.setWindowIcon(QIcon('image.ico'))
httptest = HTTPTest()
httptest.ui.show()
app.exec()
