import threading
import logging
from queue import Queue
import time
import json
from storage import file_controller
from service.blockconsensus import voting
from service.blockconsensus import block_generator
from service.blockconsensus import merkle_tree
from service.transactionmanager import transaction
from monitoring import monitoring

from queue import Queue


class VotingTypeQueueThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq

    def run(self):
        receive_event(self.thrd_name, self.inq)


def receive_event(p_thrd_name, p_inq):
    while True:
        monitoring.log("log.Waiting for V type msg")
        (recv_data,request_sock) = p_inq.get()
        # recv_data = p_inq.get()
        # request_sock = p_socketq.get()
        monitoring.log("log.V type msg rcvd: " + recv_data)

        file_controller.add_voting(recv_data)

        difficulty = voting.result_voting()

        if (difficulty > 0):
            monitoring.log("Enter block generator")
            block_generator.generate_block(
                difficulty, transaction.Merkle_root, transaction.Transactions)

        else:
            monitoring.log("log.")

        request_sock.close()
