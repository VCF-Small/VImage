# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'c:\Users\Himanshu\Desktop\Files\Projects\VImage\VImage-2\src\Designs\Resize_Window.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Resize(object):
    def __init__(self):
        pass
        
    def setupUi(self, Resize):
        Resize.setObjectName("Resize")
        Resize.resize(357, 156)
        Resize.setMinimumSize(QtCore.QSize(357, 156))
        Resize.setMaximumSize(QtCore.QSize(357, 156))
        self.pushButton = QtWidgets.QPushButton(Resize)
        self.pushButton.setGeometry(QtCore.QRect(80, 90, 101, 41))
        self.pushButton.setStyleSheet("font:12pt;")
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Resize)
        self.pushButton_2.setGeometry(QtCore.QRect(190, 90, 101, 41))
        self.pushButton_2.setStyleSheet("font:12pt;")
        self.pushButton_2.setObjectName("pushButton_2")
        self.label = QtWidgets.QLabel(Resize)
        self.label.setGeometry(QtCore.QRect(25, 25, 400, 21))
        self.label.setStyleSheet("font:9pt;")
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(Resize)
        self.lineEdit.setGeometry(QtCore.QRect(100, 50, 141, 31))
        self.lineEdit.setStyleSheet("font:16pt;")
        self.lineEdit.setText("")
        self.lineEdit.setObjectName("lineEdit")
        self.label_2 = QtWidgets.QLabel(Resize)
        self.label_2.setGeometry(QtCore.QRect(250, 50, 51, 31))
        self.label_2.setStyleSheet("font: 12pt;\n"
"")
        self.label_2.setObjectName("label_2")

        self.retranslateUi(Resize)
        QtCore.QMetaObject.connectSlotsByName(Resize)

    def retranslateUi(self, Resize):
        _translate = QtCore.QCoreApplication.translate
        Resize.setWindowTitle(_translate("Resize", "Resize"))
        self.pushButton.setText(_translate("Resize", "Resize"))
        self.pushButton_2.setText(_translate("Resize", "Cancel"))
        self.label.setText(_translate("Resize", "Cange size to x% of the original image"))
        self.label_2.setText(_translate("Resize", "%"))