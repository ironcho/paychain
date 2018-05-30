import os

from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

class NodeWidget (QWidget):
    def __init__ (self, parent = None):
        super(NodeWidget, self).__init__(parent)

        self.textQVBoxLayout = QVBoxLayout()
        self.textUpQLabel    = QLabel()
        self.textDownQLabel  = QLabel()

        font = self.textUpQLabel.font()
        font.setPointSize(12)
        self.textUpQLabel.setFont(font)

        self.textUpQLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.textUpQLabel.setAlignment(Qt.AlignCenter)

        self.textDownQLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.textDownQLabel.setAlignment(Qt.AlignCenter)

        self.textQVBoxLayout.addWidget(self.textUpQLabel)
        self.textQVBoxLayout.addWidget(self.textDownQLabel)

        self.allQHBoxLayout  = QVBoxLayout()

        self.iconQLabel = QLabel(self)
        self.iconQLabel.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        self.iconQLabel.resize(64, 64)
        self.iconQLabel.setAlignment(Qt.AlignCenter)

        self.allQHBoxLayout.addWidget(self.iconQLabel, 0)
        self.allQHBoxLayout.addLayout(self.textQVBoxLayout, 1)

        self.allQHBoxLayout.setSpacing(5)
        self.setLayout(self.allQHBoxLayout)

        # setStyleSheet
        self.textUpQLabel.setStyleSheet('''
            color: rgb(255, 255, 255);
        ''')
        self.textDownQLabel.setStyleSheet('''
            color: rgb(90, 90, 90);
        ''')

    def setTextUp (self, text):
        self.textUpQLabel.setText(text)

    def setTextDown (self, text):
        self.textDownQLabel.setText(text)

    def setIcon (self, imagePath):
        pixmap = QPixmap(imagePath)
        self.iconQLabel.setPixmap(pixmap)