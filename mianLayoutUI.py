# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mianLayoutUI.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(444, 359)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(71, 85, 298, 225))
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout.setSpacing(20)
        self.verticalLayout.setObjectName("verticalLayout")
        self.textEdit_result = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit_result.setObjectName("textEdit_result")
        self.verticalLayout.addWidget(self.textEdit_result)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton_query = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_query.setObjectName("pushButton_query")
        self.horizontalLayout.addWidget(self.pushButton_query)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton_clear = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_clear.setObjectName("pushButton_clear")
        self.horizontalLayout.addWidget(self.pushButton_clear)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.layoutWidget1 = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget1.setGeometry(QtCore.QRect(71, 31, 171, 44))
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.gridLayout = QtWidgets.QGridLayout(self.layoutWidget1)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setVerticalSpacing(10)
        self.gridLayout.setObjectName("gridLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget1)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 2)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget1)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.comboBox_city = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_city.setAutoFillBackground(False)
        self.comboBox_city.setObjectName("comboBox_city")
        self.comboBox_city.addItem("")
        self.comboBox_city.addItem("")
        self.comboBox_city.addItem("")
        self.comboBox_city.addItem("")
        self.gridLayout.addWidget(self.comboBox_city, 1, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.pushButton_query.setText(_translate("MainWindow", "查询"))
        self.pushButton_clear.setText(_translate("MainWindow", "清空"))
        self.label.setText(_translate("MainWindow", "查询城市天气"))
        self.label_2.setText(_translate("MainWindow", "城市"))
        self.comboBox_city.setItemText(0, _translate("MainWindow", "北京"))
        self.comboBox_city.setItemText(1, _translate("MainWindow", "上海"))
        self.comboBox_city.setItemText(2, _translate("MainWindow", "天津"))
        self.comboBox_city.setItemText(3, _translate("MainWindow", "广州"))

