# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'Calculator.ui'
#
# Created by: PyQt5 UI code generator 5.12.3
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_CalculatorMainWindow(object):
    def setupUi(self, CalculatorMainWindow):
        CalculatorMainWindow.setObjectName("CalculatorMainWindow")
        CalculatorMainWindow.resize(287, 392)
        self.centralwidget = QtWidgets.QWidget(CalculatorMainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_7 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_7.setGeometry(QtCore.QRect(0, 70, 71, 71))
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_8 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_8.setGeometry(QtCore.QRect(70, 70, 71, 71))
        self.pushButton_8.setObjectName("pushButton_8")
        self.pushButton_9 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_9.setGeometry(QtCore.QRect(140, 70, 71, 71))
        self.pushButton_9.setObjectName("pushButton_9")
        self.pushButton_c = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_c.setGeometry(QtCore.QRect(210, 70, 71, 71))
        self.pushButton_c.setObjectName("pushButton_c")
        self.pushButton_4 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_4.setGeometry(QtCore.QRect(0, 140, 71, 71))
        self.pushButton_4.setObjectName("pushButton_4")
        self.pushButton_5 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_5.setGeometry(QtCore.QRect(70, 140, 71, 71))
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_6 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_6.setGeometry(QtCore.QRect(140, 140, 71, 71))
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_divide = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_divide.setGeometry(QtCore.QRect(210, 140, 71, 71))
        self.pushButton_divide.setObjectName("pushButton_divide")
        self.pushButton_1 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_1.setGeometry(QtCore.QRect(0, 210, 71, 71))
        self.pushButton_1.setObjectName("pushButton_1")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(70, 210, 71, 71))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(140, 210, 71, 71))
        self.pushButton_3.setObjectName("pushButton_3")
        self.pushButton_multiply = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_multiply.setGeometry(QtCore.QRect(210, 210, 71, 71))
        self.pushButton_multiply.setObjectName("pushButton_multiply")
        self.pushButton_0 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_0.setGeometry(QtCore.QRect(0, 280, 71, 71))
        self.pushButton_0.setObjectName("pushButton_0")
        self.pushButton_plus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_plus.setGeometry(QtCore.QRect(70, 280, 71, 71))
        self.pushButton_plus.setObjectName("pushButton_plus")
        self.pushButton_minus = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_minus.setGeometry(QtCore.QRect(140, 280, 71, 71))
        self.pushButton_minus.setObjectName("pushButton_minus")
        self.pushButton_equal = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_equal.setGeometry(QtCore.QRect(210, 0, 71, 71))
        self.pushButton_equal.setObjectName("pushButton_equal")
        self.lineEdit_output = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_output.setGeometry(QtCore.QRect(0, 0, 211, 71))
        self.lineEdit_output.setObjectName("lineEdit_output")
        self.pushButton_dot = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_dot.setGeometry(QtCore.QRect(210, 280, 71, 71))
        self.pushButton_dot.setObjectName("pushButton_dot")
        CalculatorMainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(CalculatorMainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 287, 21))
        self.menubar.setObjectName("menubar")
        CalculatorMainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(CalculatorMainWindow)
        self.statusbar.setObjectName("statusbar")
        CalculatorMainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(CalculatorMainWindow)
        self.pushButton_c.clicked.connect(self.lineEdit_output.clear)
        QtCore.QMetaObject.connectSlotsByName(CalculatorMainWindow)

    def retranslateUi(self, CalculatorMainWindow):
        _translate = QtCore.QCoreApplication.translate
        CalculatorMainWindow.setWindowTitle(_translate("CalculatorMainWindow", "Calculator"))
        self.pushButton_7.setText(_translate("CalculatorMainWindow", "7"))
        self.pushButton_8.setText(_translate("CalculatorMainWindow", "8"))
        self.pushButton_9.setText(_translate("CalculatorMainWindow", "9"))
        self.pushButton_c.setText(_translate("CalculatorMainWindow", "C"))
        self.pushButton_4.setText(_translate("CalculatorMainWindow", "4"))
        self.pushButton_5.setText(_translate("CalculatorMainWindow", "5"))
        self.pushButton_6.setText(_translate("CalculatorMainWindow", "6"))
        self.pushButton_divide.setText(_translate("CalculatorMainWindow", "÷"))
        self.pushButton_1.setText(_translate("CalculatorMainWindow", "1"))
        self.pushButton_2.setText(_translate("CalculatorMainWindow", "2"))
        self.pushButton_3.setText(_translate("CalculatorMainWindow", "3"))
        self.pushButton_multiply.setText(_translate("CalculatorMainWindow", "x"))
        self.pushButton_0.setText(_translate("CalculatorMainWindow", "0"))
        self.pushButton_plus.setText(_translate("CalculatorMainWindow", "+"))
        self.pushButton_minus.setText(_translate("CalculatorMainWindow", "-"))
        self.pushButton_equal.setText(_translate("CalculatorMainWindow", "="))
        self.pushButton_dot.setText(_translate("CalculatorMainWindow", "."))
