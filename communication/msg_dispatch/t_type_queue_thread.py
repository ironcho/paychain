import threading
import logging
from queue import Queue
import time
import json
from service.transactionmanager import transaction
from storage import file_controller
from service.blockconsensus import merkle_tree
from service.blockconsensus import voting
from monitoring import monitoring
from communication.peermgr import peerconnector


class TransactionTypeQueueThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq

    def run(self):
        receive_event(self.thrd_name, self.inq)

def receive_event(p_thrd_name, p_inq):
    transaction_count = 0
    while True:
        monitoring.log("log.Waiting for T type msg.")
        (recv_data,request_sock) = p_inq.get()
        # request_sock = p_socketq.get()

        # recv_data = p_inq.get()
        # request_sock = p_socketq.get()
        Data_jobj = json.loads(recv_data)
        monitoring.log("log.T type msg rcvd: " + recv_data)
        monitoring.log("log.T Type - " + Data_jobj['type'])
        transaction_count = transaction_count + 1

        file_controller.add_transaction(recv_data)
        monitoring.log("log.Transaction added to transaction pool: " + recv_data)

        if (transaction_count == voting.TransactionCountForConsensus) or (Data_jobj['type'] == 'CT') or (Data_jobj['type'] == 'RT'):
            # difficulty = 0

            transaction.Transactions = file_controller.get_transaction_list()
            print(transaction.Transactions)
            merkle = merkle_tree.MerkleTree()
            transaction.Merkle_root = merkle.get_merkle(
                transaction.Transactions)
            monitoring.log(
                "log.Transaction list Merkle _root: " + transaction.Merkle_root)

            monitoring.log("log.Start blind voting")
            voting.blind_voting(transaction.Merkle_root)
            monitoring.log("log.End voting")

            transaction_count = 0

        request_sock.close()
