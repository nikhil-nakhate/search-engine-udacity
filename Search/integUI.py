# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'integUI.ui'
#
# Created: Mon Apr 22 23:10:01 2013
#      by: PyQt4 UI code generator 4.10
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_mainDialog(object):
    def setupUi(self, mainDialog):
        mainDialog.setObjectName(_fromUtf8("mainDialog"))
        mainDialog.resize(308, 85)
        self.nameEdit = QtGui.QLineEdit(mainDialog)
        self.nameEdit.setGeometry(QtCore.QRect(20, 30, 113, 20))
        self.nameEdit.setText(_fromUtf8(""))
        self.nameEdit.setObjectName(_fromUtf8("nameEdit"))
        self.showButton = QtGui.QPushButton(mainDialog)
        self.showButton.setGeometry(QtCore.QRect(180, 30, 75, 23))
        self.showButton.setObjectName(_fromUtf8("showButton"))

        self.retranslateUi(mainDialog)
        QtCore.QMetaObject.connectSlotsByName(mainDialog)
        mainDialog.setTabOrder(self.showButton, self.nameEdit)

    def retranslateUi(self, mainDialog):
        mainDialog.setWindowTitle(_translate("mainDialog", "Main Dialog", None))
        self.nameEdit.setPlaceholderText(_translate("mainDialog", "What is your name", None))
        self.showButton.setText(_translate("mainDialog", "Show!", None))

