# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(616, 432)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(MainWindow.sizePolicy().hasHeightForWidth())
        MainWindow.setSizePolicy(sizePolicy)
        MainWindow.setMinimumSize(QtCore.QSize(616, 432))
        MainWindow.setMaximumSize(QtCore.QSize(616, 432))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.depositButton = QtWidgets.QPushButton(self.centralwidget)
        self.depositButton.setGeometry(QtCore.QRect(280, 70, 171, 41))
        self.depositButton.setObjectName("depositButton")
        self.withdrawButton = QtWidgets.QPushButton(self.centralwidget)
        self.withdrawButton.setGeometry(QtCore.QRect(280, 20, 171, 41))
        self.withdrawButton.setObjectName("withdrawButton")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 80, 111, 16))
        self.label.setObjectName("label")
        self.currentBalanceLabel = QtWidgets.QLabel(self.centralwidget)
        self.currentBalanceLabel.setGeometry(QtCore.QRect(120, 80, 141, 16))
        self.currentBalanceLabel.setObjectName("currentBalanceLabel")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 50, 111, 16))
        self.label_3.setObjectName("label_3")
        self.accountNameLabel = QtWidgets.QLabel(self.centralwidget)
        self.accountNameLabel.setGeometry(QtCore.QRect(120, 50, 161, 21))
        self.accountNameLabel.setObjectName("accountNameLabel")
        self.setBalanceButton = QtWidgets.QPushButton(self.centralwidget)
        self.setBalanceButton.setGeometry(QtCore.QRect(280, 120, 171, 41))
        self.setBalanceButton.setObjectName("setBalanceButton")
        self.saveButton = QtWidgets.QPushButton(self.centralwidget)
        self.saveButton.setGeometry(QtCore.QRect(280, 220, 171, 41))
        self.saveButton.setObjectName("saveButton")
        self.newAccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.newAccountButton.setGeometry(QtCore.QRect(20, 150, 171, 41))
        self.newAccountButton.setObjectName("newAccountButton")
        self.withdrawAmountEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.withdrawAmountEntry.setGeometry(QtCore.QRect(460, 20, 131, 31))
        self.withdrawAmountEntry.setObjectName("withdrawAmountEntry")
        self.depositAmountEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.depositAmountEntry.setGeometry(QtCore.QRect(460, 70, 131, 31))
        self.depositAmountEntry.setObjectName("depositAmountEntry")
        self.setBalanceEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.setBalanceEntry.setGeometry(QtCore.QRect(460, 120, 131, 31))
        self.setBalanceEntry.setObjectName("setBalanceEntry")
        self.newSavingsAccountButton = QtWidgets.QPushButton(self.centralwidget)
        self.newSavingsAccountButton.setGeometry(QtCore.QRect(20, 200, 171, 41))
        self.newSavingsAccountButton.setObjectName("newSavingsAccountButton")
        self.saveFileEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.saveFileEntry.setGeometry(QtCore.QRect(460, 230, 131, 31))
        self.saveFileEntry.setObjectName("saveFileEntry")
        self.newAccountNameEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.newAccountNameEntry.setGeometry(QtCore.QRect(460, 170, 131, 31))
        self.newAccountNameEntry.setObjectName("newAccountNameEntry")
        self.changeNameButton = QtWidgets.QPushButton(self.centralwidget)
        self.changeNameButton.setGeometry(QtCore.QRect(280, 170, 171, 41))
        self.changeNameButton.setObjectName("changeNameButton")
        self.errorLabel = QtWidgets.QLabel(self.centralwidget)
        self.errorLabel.setGeometry(QtCore.QRect(20, 260, 231, 111))
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(255, 0, 0))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        self.errorLabel.setPalette(palette)
        font = QtGui.QFont()
        font.setBold(True)
        font.setWeight(75)
        self.errorLabel.setFont(font)
        self.errorLabel.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignTop)
        self.errorLabel.setWordWrap(True)
        self.errorLabel.setObjectName("errorLabel")
        self.loadButton = QtWidgets.QPushButton(self.centralwidget)
        self.loadButton.setGeometry(QtCore.QRect(280, 270, 171, 41))
        self.loadButton.setObjectName("loadButton")
        self.loadFileEntry = QtWidgets.QLineEdit(self.centralwidget)
        self.loadFileEntry.setGeometry(QtCore.QRect(460, 270, 131, 31))
        self.loadFileEntry.setObjectName("loadFileEntry")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 110, 111, 16))
        self.label_2.setObjectName("label_2")
        self.accountTypeLabel = QtWidgets.QLabel(self.centralwidget)
        self.accountTypeLabel.setGeometry(QtCore.QRect(110, 110, 141, 16))
        self.accountTypeLabel.setObjectName("accountTypeLabel")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 616, 22))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Bank Account Manager"))
        self.depositButton.setText(_translate("MainWindow", "Deposit"))
        self.withdrawButton.setText(_translate("MainWindow", "Withdraw"))
        self.label.setText(_translate("MainWindow", "Current Balance:"))
        self.currentBalanceLabel.setText(_translate("MainWindow", "set me with program"))
        self.label_3.setText(_translate("MainWindow", "Account Name:"))
        self.accountNameLabel.setText(_translate("MainWindow", "set me with program"))
        self.setBalanceButton.setText(_translate("MainWindow", "Set Balance"))
        self.saveButton.setText(_translate("MainWindow", "Save Account to file"))
        self.newAccountButton.setText(_translate("MainWindow", "Create New Account"))
        self.newSavingsAccountButton.setText(_translate("MainWindow", "Create New Savings Account"))
        self.changeNameButton.setText(_translate("MainWindow", "Set Account Name"))
        self.errorLabel.setText(_translate("MainWindow", "TextLabel"))
        self.loadButton.setText(_translate("MainWindow", "Load Account from file"))
        self.label_2.setText(_translate("MainWindow", "Account Type:"))
        self.accountTypeLabel.setText(_translate("MainWindow", "Basic Account"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
