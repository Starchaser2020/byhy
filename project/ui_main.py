# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_main.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_main(object):
    def setupUi(self, main):
        if not main.objectName():
            main.setObjectName(u"main")
        main.resize(813, 573)
        self.actionExit = QAction(main)
        self.actionExit.setObjectName(u"actionExit")
        icon = QIcon()
        icon.addFile(u"image/icons8-exit-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionExit.setIcon(icon)
        self.actionVersion = QAction(main)
        self.actionVersion.setObjectName(u"actionVersion")
        self.actionStressTest = QAction(main)
        self.actionStressTest.setObjectName(u"actionStressTest")
        icon1 = QIcon()
        icon1.addFile(u"image/icons8-test-tube-32.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionStressTest.setIcon(icon1)
        self.actionCfg = QAction(main)
        self.actionCfg.setObjectName(u"actionCfg")
        icon2 = QIcon()
        icon2.addFile(u"image/icons8-data-setting-30.png", QSize(), QIcon.Normal, QIcon.Off)
        self.actionCfg.setIcon(icon2)
        self.centralwidget = QWidget(main)
        self.centralwidget.setObjectName(u"centralwidget")
        self.treeWidget = QTreeWidget(self.centralwidget)
        self.treeWidget.setObjectName(u"treeWidget")
        self.treeWidget.setGeometry(QRect(10, 10, 201, 477))
        self.mdiArea = QMdiArea(self.centralwidget)
        self.mdiArea.setObjectName(u"mdiArea")
        self.mdiArea.setEnabled(True)
        self.mdiArea.setGeometry(QRect(217, 10, 586, 477))
        self.subwindow = QWidget()
        self.subwindow.setObjectName(u"subwindow")
        self.verticalLayout_2 = QVBoxLayout(self.subwindow)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.buttonTestLink = QPushButton(self.subwindow)
        self.buttonTestLink.setObjectName(u"buttonTestLink")

        self.horizontalLayout.addWidget(self.buttonTestLink)

        self.buttonTestDB = QPushButton(self.subwindow)
        self.buttonTestDB.setObjectName(u"buttonTestDB")

        self.horizontalLayout.addWidget(self.buttonTestDB)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.tableConfig = QTableWidget(self.subwindow)
        if (self.tableConfig.columnCount() < 2):
            self.tableConfig.setColumnCount(2)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableConfig.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableConfig.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        if (self.tableConfig.rowCount() < 6):
            self.tableConfig.setRowCount(6)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableConfig.setVerticalHeaderItem(0, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableConfig.setVerticalHeaderItem(1, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableConfig.setVerticalHeaderItem(2, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableConfig.setVerticalHeaderItem(3, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableConfig.setVerticalHeaderItem(4, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableConfig.setVerticalHeaderItem(5, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableConfig.setItem(0, 0, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableConfig.setItem(1, 0, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableConfig.setItem(2, 0, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableConfig.setItem(3, 0, __qtablewidgetitem11)
        __qtablewidgetitem12 = QTableWidgetItem()
        self.tableConfig.setItem(4, 0, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        self.tableConfig.setItem(5, 0, __qtablewidgetitem13)
        self.tableConfig.setObjectName(u"tableConfig")

        self.verticalLayout.addWidget(self.tableConfig)

        self.plainTextEdit = QPlainTextEdit(self.subwindow)
        self.plainTextEdit.setObjectName(u"plainTextEdit")

        self.verticalLayout.addWidget(self.plainTextEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        self.mdiArea.addSubWindow(self.subwindow)
        main.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(main)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 813, 22))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        self.menu_2 = QMenu(self.menubar)
        self.menu_2.setObjectName(u"menu_2")
        self.menu_3 = QMenu(self.menubar)
        self.menu_3.setObjectName(u"menu_3")
        self.menu_4 = QMenu(self.menubar)
        self.menu_4.setObjectName(u"menu_4")
        self.menu_5 = QMenu(self.menubar)
        self.menu_5.setObjectName(u"menu_5")
        self.menu_6 = QMenu(self.menubar)
        self.menu_6.setObjectName(u"menu_6")
        self.menu_7 = QMenu(self.menubar)
        self.menu_7.setObjectName(u"menu_7")
        self.menu_8 = QMenu(self.menubar)
        self.menu_8.setObjectName(u"menu_8")
        main.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(main)
        self.statusbar.setObjectName(u"statusbar")
        main.setStatusBar(self.statusbar)
        self.toolBar = QToolBar(main)
        self.toolBar.setObjectName(u"toolBar")
        main.addToolBar(Qt.TopToolBarArea, self.toolBar)

        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        self.menubar.addAction(self.menu_4.menuAction())
        self.menubar.addAction(self.menu_5.menuAction())
        self.menubar.addAction(self.menu_6.menuAction())
        self.menubar.addAction(self.menu_7.menuAction())
        self.menubar.addAction(self.menu_8.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menu_2.addAction(self.actionStressTest)
        self.menu_3.addAction(self.actionVersion)
        self.menu_3.addAction(self.actionExit)
        self.menu_6.addAction(self.actionCfg)
        self.toolBar.addAction(self.actionExit)
        self.toolBar.addAction(self.actionStressTest)
        self.toolBar.addAction(self.actionCfg)

        self.retranslateUi(main)

        QMetaObject.connectSlotsByName(main)
    # setupUi

    def retranslateUi(self, main):
        main.setWindowTitle(QCoreApplication.translate("main", u"\u9ed1\u7fbd\u6570\u636e\u7ba1\u7406", None))
        self.actionExit.setText(QCoreApplication.translate("main", u"\u9000\u51fa", None))
        self.actionVersion.setText(QCoreApplication.translate("main", u"\u7248\u672c\u53f7", None))
#if QT_CONFIG(tooltip)
        self.actionVersion.setToolTip(QCoreApplication.translate("main", u"\u7248\u672c\u53f7", None))
#endif // QT_CONFIG(tooltip)
        self.actionStressTest.setText(QCoreApplication.translate("main", u"\u538b\u529b\u6d4b\u8bd5", None))
#if QT_CONFIG(tooltip)
        self.actionStressTest.setToolTip(QCoreApplication.translate("main", u"\u538b\u529b\u6d4b\u8bd5", None))
#endif // QT_CONFIG(tooltip)
        self.actionCfg.setText(QCoreApplication.translate("main", u"\u914d\u7f6e", None))
#if QT_CONFIG(tooltip)
        self.actionCfg.setToolTip(QCoreApplication.translate("main", u"\u914d\u7f6e", None))
#endif // QT_CONFIG(tooltip)
        ___qtreewidgetitem = self.treeWidget.headerItem()
        ___qtreewidgetitem.setText(0, QCoreApplication.translate("main", u"1", None));
        self.subwindow.setWindowTitle(QCoreApplication.translate("main", u"\u5b50\u7a97\u53e3", None))
        self.buttonTestLink.setText(QCoreApplication.translate("main", u"\u6d4b\u8bd5\u8fde\u63a5", None))
        self.buttonTestDB.setText(QCoreApplication.translate("main", u"\u6d4b\u8bd5\u6570\u636e\u5e93", None))
        ___qtablewidgetitem = self.tableConfig.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("main", u"\u53c2\u6570\u540d", None));
        ___qtablewidgetitem1 = self.tableConfig.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("main", u"\u53c2\u6570\u503c", None));
        ___qtablewidgetitem2 = self.tableConfig.verticalHeaderItem(0)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("main", u"1", None));
        ___qtablewidgetitem3 = self.tableConfig.verticalHeaderItem(1)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("main", u"2", None));
        ___qtablewidgetitem4 = self.tableConfig.verticalHeaderItem(2)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("main", u"3", None));
        ___qtablewidgetitem5 = self.tableConfig.verticalHeaderItem(3)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("main", u"4", None));
        ___qtablewidgetitem6 = self.tableConfig.verticalHeaderItem(4)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("main", u"5", None));
        ___qtablewidgetitem7 = self.tableConfig.verticalHeaderItem(5)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("main", u"6", None));

        __sortingEnabled = self.tableConfig.isSortingEnabled()
        self.tableConfig.setSortingEnabled(False)
        ___qtablewidgetitem8 = self.tableConfig.item(0, 0)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("main", u"web\u670d\u52a1\u5730\u5740", None));
        ___qtablewidgetitem9 = self.tableConfig.item(1, 0)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("main", u"web\u670d\u52a1\u7aef\u53e3", None));
        ___qtablewidgetitem10 = self.tableConfig.item(2, 0)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("main", u"\u6570\u636e\u5e93\u670d\u52a1\u5730\u5740", None));
        ___qtablewidgetitem11 = self.tableConfig.item(3, 0)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("main", u"\u6570\u636e\u5e93\u670d\u52a1\u7aef\u53e3", None));
        ___qtablewidgetitem12 = self.tableConfig.item(4, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("main", u"\u6570\u636e\u5e93\u8fde\u63a5\u8d26\u53f7", None));
        ___qtablewidgetitem13 = self.tableConfig.item(5, 0)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("main", u"\u6570\u636e\u5e93\u8fde\u63a5\u5bc6\u7801", None));
        self.tableConfig.setSortingEnabled(__sortingEnabled)

        self.menu.setTitle(QCoreApplication.translate("main", u"\u6587\u4ef6", None))
        self.menu_2.setTitle(QCoreApplication.translate("main", u"\u6d4b\u8bd5", None))
        self.menu_3.setTitle(QCoreApplication.translate("main", u"\u5173\u4e8e", None))
        self.menu_4.setTitle(QCoreApplication.translate("main", u"\u8fd0\u7ef4", None))
        self.menu_5.setTitle(QCoreApplication.translate("main", u"\u6570\u636e\u5206\u6790", None))
        self.menu_6.setTitle(QCoreApplication.translate("main", u"\u914d\u7f6e", None))
        self.menu_7.setTitle(QCoreApplication.translate("main", u"\u5bfc\u5165\u5bfc\u51fa", None))
        self.menu_8.setTitle(QCoreApplication.translate("main", u"\u4fe1\u606f\u63a8\u9001", None))
        self.toolBar.setWindowTitle(QCoreApplication.translate("main", u"toolBar", None))
    # retranslateUi

