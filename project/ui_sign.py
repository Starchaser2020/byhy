# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui_sign.ui'
##
## Created by: Qt User Interface Compiler version 6.1.3
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *  # type: ignore
from PySide6.QtGui import *  # type: ignore
from PySide6.QtWidgets import *  # type: ignore


class Ui_sign(object):
    def setupUi(self, sign):
        if not sign.objectName():
            sign.setObjectName(u"sign")
        sign.resize(391, 279)
        sizePolicy = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(sign.sizePolicy().hasHeightForWidth())
        sign.setSizePolicy(sizePolicy)
        sign.setMinimumSize(QSize(391, 279))
        sign.setMaximumSize(QSize(391, 279))
        self.label_2 = QLabel(sign)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 40, 51, 51))
        self.label_2.setPixmap(QPixmap(u"image/icons8-tweakbox-50.png"))
        self.lineEdit = QLineEdit(sign)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(130, 120, 133, 21))
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setEchoMode(QLineEdit.Normal)
        self.lineEdit_2 = QLineEdit(sign)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(130, 160, 133, 21))
        sizePolicy.setHeightForWidth(self.lineEdit_2.sizePolicy().hasHeightForWidth())
        self.lineEdit_2.setSizePolicy(sizePolicy)
        self.lineEdit_2.setEchoMode(QLineEdit.Password)
        self.lineEdit_2.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.buttonSign = QPushButton(sign)
        self.buttonSign.setObjectName(u"buttonSign")
        self.buttonSign.setGeometry(QRect(160, 210, 75, 24))
        sizePolicy.setHeightForWidth(self.buttonSign.sizePolicy().hasHeightForWidth())
        self.buttonSign.setSizePolicy(sizePolicy)
        self.label = QLabel(sign)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(100, 50, 270, 35))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        font = QFont()
        font.setPointSize(20)
        self.label.setFont(font)

        self.retranslateUi(sign)

        QMetaObject.connectSlotsByName(sign)
    # setupUi

    def retranslateUi(self, sign):
        sign.setWindowTitle(QCoreApplication.translate("sign", u"\u767b\u5f55", None))
        self.label_2.setText("")
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("sign", u"\u7528\u6237\u540d", None))
        self.lineEdit_2.setPlaceholderText(QCoreApplication.translate("sign", u"\u5bc6\u7801", None))
        self.buttonSign.setText(QCoreApplication.translate("sign", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("sign", u"\u9ed1\u7fbd\u5b66\u9662\u6570\u636e\u5904\u7406\u5de5\u5177", None))
    # retranslateUi

