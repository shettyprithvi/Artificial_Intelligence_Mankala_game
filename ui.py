# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'all.ui'
#
# Created: Sat Apr 26 22:09:41 2014
#      by: PyQt4 UI code generator 4.10.4
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


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName(_fromUtf8("Dialog"))
        Dialog.resize(542, 226)
        sizePolicy = QtGui.QSizePolicy(QtGui.QSizePolicy.Fixed, QtGui.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(Dialog.sizePolicy().hasHeightForWidth())
        Dialog.setSizePolicy(sizePolicy)
        Dialog.setMinimumSize(QtCore.QSize(420, 226))
        Dialog.setMaximumSize(QtCore.QSize(950, 226))
        self.wMain = QtGui.QWidget(Dialog)
        self.wMain.setGeometry(QtCore.QRect(10, 10, 521, 211))
        self.wMain.setObjectName(_fromUtf8("wMain"))
        self.pbB1 = QtGui.QPushButton(self.wMain)
        self.pbB1.setGeometry(QtCore.QRect(380, 40, 61, 61))
        self.pbB1.setObjectName(_fromUtf8("pbB1"))
        self.pbB = QtGui.QPushButton(self.wMain)
        self.pbB.setEnabled(True)
        self.pbB.setGeometry(QtCore.QRect(0, 40, 71, 141))
        self.pbB.setAutoDefault(False)
        self.pbB.setObjectName(_fromUtf8("pbB"))
        self.pbA2 = QtGui.QPushButton(self.wMain)
        self.pbA2.setGeometry(QtCore.QRect(140, 120, 61, 61))
        self.pbA2.setObjectName(_fromUtf8("pbA2"))
        self.pbB5 = QtGui.QPushButton(self.wMain)
        self.pbB5.setGeometry(QtCore.QRect(140, 40, 61, 61))
        self.pbB5.setObjectName(_fromUtf8("pbB5"))
        self.pbA = QtGui.QPushButton(self.wMain)
        self.pbA.setGeometry(QtCore.QRect(450, 40, 71, 141))
        self.pbA.setObjectName(_fromUtf8("pbA"))
        self.pbA1 = QtGui.QPushButton(self.wMain)
        self.pbA1.setGeometry(QtCore.QRect(80, 120, 61, 61))
        self.pbA1.setObjectName(_fromUtf8("pbA1"))
        self.pbA5 = QtGui.QPushButton(self.wMain)
        self.pbA5.setGeometry(QtCore.QRect(320, 120, 61, 61))
        self.pbA5.setObjectName(_fromUtf8("pbA5"))
        self.pbA6 = QtGui.QPushButton(self.wMain)
        self.pbA6.setGeometry(QtCore.QRect(380, 120, 61, 61))
        self.pbA6.setObjectName(_fromUtf8("pbA6"))
        self.lStatus = QtGui.QLabel(self.wMain)
        self.lStatus.setGeometry(QtCore.QRect(10, 190, 501, 16))
        self.lStatus.setText(_fromUtf8(""))
        self.lStatus.setObjectName(_fromUtf8("lStatus"))
        self.pbB6 = QtGui.QPushButton(self.wMain)
        self.pbB6.setGeometry(QtCore.QRect(80, 40, 61, 61))
        self.pbB6.setCheckable(False)
        self.pbB6.setObjectName(_fromUtf8("pbB6"))
        self.pbB2 = QtGui.QPushButton(self.wMain)
        self.pbB2.setGeometry(QtCore.QRect(320, 40, 61, 61))
        self.pbB2.setObjectName(_fromUtf8("pbB2"))
        self.pbA3 = QtGui.QPushButton(self.wMain)
        self.pbA3.setGeometry(QtCore.QRect(200, 120, 61, 61))
        self.pbA3.setObjectName(_fromUtf8("pbA3"))
        self.pbB4 = QtGui.QPushButton(self.wMain)
        self.pbB4.setGeometry(QtCore.QRect(200, 40, 61, 61))
        self.pbB4.setObjectName(_fromUtf8("pbB4"))
        self.pbA4 = QtGui.QPushButton(self.wMain)
        self.pbA4.setGeometry(QtCore.QRect(260, 120, 61, 61))
        self.pbA4.setObjectName(_fromUtf8("pbA4"))
        self.pbB3 = QtGui.QPushButton(self.wMain)
        self.pbB3.setGeometry(QtCore.QRect(260, 40, 61, 61))
        self.pbB3.setObjectName(_fromUtf8("pbB3"))
        self.wStart = QtGui.QWidget(Dialog)
        self.wStart.setGeometry(QtCore.QRect(0, 10, 411, 211))
        self.wStart.setObjectName(_fromUtf8("wStart"))
        self.tabWidget = QtGui.QTabWidget(self.wStart)
        self.tabWidget.setGeometry(QtCore.QRect(10, 10, 391, 191))
        self.tabWidget.setObjectName(_fromUtf8("tabWidget"))
        self.tab = QtGui.QWidget()
        self.tab.setObjectName(_fromUtf8("tab"))
        self.pbPlayHuman = QtGui.QPushButton(self.tab)
        self.pbPlayHuman.setEnabled(True)
        self.pbPlayHuman.setGeometry(QtCore.QRect(140, 120, 101, 21))
        self.pbPlayHuman.setObjectName(_fromUtf8("pbPlayHuman"))
        self.label_2 = QtGui.QLabel(self.tab)
        self.label_2.setGeometry(QtCore.QRect(140, 70, 101, 16))
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.pbSelectFile = QtGui.QPushButton(self.tab)
        self.pbSelectFile.setGeometry(QtCore.QRect(140, 20, 101, 23))
        self.pbSelectFile.setObjectName(_fromUtf8("pbSelectFile"))
        self.cbTime = QtGui.QComboBox(self.tab)
        self.cbTime.setGeometry(QtCore.QRect(140, 90, 101, 20))
        self.cbTime.setObjectName(_fromUtf8("cbTime"))
        self.cbTime.addItem(_fromUtf8(""))
        self.cbTime.addItem(_fromUtf8(""))
        self.cbTime.addItem(_fromUtf8(""))
        self.cbTime.addItem(_fromUtf8(""))
        self.cbTime.addItem(_fromUtf8(""))
        self.lbFile = QtGui.QLabel(self.tab)
        self.lbFile.setGeometry(QtCore.QRect(140, 50, 101, 16))
        self.lbFile.setObjectName(_fromUtf8("lbFile"))
        self.tabWidget.addTab(self.tab, _fromUtf8(""))
        self.tab_2 = QtGui.QWidget()
        self.tab_2.setObjectName(_fromUtf8("tab_2"))
        self.pbCreate = QtGui.QPushButton(self.tab_2)
        self.pbCreate.setGeometry(QtCore.QRect(220, 20, 75, 23))
        self.pbCreate.setObjectName(_fromUtf8("pbCreate"))
        self.tbHostName = QtGui.QPlainTextEdit(self.tab_2)
        self.tbHostName.setGeometry(QtCore.QRect(20, 20, 191, 25))
        self.tbHostName.setObjectName(_fromUtf8("tbHostName"))
        self.label_4 = QtGui.QLabel(self.tab_2)
        self.label_4.setGeometry(QtCore.QRect(20, 0, 81, 20))
        self.label_4.setFrameShape(QtGui.QFrame.NoFrame)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.label_3 = QtGui.QLabel(self.tab_2)
        self.label_3.setGeometry(QtCore.QRect(20, 50, 71, 20))
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.lvHosts = QtGui.QListWidget(self.tab_2)
        self.lvHosts.setGeometry(QtCore.QRect(20, 70, 191, 91))
        self.lvHosts.setObjectName(_fromUtf8("lvHosts"))
        self.pbGo = QtGui.QPushButton(self.tab_2)
        self.pbGo.setGeometry(QtCore.QRect(220, 140, 161, 23))
        self.pbGo.setObjectName(_fromUtf8("pbGo"))
        self.pbCancel = QtGui.QPushButton(self.tab_2)
        self.pbCancel.setGeometry(QtCore.QRect(300, 20, 75, 23))
        self.pbCancel.setObjectName(_fromUtf8("pbCancel"))
        self.cbInternetOption = QtGui.QComboBox(self.tab_2)
        self.cbInternetOption.setGeometry(QtCore.QRect(220, 50, 161, 20))
        self.cbInternetOption.setObjectName(_fromUtf8("cbInternetOption"))
        self.cbInternetOption.addItem(_fromUtf8(""))
        self.cbInternetOption.addItem(_fromUtf8(""))
        self.tabWidget.addTab(self.tab_2, _fromUtf8(""))

        self.retranslateUi(Dialog)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(_translate("Dialog", "Kalah - EE562 - Autumn 2018", None))
        self.pbB1.setText(_translate("Dialog", "0", None))
        self.pbB.setText(_translate("Dialog", "0", None))
        self.pbA2.setText(_translate("Dialog", "0", None))
        self.pbB5.setText(_translate("Dialog", "0", None))
        self.pbA.setText(_translate("Dialog", "0", None))
        self.pbA1.setText(_translate("Dialog", "0", None))
        self.pbA5.setText(_translate("Dialog", "0", None))
        self.pbA6.setText(_translate("Dialog", "0", None))
        self.pbB6.setText(_translate("Dialog", "0", None))
        self.pbB2.setText(_translate("Dialog", "0", None))
        self.pbA3.setText(_translate("Dialog", "0", None))
        self.pbB4.setText(_translate("Dialog", "0", None))
        self.pbA4.setText(_translate("Dialog", "0", None))
        self.pbB3.setText(_translate("Dialog", "0", None))
        self.pbPlayHuman.setText(_translate("Dialog", "Play with AI", None))
        self.label_2.setText(_translate("Dialog", "Time limit (ms):", None))
        self.pbSelectFile.setText(_translate("Dialog", "Open AI File", None))
        self.cbTime.setItemText(0, _translate("Dialog", "100", None))
        self.cbTime.setItemText(1, _translate("Dialog", "500", None))
        self.cbTime.setItemText(2, _translate("Dialog", "1000", None))
        self.cbTime.setItemText(3, _translate("Dialog", "2000", None))
        self.cbTime.setItemText(4, _translate("Dialog", "5000", None))
        self.lbFile.setText(_translate("Dialog", "No file selected", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Dialog", "Local AI", None))
        self.pbCreate.setText(_translate("Dialog", "Create", None))
        self.tbHostName.setPlainText(_translate("Dialog", "Game Name", None))
        self.label_4.setText(_translate("Dialog", "Create game:", None))
        self.label_3.setText(_translate("Dialog", "Or join game:", None))
        self.pbGo.setText(_translate("Dialog", "Play with Internet", None))
        self.pbCancel.setText(_translate("Dialog", "Cancel", None))
        self.cbInternetOption.setItemText(0, _translate("Dialog", "Play with human", None))
        self.cbInternetOption.setItemText(1, _translate("Dialog", "Play with AI", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Dialog", "Internet", None))

