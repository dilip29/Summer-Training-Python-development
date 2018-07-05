# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'list1.ui'
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
        self.l1 = QtWidgets.QListWidget(Form)
        self.l1.setObjectName("l1")
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.l1.addItem(item)
        self.horizontalLayout.addWidget(self.l1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.l2 = QtWidgets.QListWidget(Form)
        self.l2.setObjectName("l2")
        self.horizontalLayout.addWidget(self.l2)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_2.addWidget(self.label_2)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.label = QtWidgets.QLabel(Form)
        self.label.setObjectName("label")
        self.horizontalLayout_2.addWidget(self.label)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        __sortingEnabled = self.l1.isSortingEnabled()
        self.l1.setSortingEnabled(False)
        item = self.l1.item(0)
        item.setText(_translate("Form", "virat"))
        item = self.l1.item(1)
        item.setText(_translate("Form", "rohit"))
        item = self.l1.item(2)
        item.setText(_translate("Form", "sachin"))
        item = self.l1.item(3)
        item.setText(_translate("Form", "sehwag"))
        self.l1.setSortingEnabled(__sortingEnabled)
        self.label_2.setText(_translate("Form", "avialble players"))
        self.label.setText(_translate("Form", "selected players"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())

