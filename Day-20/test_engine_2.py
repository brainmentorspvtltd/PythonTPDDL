# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testEngine.ui'
#
# Created by: PyQt5 UI code generator 5.9
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

options =[
    ['row_1_opt1','row_1_opt_2','row_1_opt_3','row_1_opt_4'],
    ['row_2_opt1','row_2_opt_2','row_2_opt_3','row_2_opt_4'],
    ['row_3_opt1','row_3_opt_2','row_3_opt_3','row_3_opt_4'],
    ['row_4_opt1','row_4_opt_2','row_4_opt_3','row_4_opt_4']
]

class Ui_MainWindow(QtWidgets.QMainWindow):
    count = 0
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1151, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.frame = QtWidgets.QFrame(self.centralwidget)
        self.frame.setGeometry(QtCore.QRect(-1, -1, 1151, 741))
        self.frame.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setGeometry(QtCore.QRect(210, 180, 281, 61))
        self.label.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setGeometry(QtCore.QRect(210, 290, 281, 61))
        self.label_2.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";")
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setGeometry(QtCore.QRect(570, 180, 411, 61))
        self.lineEdit.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame)
        self.lineEdit_2.setGeometry(QtCore.QRect(570, 300, 411, 61))
        self.lineEdit_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.pushButton = QtWidgets.QPushButton(self.frame)
        self.pushButton.setGeometry(QtCore.QRect(460, 450, 271, 61))
        self.pushButton.setStyleSheet("font: 18pt \"MS Shell Dlg 2\";\n"
"background-color: rgb(255, 170, 127);")
        self.pushButton.setObjectName("pushButton")
        self.frame_2 = QtWidgets.QFrame(self.frame)
        self.frame_2.setGeometry(QtCore.QRect(-1, -1, 1151, 741))
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        self.label_3.setGeometry(QtCore.QRect(70, 90, 1001, 91))
        self.label_3.setStyleSheet("font: 14pt \"MS Shell Dlg 2\";")
        self.label_3.setObjectName("label_3")
        self.radioButton = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton.setGeometry(QtCore.QRect(100, 220, 271, 51))
        self.radioButton.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton.setObjectName("radioButton")
        self.radioButton_2 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_2.setGeometry(QtCore.QRect(100, 300, 351, 51))
        self.radioButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_2.setObjectName("radioButton_2")
        self.radioButton_3 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_3.setGeometry(QtCore.QRect(100, 380, 271, 51))
        self.radioButton_3.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_3.setObjectName("radioButton_3")
        self.radioButton_4 = QtWidgets.QRadioButton(self.frame_2)
        self.radioButton_4.setGeometry(QtCore.QRect(100, 470, 271, 51))
        self.radioButton_4.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.radioButton_4.setObjectName("radioButton_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.frame_2)
        self.pushButton_2.setGeometry(QtCore.QRect(770, 580, 301, 61))
        self.pushButton_2.setStyleSheet("font: 16pt \"MS Shell Dlg 2\";")
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1151, 31))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.frame.show()
        self.frame_2.hide()

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Enter Username"))
        self.label_2.setText(_translate("MainWindow", "Enter Password"))
        self.pushButton.setText(_translate("MainWindow", "Enter Test"))
        self.label_3.setText(_translate("MainWindow", "1. Who invented Python Programming ?"))
        # self.radioButton.setText(_translate("MainWindow", "Sergery Bin"))
        # self.radioButton_2.setText(_translate("MainWindow", "Guido Van Rossum"))
        # self.radioButton_3.setText(_translate("MainWindow", "Brendon Eich"))
        # self.radioButton_4.setText(_translate("MainWindow", "Larry Page"))
        self.pushButton_2.setText(_translate("MainWindow", "Next Question"))

        for i in range(len(options)):
            self.radioButton.setText(options[self.count][0])
            self.radioButton_2.setText(options[self.count][1])
            self.radioButton_3.setText(options[self.count][2])
            self.radioButton_4.setText(options[self.count][3])

        self.pushButton.clicked.connect(self.login)
        self.pushButton_2.clicked.connect(self.checkAns)

        self.radioButton.toggled.connect(self.check_radio_button)
        self.radioButton_2.toggled.connect(self.check_radio_button)
        self.radioButton_3.toggled.connect(self.check_radio_button)
        self.radioButton_4.toggled.connect(self.check_radio_button)

    def login(self):
        self.username = self.lineEdit.text()
        self.userpwd = self.lineEdit_2.text()

        if self.username == self.userpwd:
            self.login_success()
        else:
            print("Login Failed")

    def login_success(self):
        self.frame_2.show()

    def checkAns(self):
        self.count += 1
        print(self.count)
        self.retranslateUi(MainWindow)

    def check_radio_button(self):
        radiobutton = self.sender()
        if radiobutton.isChecked():
            print(radiobutton.text())


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

