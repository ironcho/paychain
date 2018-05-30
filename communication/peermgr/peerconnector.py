import os
import threading
import logging
import json
from socket import *
from queue import Queue
from peerproperty import nodeproperty
from communication.p2p import sender
from peerproperty import set_peer
from monitoring import monitoring

with open(os.getcwd() + os.sep + 'peerconnector.json', 'r') as f:
    peerconnector_config = json.load(f)

# TODO: There are several PeerMgr candidates, of which PeerMgr succeeded first in PeerMgr process execution becomes final PeerMgr. If the PeerMgr node fails to run, the other candidate nodes attempt to run PeerMgr process.
peermgr_ID = peerconnector_config['PEER_MGR_LIST'][0]['ID']
peermgr_IP = peerconnector_config['PEER_MGR_LIST'][0]['IP']
peermgr_Port = peerconnector_config['PEER_MGR_LIST'][0]['PORT']

peerconnector_ID = peerconnector_config['PEER_CONNECTOR']['ID']
peerconnector_Port = peerconnector_config['PEER_CONNECTOR']['PORT']

# Because PeerMgr can send ConnectedPeerList in a short time interval,
# the request is processed asynchronously after enqueuing the request event
# to the queue connectedPeerMgr_XXX queue.
connectedPeerMgr_rcvddata_q = Queue()
connectedPeerMgr_socket_q = Queue()


# Add PeerMgr information to ConnectedPeerList by default.
nodeproperty.ConnectedPeerList = [[peermgr_ID, peermgr_IP]]


def connect_to_peermgr():
    monitoring.log('log.Start a thread to connect to PeerMgr.')
    # TODO: If there is no response after pinging PeerMgr, attempt to connect to another PeerMgr.
    # Returns False if all attempts to connect to the PeerMgr fail.

    connecting_to_peermgr_thr = ConnectingToPeerMgrThread(
        1, "ConnectingToPeerMgrThread",
        peermgr_IP, peermgr_Port
    )
    connecting_to_peermgr_thr.start()
    monitoring.log('log.The thread to connect to PeerMgr has started.')


def start_peerconnector() -> bool:
    connect_to_peermgr()

    monitoring.log(
        'log.Start listening thread to wait for connection of PeerMgr.')
    listening_to_peerconnector_thr = ListeningToPeerMgrThread(
        1, "ListeningToPeerMgrThread",
        nodeproperty.My_IP_address, peerconnector_Port,
        connectedPeerMgr_rcvddata_q, connectedPeerMgr_socket_q
    )
    listening_to_peerconnector_thr.start()
    monitoring.log(
        'log.The listening thread is started to wait for the connection of PeerMgr.')

    monitoring.log('log.Start a thread to update ConnectedPeerList.')
    updating_peertable_thr = UpdatingConnectedPeerListThread(
        1, "UpdatingConnectedPeerListThread",
        connectedPeerMgr_rcvddata_q, connectedPeerMgr_socket_q
    )
    updating_peertable_thr.start()
    monitoring.log(
        'log.The thread has started to update ConnectedPeerList that the peer has internally.')

    return True


class ConnectingToPeerMgrThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name,
                 p_ip, p_port):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.peermgr_ip = p_ip
        self.peermgr_port = p_port

    def run(self):
        join_msg = {'ID': peerconnector_ID}
        join_msg_json = json.dumps(join_msg)
        monitoring.log("log.Msg to connect to PeerMGr: " + join_msg_json)
        sender.send(self.peermgr_ip, join_msg_json, self.peermgr_port)
        monitoring.log('log.An connection message was sent to PeerMgr.')


class ListeningToPeerMgrThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name,
                 p_peerconnector_IP, p_peerconnector_Port,
                 p_connectedPeerMgr_rcvddata_q, p_connectedPeerMgr_socket_q):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.listening_ip = p_peerconnector_IP
        self.listening_port = p_peerconnector_Port
        self.rcvddata_q = p_connectedPeerMgr_rcvddata_q
        self.socket_q = p_connectedPeerMgr_socket_q

    def run(self):
        addr = (self.listening_ip, self.listening_port)
        buf_size = 100

        tcp_socket = socket(AF_INET, SOCK_STREAM)
        tcp_socket.bind(addr)
        tcp_socket.listen(5)
        while True:
            monitoring.log('log.Wait for PeerMgr to connect.')
            request_sock, request_ip = tcp_socket.accept()
            monitoring.log('log.PeerMgr connected.')

            while True:
                rcvd_total = []
                while True:
                    # Assuming the format of the incoming message is json
                    rcvd_pkt = request_sock.recv(buf_size)
                    if not rcvd_pkt:
                        break
                    rcvd_total.append(rcvd_pkt)
                rcvd_data = ""
                for i in rcvd_total:
                    rcvd_data += i.decode('utf-8')
                    monitoring.log("log.rcvd_data: " + rcvd_data)
                if rcvd_data == "":
                    break
                try:
                    self.rcvddata_q.put(rcvd_data)
                    self.socket_q.put(request_sock)
                    break
                except Exception as e:
                    logging.debug(e)


class UpdatingConnectedPeerListThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name,
                 p_connectedPeerMgr_rcvddata_q, p_connectedPeerMgr_socket_q):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.rcvddata_q = p_connectedPeerMgr_rcvddata_q
        self.socket_q = p_connectedPeerMgr_socket_q

    def run(self):
        while True:
            rcvd_data = self.rcvddata_q.get()
            request_sock = self.socket_q.get()

            # Assuming the format of the incoming message is json
            rcvd_list = json.loads(rcvd_data)

            monitoring.log("log.Received ConnectedPeerList: " + rcvd_data)

            request_sock.close()

            nodeproperty.ConnectedPeerList = rcvd_list
            set_peer.set_my_peer_num()
            set_peer.set_total_peer_num()
