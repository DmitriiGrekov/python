# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'formAded.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Aded(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(558, 284)
        self.titleLine = QtWidgets.QLineEdit(Form)
        self.titleLine.setGeometry(QtCore.QRect(20, 20, 521, 28))
        self.titleLine.setObjectName("titleLine")
        self.textLine = QtWidgets.QPlainTextEdit(Form)
        self.textLine.setGeometry(QtCore.QRect(20, 60, 521, 141))
        self.textLine.setObjectName("textLine")
        self.dateLine = QtWidgets.QDateTimeEdit(Form)
        self.dateLine.setGeometry(QtCore.QRect(20, 230, 194, 26))
        self.dateLine.setObjectName("dateLine")
        self.buttonAded = QtWidgets.QPushButton(Form)
        self.buttonAded.setGeometry(QtCore.QRect(240, 230, 301, 28))
        self.buttonAded.setStyleSheet("border:none;\n"
"background-color:green;\n"
"color:white")
        self.buttonAded.setObjectName("buttonAded")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление записи"))
        self.buttonAded.setText(_translate("Form", "Добавить"))

