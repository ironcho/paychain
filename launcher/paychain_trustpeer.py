import logging
import sys
import time
from PyQt5 import QtWidgets
from monitoring import monitoring
import threading
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import receiver
from service.blockmanager import genesisblock
from communication.msg_dispatch import dispatch_queue_list
from communication.msg_dispatch import t_type_queue_thread
from communication.msg_dispatch import b_type_queue_thread
from communication.msg_dispatch import v_type_queue_thread
from communication.peermgr import peermgr
from monitoring import monitoring


# Logchain launcher function for TrustPeer
# TrustPeer acts as a peer like ordinary nodes
# TrustPeer performs the role of PeerMgr in parallel.
def initialize_process_for_trust_peer():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    monitoring.log("log.Start Logchain launcher for TrustPeer...")

    # monitoring.add_peer('producer', 'producer a', 'producer.png')
    # monitoring.log('add_peer.producer.producer abc')
    monitoring.add_peer('package', 'sdfsdf', 'package.png')
    #
    # monitoring.add_peer('delivery', 'sadfsad', 'delivery.png')
    # monitoring.add_peer('delivery', 'sdfsdf', 'delivery.png')
    # monitoring.add_peer('seller', 'seller ff', 'seller.png')

    initialize()
    monitoring.log('log.Run threads for PeerMgr.')
    if not peermgr.start_peermgr():
        monitoring.log("log.Aborted because PeerMgr execution failed.")
        return

    set_peer.set_my_peer_num()
    monitoring.log("log.My peer num: " + str(nodeproperty.My_peer_num))

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    monitoring.log("log.Start a thread to receive messages from other peers.")

    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.My_receiver_port)
    recv_thread.start()
    monitoring.log(
        "log.The thread for receiving messages from other peers has started.")

    t_type_qt = t_type_queue_thread.TransactionTypeQueueThread(
        1, "TransactionTypeQueueThread",
        dispatch_queue_list.T_type_q
    )
    t_type_qt.start()

    v_type_qt = v_type_queue_thread.VotingTypeQueueThread(
        1, "VotingTypeQueueThread",
        dispatch_queue_list.V_type_q
    )
    v_type_qt.start()

    b_type_qt = b_type_queue_thread.BlockTypeQueueThread(
        1, "BlockTypeQueueThread",
        dispatch_queue_list.B_type_q
    )
    b_type_qt.start()


def initialize():
    monitoring.log('log.Start the blockchain initialization process...')
    file_controller.remove_all_transactions()
    file_controller.remove_all_blocks()
    file_controller.remove_all_voting()
    monitoring.log('log.Complete the blockchain initialization process...')
    set_peer.init_myIP()


def main(argv):
    if len(argv) != 1:
        arg_1 = argv[1]
        print("argument 1: " + arg_1)
        if arg_1 == "monitor":
            app = QtWidgets.QApplication(sys.argv)
            monitoring.Main_form = monitoring.Form()
            initialize_process_for_trust_peer()
            sys.exit(app.exec())
    else:
        initialize_process_for_trust_peer()


if __name__ == '__main__':
    # arg1: monitor -> Monitoring UI
    main(sys.argv)
