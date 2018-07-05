# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'buttons.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(573, 471)
        self.b1 = QtWidgets.QPushButton(Form)
        self.b1.setGeometry(QtCore.QRect(80, 130, 93, 28))
        self.b1.setObjectName("b1")
        self.b2 = QtWidgets.QPushButton(Form)
        self.b2.setGeometry(QtCore.QRect(150, 180, 93, 28))
        self.b2.setObjectName("b2")
        self.b3 = QtWidgets.QPushButton(Form)
        self.b3.setGeometry(QtCore.QRect(170, 270, 93, 28))
        self.b3.setObjectName("b3")
        self.b1.setCheckable(True)
        self.b1.toggle()
        self.b1.clicked.connect(self.btst)
        self.b2.clicked.connect(lambda :self.chkbtn(self.b2))
        self.b3.clicked.connect(lambda :self.chkbtn(self.b3))
        
        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.b1.setText(_translate("Form", "PushButton"))
        self.b2.setText(_translate("Form", "button2"))
        self.b3.setText(_translate("Form", "button3"))

        
    def btst(self):
        if self.b1.isChecked():
            self.b1.setText("pressed")
        else:
            self.b1.setText("released")
            
    def chkbtn(self,x):
        print("caption of btn clicked is:",x.text())

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

