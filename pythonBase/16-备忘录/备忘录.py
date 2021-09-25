import json

from PySide6.QtWidgets import *
from PySide6.QtUiTools import QUiLoader
from PySide6.QtGui import QIcon, QFont, QColor
from PySide6.QtCore import Signal, QObject
from PySide6 import QtCore, QtGui
from threading import Thread
import traceback
from PySide6.QtWidgets import QTreeWidgetItem
import re

class Mysiganl(QObject):
    saveDir = Signal()
    doubleClicked = Signal(QPlainTextEdit,QTreeWidgetItem)
global_ms = Mysiganl()



class Note(QObject):

    def __init__(self):
        super().__init__()
        self.ui = QUiLoader().load('main.ui')
        self.loadDir()
        self.ui.actionAddDir.triggered.connect(self.actionAddDir)
        self.ui.actionAddPeerDir.triggered.connect(self.actionAddPeerDir)
        self.ui.actionAddNote.triggered.connect(self.actionAddNote)
        self.ui.actionDel.triggered.connect(self.delNode)
        self.ui.tree.itemDoubleClicked.connect(self.itemDoubleClicked)
        self.ui.plainTextEdit.textChanged.connect(self.saveNote)
        self.ui.buttonText.clicked.connect(self.queryText)
        self.ui.buttonOrder.clicked.connect(self.order)
        self.ui.button2.clicked.connect(self.search_tree)
        global_ms.saveDir.connect(self.saveDir)

    def loadDir(self):
        tree = self.ui.tree
        with open('data.json', 'r', encoding='utf8') as f:
            jsonStr = json.load(f)
        root = tree.invisibleRootItem()
        self.loadDirIterateFunc(root, jsonStr)

    def loadDirIterateFunc(self, parent, dataTree):
        child_count = len(dataTree)
        for i in range(child_count):
            folderItem = QTreeWidgetItem()

            print( re.match(r".+\|.+",dataTree[i]['data']))
            if re.match(r".+\|.+",dataTree[i]['data']) != None:
                folderIcon = QIcon('note.png')
                folderItem.setIcon(0, folderIcon)
                folderItem.setText(0, dataTree[i]['data'].split('|')[0])
                folderItem.setText(1, dataTree[i]['data'].split('|')[1])
            else:
                folderIcon = QIcon('dir.png')
                folderItem.setIcon(0, folderIcon)
                folderItem.setText(0, dataTree[i]['data'])

            parent.addChild(folderItem)
            child = parent.child(i)
            self.loadDirIterateFunc(child, dataTree[i]['children'])

    def saveDir(self):
        tree = self.ui.tree
        root = tree.invisibleRootItem()
        dataTree = []
        self.saveDirIterateFunc(root, dataTree)
        jsonStr = json.dumps(dataTree, ensure_ascii=False, indent=2)
        with open('data.json', 'w', encoding='utf8') as f:
            f.write(jsonStr)

    def saveDirIterateFunc(self, parent, dataTree):
        child_count = parent.childCount()
        for i in range(child_count):
            item = parent.child(i)
            # 保存这个节点item的信息到字典对象中
            subDictNode = {}
            dataTree.append(subDictNode)
            if item.text(1) == '':
                subDictNode['data'] = item.text(0)
            else:
                subDictNode['data'] = item.text(0) + '|' + item.text(1)
            subDictNode['children'] = []
            # 对该子节点递归调用遍历处理函数
            self.saveDirIterateFunc(item, subDictNode['children'])

    def actionAddDir(self):
        tree = self.ui.tree
        # 获取当前用户点选的节点
        currentItem = tree.currentItem()
        # 没有当前选中节点，不可见根节点作为当前节点
        if not currentItem:
            currentItem = tree.invisibleRootItem()

        # 让用户输入信息
        text, okPressed = QInputDialog.getText(
            self.ui, "输入目录名称",
            "名称:",
            QLineEdit.Normal,
            "")
        if not okPressed or text == '':
            return
        folderItem = QTreeWidgetItem()
        folderIcon = QIcon('dir.png')
        folderItem.setIcon(0, folderIcon)

        dirName = text
        folderItem.setText(0, dirName)
        currentItem.addChild(folderItem)
        folderItem.setExpanded(True)
        global_ms.saveDir.emit()

    def actionAddPeerDir(self):
        tree = self.ui.tree
        # 获取当前用户点选的节点
        ParentItem = tree.currentItem().parent()
        # 没有当前选中节点，不可见根节点作为当前节点
        if not ParentItem:
            ParentItem = tree.invisibleRootItem()

        # 让用户输入信息
        text, okPressed = QInputDialog.getText(
            self.ui, "输入目录名称",
            "名称:",
            QLineEdit.Normal,
            "")
        if not okPressed or text == '':
            return
        folderItem = QTreeWidgetItem()
        folderIcon = QIcon('dir.png')
        folderItem.setIcon(0, folderIcon)

        dirName = text
        folderItem.setText(0, dirName)
        ParentItem.addChild(folderItem)
        folderItem.setExpanded(True)
        global_ms.saveDir.emit()

    def actionAddNote(self):
        tree = self.ui.tree
        # 获取当前用户点选的节点
        currentItem = tree.currentItem()
        # 没有当前选中节点，不可见根节点作为当前节点
        if not currentItem:
            currentItem = tree.invisibleRootItem()
        # 让用户输入信息
        text, okPressed = QInputDialog.getText(
            self.ui, "输入笔记名称",
            "名称|日期",
            QLineEdit.Normal,
            "")
        if not okPressed or text == '':
            return
        noteItem = QTreeWidgetItem()
        noteIcon = QIcon('note.png')
        noteItem.setIcon(0, noteIcon)
        try:
            noteName = text
            noteItem.setText(0, noteName.split('|')[0])
            noteItem.setText(1, noteName.split('|')[1])
            currentItem.addChild(noteItem)
            currentItem.setExpanded(True)
        except:
            QMessageBox.about(self.ui, '错误', '输入有误，例子：“笔记|20200101”')
            traceback.print_exc()
        global_ms.saveDir.emit()

    def delNode(self):
        # 获取当前用户点选的节点
        tree = self.ui.tree
        currentItem = tree.currentItem()

        # 如果没有当前选中节点
        if not currentItem:
            return

        # 找到改节点的父节点
        parentItem = currentItem.parent()
        # 如果没有父节点，就是不可见父节点
        if not parentItem:
            parentItem = tree.invisibleRootItem()
        # 删除该节点
        parentItem.removeChild(currentItem)
        with open('note.json','r',encoding='utf8') as f:
            note = json.load(f)
            if not currentItem and currentItem.text(0) in note[0]:
                del note[0][self.ui.tree.currentItem().text(0)]
        jsonStr = json.dumps(note, ensure_ascii=False, indent=2)
        with open('note.json', 'w', encoding='utf8') as f:
            f.write(jsonStr)
        global_ms.saveDir.emit()

    def itemDoubleClicked(self, item):
        with open('note.json', 'r', encoding='utf8') as f:
            note = json.load(f)
        if item.text(0) in note[0] and item.text(1) != ' ':
            self.ui.plainTextEdit.setPlainText(note[0][item.text(0)])
        else:
            self.ui.plainTextEdit.setPlainText('')

    def saveNote(self):
        with open('note.json','r',encoding='utf8') as f:
            note = json.load(f)
            if self.ui.tree.currentItem().text(1).strip() != '':
                note[0][self.ui.tree.currentItem().text(0)] = self.ui.plainTextEdit.toPlainText()
        jsonStr = json.dumps(note, ensure_ascii=False, indent=2)
        with open('note.json', 'w', encoding='utf8') as f:
            f.write(jsonStr)

    def queryText(self):

        te = self.ui.plainTextEdit

        cursor = te.textCursor()

        # 清空格式
        cursor.select(QtGui.QTextCursor.Document)
        cursor.setCharFormat(QtGui.QTextCharFormat())
        cursor.clearSelection()
        te.setTextCursor(cursor)


        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("#6ac06e")))

        searchString = self.ui.lineText.text()
        # 空字符串，清空选择
        if searchString == '':
            # 清空格式
            cursor.select(QtGui.QTextCursor.Document)
            cursor.setCharFormat(QtGui.QTextCharFormat())
            cursor.clearSelection()
            te.setTextCursor(cursor)
            return

        # Process the displayed document
        pos = 0

        lenOfs = len(searchString)
        while True:
            index = te.toPlainText().find(searchString,pos)
            if index < 0:
                break

            cursor.setPosition(index)

            cursor.movePosition(
                QtGui.QTextCursor.Right,
                QtGui.QTextCursor.MoveMode.KeepAnchor,
                lenOfs)
            cursor.mergeCharFormat(format)

            pos = index + lenOfs

    def order(self):
        noteList = {}
        def findNote(parent):
            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)
                if item.text(1) != '':
                    noteList[item.text(0)] = item.text(1)
                findNote(item)
        parent = self.ui.tree.invisibleRootItem()
        findNote(parent)

        d_order=sorted(noteList.items(),key=lambda x:x[1],reverse=False)
        order = ''
        for k,v in d_order:
            order += k +':'+ v + '\n'
        QMessageBox.about(self.ui,'计划顺序',order)

    def search_tree(self):
        keywords = self.ui.lineText2.text()
        def searchFunc(parent):
            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)
                if keywords in item.text(0):
                    item.setBackground(0, QColor('#c9e9e3'))
                else:
                    item.setBackground(0, QColor('white'))

        if keywords == '':
            keywords = '$%#$%@#$@#$@#$!!!$' # 搞一个不可能存在的字符串，让不匹配
        root = self.ui.tree.invisibleRootItem()
        searchFunc(root)


        return




app = QApplication()
note = Note()
note.ui.show()

app.exec()
