import threading
import logging
import json
from queue import Queue
from socket import *
from communication.p2p import sender
from peerproperty import set_peer
from peerproperty import nodeproperty
import os
from monitoring import monitoring


with open(os.getcwd() + os.sep + "peermgr.json", 'r') as f:
    peermgr_config = json.load(f)

peermgr_ID = peermgr_config['PEER_MGR']['ID']
peermgr_IP = peermgr_config['PEER_MGR']['IP']
peermgr_Port = peermgr_config['PEER_MGR']['PORT']

# The peermgr configuration file(peermgr.json) contains only the ID list of peers.
# The IP list is not included.
Predefined_peer_list = peermgr_config['PEER_LIST']

# Since multiple PeerConnectors can attempt to connect to PeerMgr simultaneously,
# the request is processed asynchronously after enqueuing the request event
# to the queue connectedPeer_XXX queue.
connectedPeer_rcvddata_q = Queue()
connectedPeer_socket_q = Queue()
connectedPeer_IP_q = Queue()

# Add PeerMgr information to ConnectedPeerList by default.
nodeproperty.ConnectedPeerList = [[peermgr_ID, peermgr_IP]]
peerconnector_Port = peermgr_config['PEER_CONNECTOR_PORT']


def start_peermgr() -> bool:
    if nodeproperty.My_IP_address != peermgr_IP:
        monitoring.log('log.Only a node with a predefined IP can run PeerMgr.')
        return False

    monitoring.log(
        'log.Start listening thread to wait for connection of PeerConnector.')
    listening_to_peerconnector_thr = ListeningToPeerConnectorThread(
        1, "ListeningToPeerConnectorThread",
        peermgr_IP, peermgr_Port,
        connectedPeer_rcvddata_q, connectedPeer_socket_q, connectedPeer_IP_q
    )
    listening_to_peerconnector_thr.start()
    monitoring.log(
        'log.The listening thread is started to wait for the connection of PeerConnector.')

    monitoring.log('log.Start a thread to manage ConnectedPeerList.')
    managing_peertable_thr = ManagingConnectedPeerListThread(
        1, "ManagingConnectedPeerListThread",
        Predefined_peer_list,
        connectedPeer_rcvddata_q, connectedPeer_socket_q, connectedPeer_IP_q
    )
    managing_peertable_thr.start()
    monitoring.log(
        'log.The thread to manage the ConnectedPeerList has started.')

    return True


def getPeerIconfilename(peerid: str) -> str:
    if "producer" in peerid:
        return "producer"
    elif "package" in peerid:
        return "package"
    elif "delivery" in peerid:
        return "delivery"
    elif "seller" in peerid:
        return "seller"
    else:
        return "node"


class ListeningToPeerConnectorThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name,
                 p_ip, p_port,
                 p_connectedPeer_rcvddata_q, p_connectedPeer_socket_q, p_connectedPeer_IP_q):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.listening_ip = p_ip
        self.listening_port = p_port
        self.thrd_name = p_thrd_name
        self.rcvddata_q = p_connectedPeer_rcvddata_q
        self.socket_q = p_connectedPeer_socket_q
        self.socketip_q = p_connectedPeer_IP_q

    def run(self):
        addr = (self.listening_ip, self.listening_port)
        buf_size = 100
        tcp_socket = socket(AF_INET, SOCK_STREAM)
        tcp_socket.bind(addr)
        tcp_socket.listen(5)

        while True:
            monitoring.log('log.Wait for PeerConnector to connect.')
            request_sock, request_ip = tcp_socket.accept()
            monitoring.log('log.PeerConnector connected.')
            monitoring.log("log.PeerConnector IP: " + request_ip[0])

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
                logging.debug("rcvd_data: " + rcvd_data)
                if rcvd_data == "":
                    break
                try:
                    self.rcvddata_q.put(rcvd_data)
                    self.socket_q.put(request_sock)
                    self.socketip_q.put(request_ip[0])
                    break
                except Exception as e:
                    logging.debug(e)


class ManagingConnectedPeerListThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name,
                 p_peer_list,
                 p_connectedPeer_rcvddata_q, p_connectedPeer_socket_q, p_connectedPeer_IP_q):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.peer_list = p_peer_list
        self.rcvddata_q = p_connectedPeer_rcvddata_q
        self.socket_q = p_connectedPeer_socket_q
        self.socketip_q = p_connectedPeer_IP_q

    def run(self):
        while True:
            rcvd_data = self.rcvddata_q.get()
            request_sock = self.socket_q.get()
            socketip = self.socketip_q.get()

            # Assuming the format of the incoming message is json
            rcvd_data_json = json.loads(rcvd_data)
            peerid = rcvd_data_json['ID']
            monitoring.log("log.The ID of ConnectedPeer: " + peerid)
            monitoring.log("log.The IP of ConnectedPeer: " + socketip)

            if peerid in self.peer_list:
                monitoring.log("log.Add new peer's IP to ConnectedPeerList.")
                nodeproperty.ConnectedPeerList.append([peerid, socketip])
                nodeproperty.ConnectedPeerList.sort()
                request_sock.close()

                connected_peer_list_json = json.dumps(
                    nodeproperty.ConnectedPeerList, indent=4, default=lambda o: o.__dict__, sort_keys=True)
                monitoring.log(
                    "log.Updated ConnectedPeerList(json format): " + connected_peer_list_json)
                sender.send_to_all_peers_except_itself(
                    connected_peer_list_json, peerconnector_Port)

                set_peer.set_my_peer_num()
                set_peer.set_total_peer_num()

                monitoring.add_peer(
                    peerid, socketip, getPeerIconfilename(peerid))

            else:
                request_sock.close()
                # If there is no ID in the peer list, ignore it.
                monitoring.log(
                    "log.Ignore it because there is no corresponding ID in the predefined list.")


# TODO: We should update ConnectedPeerList by periodically executing ping.
