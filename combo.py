# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'combo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(Form)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.t1 = QtWidgets.QLineEdit(Form)
        self.t1.setObjectName("t1")
        self.horizontalLayout.addWidget(self.t1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.bt1 = QtWidgets.QPushButton(Form)
        self.bt1.setObjectName("bt1")
        self.horizontalLayout.addWidget(self.bt1)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.c1 = QtWidgets.QComboBox(Form)
        self.c1.setObjectName("c1")
        self.c1.addItem("")
        self.c1.addItem("")
        self.c1.addItem("")
        self.horizontalLayout_2.addWidget(self.c1)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem1)
        self.bt2 = QtWidgets.QPushButton(Form)
        self.bt2.setObjectName("bt2")
        self.horizontalLayout_2.addWidget(self.bt2)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.t2 = QtWidgets.QLineEdit(Form)
        self.t2.setObjectName("t2")
        self.verticalLayout.addWidget(self.t2)
        self.bt1.clicked.connect(self.remitem)
        self.bt2.clicked.connect(self.additem)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.bt1.setText(_translate("Form", "PushButton"))
        self.c1.setItemText(0, _translate("Form", "c"))
        self.c1.setItemText(1, _translate("Form", "c++"))
        self.c1.setItemText(2, _translate("Form", "java"))
        self.bt2.setText(_translate("Form", "PushButton"))

    def remitem(self):
        indx=self.c1.currentIndex()
        item=self.c1.currentText()

        self.t2.setText(item+"is removed")
        self.c1.removeItem(indx)

    def additem(self):
        
        self.c1.addItem(self.t1.text())
        self.t2.setText(self.t1.text()+ "is added")


    
        


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

