# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\soohw\Desktop\DemoUI\Demo.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!
from demo.demo_savetx import transaction_generator
from PyQt5 import QtCore, QtGui, QtWidgets
from demo.demo_savetx import request_test

import queue
import json
transaction_queue = queue.Queue()
requests_url = None

class Ui_LogchainDemo(object):
    def setupUi(self, LogchainDemo):
        LogchainDemo.setObjectName("LogchainDemo")
        LogchainDemo.resize(592, 682)
        palette = QtGui.QPalette()
        brush = QtGui.QBrush(QtGui.QColor(116, 116, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 152, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Active, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(116, 116, 116))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 152, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Inactive, QtGui.QPalette.Button, brush)
        brush = QtGui.QBrush(QtGui.QColor(120, 120, 120))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.WindowText, brush)
        brush = QtGui.QBrush(QtGui.QColor(152, 152, 152))
        brush.setStyle(QtCore.Qt.SolidPattern)
        palette.setBrush(QtGui.QPalette.Disabled, QtGui.QPalette.Button, brush)
        LogchainDemo.setPalette(palette)
        self.label = QtWidgets.QLabel(LogchainDemo)
        self.label.setGeometry(QtCore.QRect(10, 20, 161, 21))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(LogchainDemo)
        self.pushButton.setGeometry(QtCore.QRect(20, 70, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(LogchainDemo)
        self.pushButton_2.setGeometry(QtCore.QRect(20, 420, 251, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.line_2 = QtWidgets.QFrame(LogchainDemo)
        self.line_2.setGeometry(QtCore.QRect(10, 310, 560, 16))
        self.line_2.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line = QtWidgets.QFrame(LogchainDemo)
        self.line.setGeometry(QtCore.QRect(0, 60, 21, 600))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_3 = QtWidgets.QFrame(LogchainDemo)
        self.line_3.setGeometry(QtCore.QRect(10, 660, 560, 3))
        self.line_3.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(LogchainDemo)
        self.line_4.setGeometry(QtCore.QRect(560, 60, 20, 600))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(LogchainDemo)
        self.line_5.setGeometry(QtCore.QRect(10, 60, 560, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.textEdit = QtWidgets.QTextEdit(LogchainDemo)
        self.textEdit.setGeometry(QtCore.QRect(20, 110, 541, 201))
        self.textEdit.setObjectName("textEdit")
        self.textEdit_2 = QtWidgets.QTextEdit(LogchainDemo)
        self.textEdit_2.setGeometry(QtCore.QRect(20, 460, 541, 191))
        self.textEdit_2.setObjectName("textEdit_2")
        self.label_2 = QtWidgets.QLabel(LogchainDemo)
        self.label_2.setGeometry(QtCore.QRect(20, 330, 141, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(LogchainDemo)
        self.label_3.setGeometry(QtCore.QRect(20, 370, 51, 16))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.textEdit_3 = QtWidgets.QTextEdit(LogchainDemo)
        self.textEdit_3.setGeometry(QtCore.QRect(80, 360, 381, 31))
        self.textEdit_3.setObjectName("textEdit_3")
        self.pushButton_3 = QtWidgets.QPushButton(LogchainDemo)
        self.pushButton_3.setGeometry(QtCore.QRect(480, 362, 75, 31))
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")

        # generate transaction
        self.pushButton.clicked.connect(self.generate_transaction)
        # send_transaction
        self.pushButton_2.clicked.connect(self.send_transaction)
        # set
        self.pushButton_3.clicked.connect(self.set_request_url)


        self.retranslateUi(LogchainDemo)
        QtCore.QMetaObject.connectSlotsByName(LogchainDemo)

    def retranslateUi(self, LogchainDemo):
        _translate = QtCore.QCoreApplication.translate
        LogchainDemo.setWindowTitle(_translate("LogchainDemo", "Dialog"))
        self.label.setText(_translate("LogchainDemo", "Logchain Demo UI"))
        self.pushButton.setText(_translate("LogchainDemo", "Generate transaction(IoT)"))
        self.pushButton_2.setText(_translate("LogchainDemo", "Send transaction"))
        self.label_2.setText(_translate("LogchainDemo", "Post Man "))
        self.label_3.setText(_translate("LogchainDemo", "URL :"))
        self.pushButton_3.setText(_translate("LogchainDemo", "Set "))


    def generate_transaction(self):

        tx= transaction_generator.transaction_generator()
        transaction_queue.put(tx)
        self.textEdit.append(json.dumps(tx,indent=4))
        self.textEdit.append("  ")
        self.textEdit.append("  ")

    def set_request_url(self):
        requests_url = self.textEdit_3.toPlainText()
        self.textEdit_2.append("Post : ")
        self.textEdit_2.append(requests_url)

    def send_transaction(self):
        requests_url = self.textEdit_3.toPlainText()
        tx= transaction_queue.get()
        try:
            response=request_test.post_transaction(requests_url,tx)
            self.textEdit_2.append(str(response.text))
        except Exception as e:
            print(e)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    LogchainDemo = QtWidgets.QDialog()
    ui = Ui_LogchainDemo()
    ui.setupUi(LogchainDemo)
    LogchainDemo.show()
    sys.exit(app.exec_())

