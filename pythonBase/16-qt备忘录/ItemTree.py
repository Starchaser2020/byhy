#******************************************************************************
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA. 
#******************************************************************************

import os,random,string

from PySide2.QtGui import QIcon, QFont, QTextDocument,QColor
from PySide2.QtWidgets import QTreeWidget, QAbstractItemView, QDialog,QInputDialog,QTreeWidgetItem,QMessageBox

from PySide2 import QtCore

#******************************************************************************

class ItemTree (QTreeWidget):
    """
     Container for TaskItem instances 
    :version:
    :author: pir
    """

    def __init__(self,parent):
        super().__init__()
        
        # Configure tree widget
        # self.setHeaderHidden(True)
        # self.setColumnCount(2)
        # self.setDragDropMode(QAbstractItemView.InternalMove)
        
        #self.setColumnWidth(1,100)
        # self.resizeColumnToContents(2)
        # how to set column widths to display string of arbitrary length????

        # self.itemClicked.connect(self.on_item_clicked)
        # self.itemDoubleClicked.connect(self.on_item_double_clicked)
       
        # Load tree icons from ./treeIcons directory
        self.treeIconsFilesList = os.listdir("./Images")
        self.treeIconsFilesList.sort()
        self.treeIconsDict = {}
        for i in range(0, len(self.treeIconsFilesList)):
            iconFile = self.treeIconsFilesList[i]
            iconName = iconFile.rsplit('.',1)[0]
            self.treeIconsDict[iconName] = (QIcon("./Images/" + iconFile ))

        # # Default parameters
        # self.defaultIconIndex = 0
        # self.defaultTreeFont = QFont("Helvetica", 11)
        # self.defaultTreeFontSize = 11
        
        return
        
    #--------------------------------------------------------------------------

    def insert_task_item(self, parentItem,title,deadline, folderOrNote,
                         id=None,index=None):
        """
        Insert a new task item into the task tree with the supplied properties:
        

        title: string of text used in tree
        deadline: int in ISO-8601 format of: YYYYMMDDHHMM

        @return: None
        @author: pir
        """     
      


        newTaskItem = QTreeWidgetItem()

        if id :
            newTaskItem.id = id
        else:
            # 产生8位随机字符作为ID，重复概率 1/36**8  接近于0
            newTaskItem.id = ''.join(random.choices(string.ascii_uppercase + string.digits, k=10))

        newTaskItem.setIcon(0, self.treeIconsDict[folderOrNote])
        newTaskItem.title = title
        newTaskItem.setText(0, title)
        if deadline:
            newTaskItem.deadline = deadline
            newTaskItem.setText(1, deadline)
        newTaskItem.nodetype = folderOrNote
        newTaskItem.setExpanded(True)
        newTaskItem.note = QTextDocument()
        if index is None:
            parentItem.addChild( newTaskItem)
        else:
            parentItem.insertChild( index, newTaskItem)

        parentItem.setExpanded(True)

        newTaskItem.setFlags(newTaskItem.flags() | QtCore.Qt.ItemIsEditable)
        return newTaskItem
    
    #--------------------------------------------------------------------------

    def delete_task_item(self):
        """
        Delete the currently-selected task item from the task tree
        @return: None
        @author: 
        """

        targetItem = self.currentItem()

        # 没有当前选中节点
        if not targetItem:
            return
        
        return

    #--------------------------------------------------------------------------


    #--------------------------------------------------------------------------

    def edit_task_item(self):
        """
        Edit the current selected task item
        @return:
        @author:
        """

        return

    #--------------------------------------------------------------------------
    
    def show_schedule(self):
        """
        Show the schedules for all items with assigned deadlines; ignore tasks without deadlines
        @return:
        @author:
        """

        # get all notes with deadlines, put into a list
        notesList = []

        # go through the tree, collect  notes with deadlines
        def iterateFunc(parent):
            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)

                if item.nodetype == 'note' and item.deadline != 'none':

                    notesList.append(item)

                # 如果节点类型是目录，递归调用
                if item.nodetype == 'folder':
                    iterateFunc(item)

        root = self.invisibleRootItem()
        iterateFunc(root)

        # 排序显示
        def bubbleSort(arr):
            length = len(arr)

            for j in range(length - 1, 0, -1):
                for i in range(0, length - 1):
                    if arr[i].deadline > arr[i + 1].deadline:
                        arr[i], arr[i + 1] = arr[i + 1], arr[i]

            return arr

        bubbleSort(notesList)
        infoList = [f'   {item.deadline} {item.title}           ' for item in notesList]

        QMessageBox.information(
            self,
            '任务按照时间排序',
            '\n'.join(infoList))

        return
    
    #--------------------------------------------------------------------------
        
    def search_tree(self,keywords):
        """  
        Search tree for specified text in title
        @return:
        @author:
        """


        # recursive function 递归调用函数，完成整个树的搜索过滤
        def searchFunc(parent):
            child_count = parent.childCount()
            for i in range(child_count):
                item = parent.child(i)
                if keywords in item.text(0):
                    item.setBackgroundColor(0, QColor('#c9e9e3'))
                else:
                    item.setBackgroundColor(0, QColor('white'))

                if item.nodetype == 'folder':
                    searchFunc(item)

        if keywords == '':
            keywords = '$%#$%@#$@#$@#$!!!$' # 搞一个不可能存在的字符串，让不匹配
        root = self.invisibleRootItem()
        searchFunc(root)


        return
    
    #--------------------------------------------------------------------------

    def search_notes(self):
        """
        Search notes for specified text
        @return:
        @author:
        """

        return

    #--------------------------------------------------------------------------

        
    #--------------------------------------------------------------------------

    def on_item_clicked(self, currentItem, column):
        """
        Update text editor with note (QTextDocument) of current item
        @return: None
        @author: pir
        """
        #print(currentItem.text(0), "task clicked") #test
        # self.editBox.setDocument(currentItem.note)

        return

    #--------------------------------------------------------------------------

    def on_item_double_clicked(self, currentItem, column):
        """
        Edit properties of current item 
        @return:
        @author:
        """

        print(currentItem.text(0), "task double-clicked")   # test

        return
    
#******************************************************************************
