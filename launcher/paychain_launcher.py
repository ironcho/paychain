import logging
import sys
import json
import time
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from queue import Queue
from storage import file_controller
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.restapi_dispatch import save_tx_queue, contract_execution_queue
from communication.restapi_dispatch import contract_deploy_queue, query_block_queue
from communication.restapi_dispatch import infopage
from communication.peermgr import peerconnector
from service.blockmanager import genesisblock
from communication.msg_dispatch import dispatch_queue_list
from communication.msg_dispatch import t_type_queue_thread
from communication.msg_dispatch import b_type_queue_thread
from communication.msg_dispatch import v_type_queue_thread
from communication.p2p import receiver
from monitoring import monitoring
from storage import search
from storage import validation
import hashlib

app = Flask(__name__)

query_q = Queue()
savetx_q = Queue()


@app.route('/tx/save/', methods=['POST'])
def tx_save():
    monitoring.log('log.request(save tx) rcvd...')
    savetx_q.put((request.json, request.remote_addr))
    monitoring.log("log."+str(savetx_q))
    monitoring.log("log."+str(savetx_q.qsize()))
    time.sleep(5)
    block = file_controller.get_last_block_payup()
    hashvalue = hashlib.sha256(str(block["tx_list"]).encode('utf-8')).hexdigest()
    return jsonify({
        "status" : "pay_up transaction request complete",
        "block Id " : block['block_header']['block_id'],
        "hash_value": hashvalue
    })

@app.route('/block/search/', methods=['POST'])
def block_search():
    monitoring.log('log.search.tx')
    block_id = request.json["block_id"]
    block = search.search_block(block_id)
    return jsonify(block)

@app.route('/transaction/validation/', methods=['POST'])

def transaction_validation():
    monitoring.log('log.validation.tx')
    hash_value = request.json["hash_value"]
    block_id = request.json["block_id"]
    block = search.search_block(block_id)
    request_transaction, block_transaction, validation_value = validation.tx_validation(hash_value, block)
    return jsonify({
        "request_transaction": request_transaction,
        "block_transaction": block_transaction,
        "validation": validation
    })

@app.route('/info/tx/', methods=['GET'])
def get_txinfo():
    return jsonify(infopage.SavedTxList)

@app.route("/")
def hello():
    return "Pay chain  launcher for Generic Peer - REST API node"


def initialize_process_for_generic_peer():
    logging.basicConfig(stream=sys.stderr, level=logging.DEBUG)
    monitoring.log("log.Start Pay chain launcher for Generic Peer...")

    initialize()

    monitoring.log('log.Run processes for PeerConnector.')
    if not peerconnector.start_peerconnector():
        monitoring.log('log.Aborted because PeerConnector execution failed.')
        sys.exit(1)

    set_peer.set_my_peer_num()
    monitoring.log("log.My peer num: " + str(nodeproperty.My_peer_num))

    'Genesis Block Create'
    genesisblock.genesisblock_generate()

    monitoring.log("log.Start a thread to receive messages from other peers.")
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.My_receiver_port)
    recv_thread.start()
    monitoring.log("log.The thread for receiving messages from other peers has started.")


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

def initialize_process_for_RESTAPInode():
    queryqueue_thread = query_block_queue.QueryQueueThread(
        1, "QueryQueueThread", query_q
    )
    queryqueue_thread.start()
    logging.debug('QueryQueueThread started')

    savetxqueue_thread = save_tx_queue.RESTAPIReqSaveTxQueueThread(
        1, "RESTAPIReqSaveTxQueueThread", savetx_q
    )
    savetxqueue_thread.start()
    logging.debug('RESTAPIReqSaveTxQueueThread started')


# REST API Node launcher function
if __name__ == "__main__":
    logging.basicConfig(stream = sys.stderr, level = logging.DEBUG)
    initialize_process_for_generic_peer()
    initialize_process_for_RESTAPInode()
    app.run(host='0.0.0.0')
