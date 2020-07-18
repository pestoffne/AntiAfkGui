# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'foo.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(357, 268)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.le_period = QtWidgets.QLineEdit(self.centralwidget)
        self.le_period.setObjectName("le_period")
        self.gridLayout.addWidget(self.le_period, 1, 1, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.le_key = QtWidgets.QLineEdit(self.centralwidget)
        self.le_key.setObjectName("le_key")
        self.gridLayout.addWidget(self.le_key, 0, 1, 1, 1)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setObjectName("label_1")
        self.gridLayout.addWidget(self.label_1, 0, 0, 1, 1)
        self.button_start_stop = QtWidgets.QPushButton(self.centralwidget)
        self.button_start_stop.setObjectName("button_start_stop")
        self.gridLayout.addWidget(self.button_start_stop, 3, 0, 1, 1)
        self.le_down_time = QtWidgets.QLineEdit(self.centralwidget)
        self.le_down_time.setObjectName("le_down_time")
        self.gridLayout.addWidget(self.le_down_time, 2, 1, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Авто-нажиматель"))
        self.le_period.setText(_translate("MainWindow", "1 s"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p>Длительность нажания<br/>ms, s, m, h</p></body></html>"))
        self.le_key.setText(_translate("MainWindow", "w"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p>Интервал между нажатиями<br/>ms, s, m, h</p></body></html>"))
        self.label_1.setText(_translate("MainWindow", "Клавиша"))
        self.button_start_stop.setText(_translate("MainWindow", "Старт/Стоп"))
        self.le_down_time.setText(_translate("MainWindow", "950 ms"))
