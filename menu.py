# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'menu.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

import math

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(110, 80, 55, 16))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(120, 170, 55, 16))
        self.label_2.setObjectName("label_2")
        self.t1 = QtWidgets.QLineEdit(self.centralwidget)
        self.t1.setGeometry(QtCore.QRect(250, 80, 113, 22))
        self.t1.setObjectName("t1")
        self.t2 = QtWidgets.QLineEdit(self.centralwidget)
        self.t2.setGeometry(QtCore.QRect(260, 170, 113, 22))
        self.t2.setObjectName("t2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        self.menufile = QtWidgets.QMenu(self.menubar)
        self.menufile.setObjectName("menufile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actioncube = QtWidgets.QAction(MainWindow)
        self.actioncube.setObjectName("actioncube")
        self.actionsquare = QtWidgets.QAction(MainWindow)
        self.actionsquare.setObjectName("actionsquare")
        self.actionquit = QtWidgets.QAction(MainWindow)
        self.actionquit.setObjectName("actionquit")
        self.menufile.addAction(self.actioncube)
        self.menufile.addAction(self.actionsquare)
        self.menufile.addSeparator()
        self.menufile.addSeparator()
        self.menufile.addAction(self.actionquit)
        self.menubar.addAction(self.menufile.menuAction())
        self.menufile.triggered[QtWidgets.QAction].connect(self.menufunction)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "no."))
        self.label_2.setText(_translate("MainWindow", "res"))
        self.menufile.setTitle(_translate("MainWindow", "file"))
        self.actioncube.setText(_translate("MainWindow", "cube"))
        self.actionsquare.setText(_translate("MainWindow", "square"))
        self.actionquit.setText(_translate("MainWindow", "quit"))

    def menufunction(self,action):
        txt=(action.text())
        no=int(self.t1.text())
        print(txt,no)

        if txt=='cube':
            self.t2.setText(str(no*no*no))

        if txt=='square':
            self.t2.setText(str(no*no))

        
            
            
    


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

