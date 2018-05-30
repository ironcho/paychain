# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'C:\Users\soohw\Desktop\DemoUI\demo_ui.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from demo.demo_smartcontract import smart_contract
from demo.demo_smartcontract import request_test
from demo.demo_smartcontract import run_smartcontract
import json
import requests
requests_contract_url =None
run_contract_url = None


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(739, 539)
        self.pushButton = QtWidgets.QPushButton(Dialog)
        self.pushButton.setGeometry(QtCore.QRect(10, 80, 121, 31))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(Dialog)
        self.pushButton_2.setGeometry(QtCore.QRect(152, 150, 121, 31))
        self.pushButton_2.setObjectName("pushButton_2")
        self.pushButton_3 = QtWidgets.QPushButton(Dialog)
        self.pushButton_3.setGeometry(QtCore.QRect(550, 149, 121, 31))
        self.pushButton_3.setObjectName("pushButton_3")
        self.textEdit = QtWidgets.QTextEdit(Dialog)
        self.textEdit.setGeometry(QtCore.QRect(130, 80, 221, 31))
        self.textEdit.setObjectName("textEdit")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(10, 10, 81, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(22, 150, 161, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(390, 149, 101, 31))
        self.label_3.setObjectName("label_3")
        self.toolButton = QtWidgets.QToolButton(Dialog)
        self.toolButton.setGeometry(QtCore.QRect(20, 190, 81, 21))
        self.toolButton.setObjectName("toolButton")
        self.toolButton_2 = QtWidgets.QToolButton(Dialog)
        self.toolButton_2.setGeometry(QtCore.QRect(20, 240, 81, 21))
        self.toolButton_2.setObjectName("toolButton_2")
        self.toolButton_3 = QtWidgets.QToolButton(Dialog)
        self.toolButton_3.setGeometry(QtCore.QRect(390, 190, 101, 21))
        self.toolButton_3.setObjectName("toolButton_3")
        self.toolButton_4 = QtWidgets.QToolButton(Dialog)
        self.toolButton_4.setGeometry(QtCore.QRect(391, 236, 101, 21))
        self.toolButton_4.setObjectName("toolButton_4")
        self.textEdit_2 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_2.setGeometry(QtCore.QRect(110, 190, 221, 31))
        self.textEdit_2.setObjectName("textEdit_2")
        self.textEdit_3 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_3.setGeometry(QtCore.QRect(110, 240, 221, 121))
        self.textEdit_3.setObjectName("textEdit_3")
        self.textEdit_4 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_4.setGeometry(QtCore.QRect(110, 390, 221, 131))
        self.textEdit_4.setObjectName("textEdit_4")
        self.textEdit_5 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_5.setGeometry(QtCore.QRect(500, 190, 221, 31))
        self.textEdit_5.setObjectName("textEdit_5")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(30, 380, 161, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(Dialog)
        self.label_5.setGeometry(QtCore.QRect(400, 380, 161, 21))
        self.label_5.setObjectName("label_5")
        self.textEdit_6 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_6.setGeometry(QtCore.QRect(500, 240, 221, 131))
        self.textEdit_6.setObjectName("textEdit_6")
        self.textEdit_7 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_7.setGeometry(QtCore.QRect(500, 390, 221, 131))
        self.textEdit_7.setObjectName("textEdit_7")
        self.line = QtWidgets.QFrame(Dialog)
        self.line.setGeometry(QtCore.QRect(10, 120, 721, 16))
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.line_2 = QtWidgets.QFrame(Dialog)
        self.line_2.setGeometry(QtCore.QRect(10, 134, 3, 400))
        self.line_2.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_2.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_2.setObjectName("line_2")
        self.line_3 = QtWidgets.QFrame(Dialog)
        self.line_3.setGeometry(QtCore.QRect(360, 131, 3, 390))
        self.line_3.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_3.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_3.setObjectName("line_3")
        self.line_4 = QtWidgets.QFrame(Dialog)
        self.line_4.setGeometry(QtCore.QRect(730, 130, 3, 400))
        self.line_4.setFrameShape(QtWidgets.QFrame.VLine)
        self.line_4.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_4.setObjectName("line_4")
        self.line_5 = QtWidgets.QFrame(Dialog)
        self.line_5.setGeometry(QtCore.QRect(10, 530, 720, 3))
        self.line_5.setFrameShape(QtWidgets.QFrame.HLine)
        self.line_5.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line_5.setObjectName("line_5")
        self.pushButton_4 = QtWidgets.QPushButton(Dialog)
        self.pushButton_4.setGeometry(QtCore.QRect(370, 80, 121, 31))
        self.pushButton_4.setObjectName("pushButton_4")
        self.textEdit_8 = QtWidgets.QTextEdit(Dialog)
        self.textEdit_8.setGeometry(QtCore.QRect(500, 80, 221, 31))
        self.textEdit_8.setObjectName("textEdit_8")

        self.retranslateUi(Dialog)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

        # Set deploy URL
        self.pushButton.clicked.connect(self.set_request_url)

        # Set Run URL
        self.pushButton_4.clicked.connect(self.set_run_contract_url)

        # Deploy
        self.pushButton_2.clicked.connect(self.deploy_smart_contract)

        #Run
        self.pushButton_3.clicked.connect(self.run_smart_contract)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.pushButton.setText(_translate("Dialog", "<Deploy_URL/>"))
        self.pushButton_2.setText(_translate("Dialog", "{ Deploy }"))
        self.pushButton_3.setText(_translate("Dialog", "{ Run }"))
        self.label.setText(_translate("Dialog", "Logchain-S"))
        self.label_2.setText(_translate("Dialog", "Smart Contract Deploy"))
        self.label_3.setText(_translate("Dialog", "Smart Contract Run"))
        self.toolButton.setText(_translate("Dialog", "Title"))
        self.toolButton_2.setText(_translate("Dialog", "Body "))
        self.toolButton_3.setText(_translate("Dialog", "Contract Address"))
        self.toolButton_4.setText(_translate("Dialog", "Parameter"))
        self.label_4.setText(_translate("Dialog", "Response "))
        self.label_5.setText(_translate("Dialog", "Response "))
        self.pushButton_4.setText(_translate("Dialog", "<Run_URL/>"))

    def set_request_url(self):
        requests_contract_url = self.textEdit.toPlainText()
        self.textEdit_4.append("Request URL : "+requests_contract_url)
        self.textEdit_4.append("  ")

    def set_run_contract_url(self):
        run_contract_url = self.textEdit_8.toPlainText()
        self.textEdit_7.append("Reun Contract URL : "+run_contract_url)
        self.textEdit_7.append("  ")

    def deploy_smart_contract(self):
        #generate smartContract from input (title, body)
        requests_contract_url = self.textEdit.toPlainText()
        contract_title=self.textEdit_2.toPlainText()
        contract_body = self.textEdit_3.toPlainText()
        smartContract = smart_contract.smartContract(title,body)
        smartContract = json.dumps(smartContract, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        response=request_test.post_transaction(requests_contract_url,smartContract)
        self.textEdit_4.append(str(response))


    def run_smart_contract(self):
        run_contract_url = self.textEdit_8.toPlainText()
        address = self.textEdit_5.toPlainText()
        parameter = self.textEdit_6.toPlainText()
        RunSmartContract= run_smartcontract.runSmartContract(address,parameter)
        RunSmartContract = json.dumps(RunSmartContract, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        response = request_test.post_transaction(run_contract_url, RunSmartContract)
        self.textEdit_7.append(str(response))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Dialog = QtWidgets.QDialog()
    ui = Ui_Dialog()
    ui.setupUi(Dialog)
    Dialog.show()
    sys.exit(app.exec_())

