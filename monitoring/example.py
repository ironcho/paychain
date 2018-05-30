import sys, threading, time, queue
from PyQt5 import QtWidgets
from monitoring import Form

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)

    main_form = Form()

    main_form.change_status_text("Server Status : NOMAL            13:22:09")

    main_form.add_queue_data('block.Block1{add}')
    main_form.add_queue_data('block.Block2{add}')
    main_form.add_queue_data('block.Block3{add}')
 
    main_form.add_queue_data('transaction.tx1{node1->node2}')
    main_form.add_queue_data('transaction.tx2{node1->node2}')
    main_form.add_queue_data('transaction.tx3{node1->node2}')

    main_form.add_queue_data('log.start voting')
    main_form.add_queue_data('log.end voting')

    sys.exit(app.exec())
