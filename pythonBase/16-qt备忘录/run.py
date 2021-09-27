from PySide2.QtWidgets import QApplication, QMessageBox,QFileDialog,QInputDialog,QMainWindow,QAbstractItemView,QLineEdit

from PySide2 import QtGui,QtCore

from PySide2.QtUiTools import QUiLoader
from PySide2.QtCore import QDir,QSortFilterProxyModel

import traceback,os,time,json


from ui_main import Ui_MainWindow


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.ui =  Ui_MainWindow()

        # 初始化界面
        self.ui.setupUi(self)


        self.ui.searchInTree.clicked.connect(self.searchInTree)
        self.ui.showSchedule.clicked.connect(self.ui.notesTree.show_schedule)

        self.ui.actionAddSubFolder.triggered.connect(
            lambda: self.actionAddNode('sub','folder'))
        self.ui.actionAddSibleFolder.triggered.connect(
            lambda: self.actionAddNode('sible','folder'))
        self.ui.actionAddNote.triggered.connect(
            lambda: self.actionAddNode('sub','note'))
        self.ui.actionDelete.triggered.connect(self.actionDelete)

        self.ui.actionSave.triggered.connect(self.saveFile)

        self.ui.searchInTextEditor.clicked.connect(self.searchInTextEditor)


        self.loadTree()

        # 必须先加载树，然后再设置信号处理，
        # 否则加载过程也会触发 itemChanged 信号
        self.ui.notesTree.itemChanged.connect(self.itemChanged)

        self.ui.notesTree.itemClicked.connect(self.itemClicked)

        # self.ui.textEdit.textChanged.connect(self.textChange)

        # 记事帖 文件目录
        os.makedirs('notes', exist_ok=True)

        # 文本框对应的note节点
        self.currentNoteNode = None

    # 关闭窗口
    def closeEvent(self, event):
        # 保存当前内容
        self.saveFile()
        event.accept()

    # 保存文件
    def saveFile(self):

        if self.currentNoteNode is None:
            print('请选择当前备忘录')
            return

        # 先保存到节点textData属性
        self.currentNoteNode.textData = self.ui.textEdit.toPlainText()

        # 再保存到文件
        filename = os.path.join('notes', self.currentNoteNode.id)

        with open(filename,'w',encoding='utf8') as f:
            f.write(self.ui.textEdit.toPlainText())


    # # 编辑文本发生改变，存入节点 textData 中
    # def textChange(self):
    #     print('textChange')
    #     if self.currentNoteNode is None:
    #         print('请选择当前备忘录')
    #         return
    #
    #     self.currentNoteNode.textData = self.ui.textEdit.toPlainText()

    def itemClicked(self, item, column):

        # 保存原来节点的内容到内存 和 文件
        if self.currentNoteNode is not None:
            self.saveFile()


        # 不是备忘录节点
        if item.nodetype != 'note':
            return

        # 是备忘录节点
        self.ui.textEdit.setText('')

        self.currentNoteNode = item
        self.ui.textEdit.setEnabled(True)

        # 如果内存中有，载入
        if hasattr(item,'textData'):
            print('内存载入')
            self.ui.textEdit.setText(item.textData)
            return

        #  内存中没有，检查文件
        filename = os.path.join('notes',item.id)

        # 没有文件
        if not os.path.exists(filename):
            item.textData = ''
            return

        # 有文件
        with open(filename,encoding='utf8') as f:
            print('文件载入')
            content = f.read()
            item.textData = content
            self.ui.textEdit.setText(content)


    def itemChanged(self, item, column):
        newText = item.text(column)

        # 根据改变的 column 得知是哪个数据修改了
        # 保存到对应的数据
        if column == 0:
            item.title = newText
        elif column == 1:
            item.deadline = newText

        self.saveTree()

    def sort(self):

        root = self.ui.notesTree.invisibleRootItem()
        child_count = root.childCount()
        for i in range(child_count):
            item = root.child(i)
            print(item.deadline)


    def searchInTree(self):

        keywords = self.ui.keywords.text()
        self.ui.notesTree.search_tree(keywords)



    def searchInTextEditor(self):


        te = self.ui.textEdit

        cursor = te.textCursor()

        # 清空格式
        cursor.select(QtGui.QTextCursor.Document)
        cursor.setCharFormat(QtGui.QTextCharFormat())
        cursor.clearSelection()
        te.setTextCursor(cursor)


        # Setup the desired format for matches
        format = QtGui.QTextCharFormat()
        format.setBackground(QtGui.QBrush(QtGui.QColor("#6ac06e")))

        searchString = self.ui.keywords_2.text()
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




        # index = regex.indexIn(te.toPlainText(), pos)
        # while (index != -1):
        #     # Select the matched text and apply the desired format
        #     cursor.setPosition(index)
        #     cursor.movePosition(QtGui.QTextCursor.EndOfWord,QtGui.QTextCursor.MoveMode.MoveAnchor, 1)
        #     cursor.mergeCharFormat(format)
        #     # Move to the next match
        #     pos = index + regex.matchedLength()
        #     index = regex.indexIn(document, pos)

    def actionAddNode(self,sibleOrSub,folderOrNote):

        tree = self.ui.notesTree

        index = None # index 是插入的位置，None表示插入末尾

        currentItem = tree.currentItem()
        # 没有当前选中节点
        if not currentItem:
            parentItem = tree.invisibleRootItem()

        # 有当前选中节点
        else:
            # 要创建的是 子节点
            if (sibleOrSub == 'sub'):
                if currentItem.nodetype == 'folder':
                    parentItem = currentItem

                # 当前节点是笔记节点，只能添加兄弟节点
                else:
                    parentItem = currentItem.parent()
                    if not parentItem:
                        parentItem = tree.invisibleRootItem()

            # 要创建的是 兄弟节点
            else:
                parentItem = currentItem.parent()
                if not parentItem:
                    parentItem = tree.invisibleRootItem()

        # 让用户输入信息
        deadline = None
        # 添加的是目录
        if folderOrNote == 'folder':
            title, okPressed = QInputDialog.getText(self, "输入目录名称",
                                                "名称:",
                                                QLineEdit.Normal,
                                                "")
            if not okPressed or title == '':
                return

        # 添加的是笔记
        else:
            info, okPressed = QInputDialog.getText(self, "输入笔记信息",
                                                "笔记信息 (名称和截至日期，以竖线隔开)",
                                                QLineEdit.Normal,
                                                "")
            if not okPressed or info == '':
                return

            parts = info.split('|')
            title = parts[0]
            if len(parts) ==2 :
                deadline = parts[1]
            else:
                deadline = 'none'

            # 是笔记节点，要按照 deadline进行排序，指定插入位置

            child_count = parentItem.childCount()
            for i in range(child_count):
                item = parentItem.child(i)
                if item.nodetype == 'note':
                    if deadline <= item.deadline:
                        index = i
                        break


        tree.insert_task_item(parentItem, title, deadline ,folderOrNote,index)

        # 每次更新完树，都要存盘

        self.saveTree()


    def actionDelete(self):

        tree = self.ui.notesTree

        currentItem = tree.currentItem()

        # 没有当前选中节点
        if not currentItem:
            return

        parentItem = currentItem.parent()
        if not parentItem:
            parentItem = tree.invisibleRootItem()

        parentItem.removeChild(currentItem)

        # 每次更新完树，都要存盘
        self.saveTree()

    def saveTree(self):
        # 递归调用函数，完成整个树的遍历
        def iterateFunc(parent,dataTree):
            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)

                # 保存这个节点item的信息到字典对象中
                subDictNode = {}
                subDictNode['id'] = item.id
                subDictNode['nodetype'] = item.nodetype
                subDictNode['title'] = item.title
                if item.nodetype  == 'note':
                    subDictNode['deadline'] = item.deadline

                dataTree.append(subDictNode)

                # 如果节点类型是目录，递归调用
                if item.nodetype == 'folder':
                    subDictNode['children'] = []
                    iterateFunc(item,subDictNode['children'])


        root = self.ui.notesTree.invisibleRootItem()
        dataTree = [] # 用嵌套列表来对应树的数据结构，方便保存到文件
        iterateFunc(root,dataTree)
        # 序列化到json文件，保存
        jsonStr = json.dumps(dataTree,ensure_ascii=False,indent=2)
        with open('data.json','w',encoding='utf8') as f:
            f.write(jsonStr)

    def loadTree(self):
        if not os.path.exists('data.json'):
            return

        def loadOneNode(dadItem,dataTree):
            for node in dataTree:
                item = self.ui.notesTree.insert_task_item(
                    dadItem,
                    node['title'],
                    node.get('deadline',None),
                    node['nodetype'],
                    id = node['id'])

                # 如果有子节点，加载子节点
                if node.get('children',None):
                    loadOneNode(item, node['children'])



        # 从数据文件中读入保存的树结构，创建树控件节点
        with open('data.json',encoding='utf8') as f:
            jsonStr = f.read()

        dataTree = json.loads(jsonStr)
        root = self.ui.notesTree.invisibleRootItem()
        loadOneNode(root,dataTree)


app = QApplication([])
mainw = MainWindow()
mainw.show()
app.exec_()