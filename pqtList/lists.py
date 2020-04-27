# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'lists.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(414, 364)
        Form.setFocusPolicy(QtCore.Qt.TabFocus)
        Form.setStyleSheet("")
        self.pushButton = QtWidgets.QPushButton(Form)
        self.pushButton.setGeometry(QtCore.QRect(20, 40, 45, 35))
        self.pushButton.setAutoFillBackground(False)
        self.pushButton.setStyleSheet("QPushButton{\n"
"border:none;\n"
"background-color:rgb(67, 255, 57);\n"
"color:blue;\n"
"\n"
"\n"
"}\n"
"\n"
"QPushButton:hover{\n"
"background-color:silver;\n"
"}")
        self.pushButton.setObjectName("pushButton")
        self.listView = QtWidgets.QListView(Form)
        self.listView.setGeometry(QtCore.QRect(0, 90, 411, 271))
        self.listView.setObjectName("listView")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Записка"))
        self.pushButton.setText(_translate("Form", "+"))

