# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from ItemTree import ItemTree


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(942, 736)
        MainWindow.setStyleSheet(u"*{	\n"
"	font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"	font-size:14px;\n"
"	color: #1d649c;\n"
"}\n"
"\n"
"QGroupBox{\n"
"   font-family:\u5fae\u8f6f\u96c5\u9ed1;\n"
"   font-size:15px;\n"
"   color: rgb(126, 0, 0);\n"
"}")
        self.actionAddSubFolder = QAction(MainWindow)
        self.actionAddSubFolder.setObjectName(u"actionAddSubFolder")
        icon = QIcon()
        icon.addFile(u"Images/subfolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddSubFolder.setIcon(icon)
        self.actionAddNote = QAction(MainWindow)
        self.actionAddNote.setObjectName(u"actionAddNote")
        icon1 = QIcon()
        icon1.addFile(u"Images/note.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddNote.setIcon(icon1)
        self.actionAddSibleFolder = QAction(MainWindow)
        self.actionAddSibleFolder.setObjectName(u"actionAddSibleFolder")
        icon2 = QIcon()
        icon2.addFile(u"Images/siblefolder.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionAddSibleFolder.setIcon(icon2)
        self.actionSave = QAction(MainWindow)
        self.actionSave.setObjectName(u"actionSave")
        icon3 = QIcon()
        icon3.addFile(u"Images/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionSave.setIcon(icon3)
        self.actionDelete = QAction(MainWindow)
        self.actionDelete.setObjectName(u"actionDelete")
        icon4 = QIcon()
        icon4.addFile(u"Images/delete.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionDelete.setIcon(icon4)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.keywords = QLineEdit(self.centralwidget)
        self.keywords.setObjectName(u"keywords")

        self.horizontalLayout_3.addWidget(self.keywords)

        self.showSchedule = QPushButton(self.centralwidget)
        self.showSchedule.setObjectName(u"showSchedule")

        self.horizontalLayout_3.addWidget(self.showSchedule)

        self.searchInTree = QPushButton(self.centralwidget)
        self.searchInTree.setObjectName(u"searchInTree")

        self.horizontalLayout_3.addWidget(self.searchInTree)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.notesTree = ItemTree(self.centralwidget)
        __qtreewidgetitem = QTreeWidgetItem()
        __qtreewidgetitem.setText(1, u"\u63d0\u4ea4\u65e5\u671f");
        __qtreewidgetitem.setText(0, u"\u4f5c\u4e1a");
        self.notesTree.setHeaderItem(__qtreewidgetitem)
        self.notesTree.setObjectName(u"notesTree")
        self.notesTree.setWordWrap(True)
        self.notesTree.setHeaderHidden(False)
        self.notesTree.setColumnCount(2)
        self.notesTree.header().setVisible(True)
        self.notesTree.header().setDefaultSectionSize(150)

        self.verticalLayout_2.addWidget(self.notesTree)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.keywords_2 = QLineEdit(self.centralwidget)
        self.keywords_2.setObjectName(u"keywords_2")

        self.horizontalLayout_2.addWidget(self.keywords_2)

        self.searchInTextEditor = QPushButton(self.centralwidget)
        self.searchInTextEditor.setObjectName(u"searchInTextEditor")

        self.horizontalLayout_2.addWidget(self.searchInTextEditor)


        self.verticalLayout_3.addLayout(self.horizontalLayout_2)

        self.textEdit = QTextEdit(self.centralwidget)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)

        self.verticalLayout_3.addWidget(self.textEdit)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 2)

        self.verticalLayout.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 942, 26))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(MainWindow)
        self.toolBar.setObjectName(u"toolBar")
        MainWindow.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menu_2.addAction(self.actionAddSubFolder)
        self.toolBar.addSeparator()
        self.toolBar.addAction(self.actionAddSubFolder)
        self.toolBar.addAction(self.actionAddSibleFolder)
        self.toolBar.addAction(self.actionAddNote)
        self.toolBar.addAction(self.actionDelete)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"\u5907\u5fd8\u5f55", None))
        self.actionAddSubFolder.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5b50\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.actionAddSubFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5b50\u76ee\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.actionAddNote.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7b14\u8bb0", None))
#if QT_CONFIG(tooltip)
        self.actionAddNote.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u7b14\u8bb0", None))
#endif // QT_CONFIG(tooltip)
        self.actionAddSibleFolder.setText(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5144\u5f1f\u76ee\u5f55", None))
#if QT_CONFIG(tooltip)
        self.actionAddSibleFolder.setToolTip(QCoreApplication.translate("MainWindow", u"\u6dfb\u52a0\u5144\u5f1f\u76ee\u5f55", None))
#endif // QT_CONFIG(tooltip)
        self.actionSave.setText(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58", None))
#if QT_CONFIG(tooltip)
        self.actionSave.setToolTip(QCoreApplication.translate("MainWindow", u"\u4fdd\u5b58\u76ee\u5f55\u6811", None))
#endif // QT_CONFIG(tooltip)
        self.actionDelete.setText(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
#if QT_CONFIG(tooltip)
        self.actionDelete.setToolTip(QCoreApplication.translate("MainWindow", u"\u5220\u9664", None))
#endif // QT_CONFIG(tooltip)
        self.keywords.setText("")
        self.keywords.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u67e5\u8be2\u5173\u952e\u5b57", None))
        self.showSchedule.setText(QCoreApplication.translate("MainWindow", u"\u8ba1\u5212\u6392\u5e8f", None))
        self.searchInTree.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u6ee4", None))
        self.keywords_2.setText("")
        self.keywords_2.setPlaceholderText(QCoreApplication.translate("MainWindow", u"\u8bf7\u8f93\u5165\u67e5\u8be2\u5173\u952e\u5b57", None))
        self.searchInTextEditor.setText(QCoreApplication.translate("MainWindow", u"\u8fc7\u6ee4", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("MainWindow", u"\u64cd\u4f5c", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("MainWindow", u"toolBar", None))
    # retranslateUi

