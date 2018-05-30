import sys

from PyQt5.QtWidgets import (QApplication, QComboBox, QDialog,
                             QDialogButtonBox, QFormLayout, QGridLayout, QGroupBox, QHBoxLayout,
                             QLabel, QLineEdit, QMenu, QMenuBar, QPushButton, QSpinBox, QTextEdit,
                             QVBoxLayout)

from PyQt5.QtCore import pyqtSlot


class Dialog(QDialog):
    NumGridRows = 3
    NumButtons = 4

    def __init__(self):
        super(Dialog, self).__init__()
        self.createFormGroupBox()

        buttonBox = QDialogButtonBox(
            QDialogButtonBox.Save | QDialogButtonBox.Cancel)

        buttonBox.accepted.connect(self.on_click)
        buttonBox.rejected.connect(self.reject)

        mainLayout = QVBoxLayout()
        mainLayout.addWidget(self.formGroupBox)
        mainLayout.addWidget(buttonBox)
        self.setLayout(mainLayout)

        self.setWindowTitle("Save agreement on sensor rule")

    def createFormGroupBox(self):
        self.formGroupBox = QGroupBox("Agreement")
        layout = QFormLayout()

        # Create textbox
        self.textboxRef = QLineEdit(self)
        self.textboxRule = QLineEdit(self)
        self.textboxPartyA = QLineEdit(self)
        self.textboxPartyB = QLineEdit(self)

        layout.addRow(QLabel("Ref Tx ID:"), self.textboxRef)
        layout.addRow(QLabel("Sensor rule:"), self.textboxRule)
        layout.addRow(QLabel("Party A:"), self.textboxPartyA)
        layout.addRow(QLabel("Party B:"), self.textboxPartyB)
        self.formGroupBox.setLayout(layout)

    @pyqtSlot()
    def on_click(self):
        print('PyQt5 button click')
        textValuePartyA = self.textboxPartyA.text()
        print('party A:' + textValuePartyA)
        textValuePartyB = self.textboxPartyB.text()
        print('party B:' + textValuePartyB)
        textValueRefID = self.textboxRef.text()
        print('Ref Tx ID:' + textValueRefID)
        textValueRule = self.textboxRule.text()
        print('Sensor rule:' + textValueRule)
        # logchain에게 Tx 저장 요청 전송
        # 저장된 Tx에 대한 ID(hash값) return


if __name__ == '__main__':
    app = QApplication(sys.argv)
    dialog = Dialog()
sys.exit(dialog.exec_())
