import time
import threading
import queue
import os
import logging

from PyQt5 import QtWidgets
from PyQt5 import uic
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QListWidgetItem

from monitoring.node_widget import NodeWidget

monitoring_queue = queue.Queue()

Main_form = None

def log(data):
    if Main_form==None:
        logging.debug(data)
    else:
        Main_form.add_queue_data(data)

def add_peer(title, subtitle, iconfilename):
    # Main_form.add_queue_data("log."+title + " peer is added.")
    if Main_form == None:
        logging.debug(title + "("+subtitle+") peer is added.")
    else:
        Main_form.add_node(title, subtitle, iconfilename)



class Form(QtWidgets.QDialog):
    def __init__(self, parent=None):
        QtWidgets.QDialog.__init__(self, parent)
        self.ui = uic.loadUi("monitoring" + os.sep + "monitoring.ui")

        self.ui.setWindowFlags(Qt.SplashScreen)                          # 윈도우 타이틀 없애기

        self.ui.listWidget_4.setSpacing(30)

        queue_thread = threading.Thread(target=self.read_queue)
        queue_thread.daemon = True
        queue_thread.start()

        self.ui.show()

    def add_node(self, title, subtitle, iconfilename):
        # Create QCustomQWidget
        myQCustomQWidget = NodeWidget()
        myQCustomQWidget.setTextUp(title)
        myQCustomQWidget.setTextDown(subtitle)
        myQCustomQWidget.setIcon(iconfilename)

        # Create QListWidgetItem
        myQListWidgetItem = QListWidgetItem(self.ui.listWidget_4)

        # Set size hint
        myQListWidgetItem.setSizeHint(myQCustomQWidget.sizeHint())

        # Add QListWidgetItem into QListWidget
        self.ui.listWidget_4.addItem(myQListWidgetItem)
        self.ui.listWidget_4.setItemWidget(myQListWidgetItem, myQCustomQWidget)

    def remove_node(self, index):
        self.ui.listWidget_4.removeItemWidget(self.ui.listWidget_4.takeItem(index))

    def change_status_text(self, message):
        self.ui.label_7.setText(""+message)

    def add_log_item(self,log):
        item = QListWidgetItem(log)
        self.ui.listWidget.addItem(item)

    def add_block_item(self,log):
        item = QListWidgetItem(log)
        self.ui.listWidget_3.addItem(item)

    def add_transaction_item(self,log):
        item = QListWidgetItem(log)
        self.ui.listWidget_2.addItem(item)

    def change_frame_color(self, r, g, b):
        stylesheet = "background-color: rgb({0}, {1}, {2})".format(r, g, b)
        widget_list = [self.ui.widget,self.ui.widget_2,self.ui.widget_3,self.ui.widget_4,self.ui.widget_5]
        
        for widget in widget_list:
            widget.setStyleSheet(stylesheet)
            # widget.setAutoFillBackground(True)
            # pt = widget.palette()
            # pt.setColor(widget.backgroundRole(),QColor(r,g,b))
            # widget.setPalette(pt)
            # print(p.name(), widget.autoFillBackground(), widget.updatesEnabled())

        # stylesheet = "background-color: rgb({0}, {1}, {2})".format(r,g,b)
        # print(stylesheet)
        # self.ui.widget.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_2.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_3.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_4.setStyleSheet(stylesheet)
        # print(stylesheet)
        # self.ui.widget_5.setStyleSheet(stylesheet)
        # print(stylesheet)

    def add_queue_data(self,data):
        monitoring_queue.put(data)

    def read_queue(self):
        time.sleep(1.5)
        while True:
            self.change_status_text('Server Status : NOMAL            ' + time.strftime('%H:' + '%M:' + '%S'))

            if monitoring_queue.qsize() > 0:
                datas = monitoring_queue.get()

                data = datas.split('.')

                if data[0] == 'log':
                    self.add_log_item(data[1])
                    self.change_frame_color(44, 132, 238)
                elif data[0] == 'block':
                    self.add_block_item(data[1])
                    self.change_frame_color(231,76,60)
                elif data[0] == 'transaction':
                    self.add_transaction_item(data[1])
                    self.change_frame_color(241, 196, 15)
                elif data[0] == 'add_peer':
                    # self.add_node(data[1], data[2], data[1]+".png")
                    self.add_node(data[1], data[2], "producer.png")
