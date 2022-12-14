# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(494, 602)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.Title_Label = QtWidgets.QLabel(self.centralwidget)
        self.Title_Label.setGeometry(QtCore.QRect(160, 0, 161, 81))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(28)
        font.setBold(True)
        font.setWeight(87)
        self.Title_Label.setFont(font)
        self.Title_Label.setStyleSheet("color:rgb(255, 0, 0);\n"
"font-weight:700;\n"
"")
        self.Title_Label.setAlignment(QtCore.Qt.AlignCenter)
        self.Title_Label.setObjectName("Title_Label")
        self.label_1 = QtWidgets.QLabel(self.centralwidget)
        self.label_1.setGeometry(QtCore.QRect(30, 70, 221, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.label_1.setFont(font)
        self.label_1.setObjectName("label_1")
        self.original_text = QtWidgets.QTextEdit(self.centralwidget)
        self.original_text.setGeometry(QtCore.QRect(30, 120, 441, 101))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.original_text.setFont(font)
        self.original_text.setObjectName("original_text")
        self.file_btn = QtWidgets.QPushButton(self.centralwidget)
        self.file_btn.setGeometry(QtCore.QRect(370, 80, 101, 31))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.file_btn.setFont(font)
        self.file_btn.setObjectName("file_btn")
        self.encry_btn = QtWidgets.QPushButton(self.centralwidget)
        self.encry_btn.setGeometry(QtCore.QRect(30, 240, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.encry_btn.setFont(font)
        self.encry_btn.setObjectName("encry_btn")
        self.clear_btn = QtWidgets.QPushButton(self.centralwidget)
        self.clear_btn.setGeometry(QtCore.QRect(370, 240, 100, 40))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(20)
        self.clear_btn.setFont(font)
        self.clear_btn.setObjectName("clear_btn")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(190, 290, 121, 51))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(22)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.res_shower = QtWidgets.QTextEdit(self.centralwidget)
        self.res_shower.setGeometry(QtCore.QRect(30, 350, 441, 111))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(18)
        self.res_shower.setFont(font)
        self.res_shower.setObjectName("res_shower")
        self.exit_btn = QtWidgets.QPushButton(self.centralwidget)
        self.exit_btn.setGeometry(QtCore.QRect(30, 480, 441, 71))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(24)
        self.exit_btn.setFont(font)
        self.exit_btn.setObjectName("exit_btn")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 494, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.exit_btn.clicked.connect(self.exit_btn.close)
        self.exit_btn.clicked.connect(self.exit_btn.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.Title_Label.setText(_translate("MainWindow", "MD5??????"))
        self.label_1.setText(_translate("MainWindow", "????????????????????????"))
        self.file_btn.setText(_translate("MainWindow", "????????????"))
        self.encry_btn.setText(_translate("MainWindow", "??????"))
        self.clear_btn.setText(_translate("MainWindow", "??????"))
        self.label_2.setText(_translate("MainWindow", "????????????"))
        self.exit_btn.setText(_translate("MainWindow", "????????????"))
