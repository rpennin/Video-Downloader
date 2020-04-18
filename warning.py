# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\warning.ui'
#
# Created by: PyQt5 UI code generator 5.14.2
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_WarningDialogue(object):
    def setupUi(self, WarningDialogue):
        WarningDialogue.setObjectName("WarningDialogue")
        WarningDialogue.resize(287, 109)
        font = QtGui.QFont()
        font.setPointSize(12)
        WarningDialogue.setFont(font)
        self.horizontalLayout = QtWidgets.QHBoxLayout(WarningDialogue)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.warningLabel = QtWidgets.QLabel(WarningDialogue)
        self.warningLabel.setObjectName("warningLabel")
        self.horizontalLayout.addWidget(self.warningLabel, 0, QtCore.Qt.AlignHCenter|QtCore.Qt.AlignVCenter)

        self.retranslateUi(WarningDialogue)
        QtCore.QMetaObject.connectSlotsByName(WarningDialogue)

    def retranslateUi(self, WarningDialogue):
        _translate = QtCore.QCoreApplication.translate
        WarningDialogue.setWindowTitle(_translate("WarningDialogue", "Warning!"))
        self.warningLabel.setText(_translate("WarningDialogue", "TextLabel"))
