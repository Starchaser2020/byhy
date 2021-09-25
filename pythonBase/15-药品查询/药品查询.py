import MySQLdb
# conn = MySQLdb.connect(
#     host='127.0.0.1',
#     user='root',
#     passwd='root',
#     db='prac',
#     charset="utf8"
# )
# cursor = conn.cursor()
# sql = """
# CREATE TABLE medicines(
# id INT auto_increment primary key,
# name varchar(150) not null ,
# `index` varchar(150) not null,
# `desc` varchar(150) not null
# )ENGINE=innodb default charset=utf8;
# """
# cursor.execute(sql)
# for x in range(100):
#     cursor.execute(f"insert into medicines(name,`index`,`desc`) values ('青霉素{x}','编号{x}','描述')")
# conn.commit()
import traceback

from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon
from PySide6.QtCore import Signal, QObject
from PySide6 import QtCore
import re
import requests
from threading import Thread


class MySignals(QObject):
    pagechange = Signal(QTableWidget)


global_ms = MySignals()


class CheckMedicines(QObject):

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('main.ui')
        self.conn = self.connectdb()
        self.offset = 0
        self.ui.buttoncheck.clicked.connect(self.checkMedicines)
        self.ui.buttonchange.clicked.connect(self.changeMedicines)
        self.ui.button_next.clicked.connect(self.nextpage)
        self.ui.button_pre.clicked.connect(self.prepage)
        self.ui.tablemedicines.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def connectdb(self):
        conn = MySQLdb.connect(
            host='127.0.0.1',
            user='root',
            passwd='root',
            db='prac',
            charset="utf8"
        )
        return conn

    def prepage(self):
        if self.offset - 20 < 0:
            QMessageBox.about(self.ui, "提示", "已经首页了！")
        else:
            self.offset -= 20
            self.checkMedicines()

    def nextpage(self):
        if self.ui.tablemedicines.rowCount() < 20:
            QMessageBox.about(self.ui, "提示", "已经尾页了！")
        else:
            self.offset += 20
            self.checkMedicines()

    def checkMedicines(self):
        c = self.conn.cursor()
        c.execute(f"SELECT * FROM medicines limit 20 offset {self.offset}")
        rows = c.fetchall()
        self.conn.commit()
        self.ui.tablemedicines.setRowCount(len(rows))
        for rowNumber in range(len(rows)):
            for colNumber in range(4):
                self.ui.tablemedicines.setItem(rowNumber, colNumber, QTableWidgetItem(str(rows[rowNumber][colNumber])))
                if colNumber == 0:
                    self.ui.tablemedicines.item(rowNumber, colNumber).setFlags(QtCore.Qt.ItemIsEditable)
        self.ui.text.append("成功查询")

    def changeMedicines(self):

        rowN = self.ui.tablemedicines.rowCount()
        colN = self.ui.tablemedicines.columnCount()
        medicines = []
        for rowNumber in range(rowN):
            medicine = []
            for colNumber in range(colN):
                item = self.ui.tablemedicines.item(rowNumber, colNumber).text()
                if colNumber == 0:
                    item = int(item)
                medicine.append(item)
            medicines.append(medicine)

        c = self.conn.cursor()
        for medicine in medicines:
            c.execute(f"""update medicines set `name`=%s,`index`=%s,`desc`=%s where `id`=%s""",
                      (medicine[1], medicine[2], medicine[3], medicine[0]))
        self.conn.commit()
        self.ui.text.append("成功更新")


app = QApplication()
checkMedicines = CheckMedicines()
checkMedicines.ui.show()
app.exec()
