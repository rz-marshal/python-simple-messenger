# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'messenger.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Messenger(object):
    def setupUi(self, Messenger):
        Messenger.setObjectName("Messenger")
        Messenger.resize(438, 534)
        self.centralwidget = QtWidgets.QWidget(Messenger)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(120, 10, 211, 41))
        font = QtGui.QFont()
        font.setPointSize(24)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(20, 110, 401, 331))
        self.textBrowser.setObjectName("textBrowser")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(20, 460, 321, 31))
        self.textEdit.setObjectName("textEdit")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(350, 460, 71, 32))
        self.pushButton.setObjectName("pushButton")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(100, 70, 101, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(30, 70, 60, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(230, 70, 60, 16))
        self.label_3.setObjectName("label_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(300, 70, 101, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        Messenger.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Messenger)
        self.statusbar.setObjectName("statusbar")
        Messenger.setStatusBar(self.statusbar)

        self.retranslateUi(Messenger)
        QtCore.QMetaObject.connectSlotsByName(Messenger)

    def retranslateUi(self, Messenger):
        _translate = QtCore.QCoreApplication.translate
        Messenger.setWindowTitle(_translate("Messenger", "Messenger"))
        self.label.setText(_translate("Messenger", "Simple Messenger"))
        self.pushButton.setText(_translate("Messenger", "Send"))
        self.label_2.setText(_translate("Messenger", "username"))
        self.label_3.setText(_translate("Messenger", "password"))
