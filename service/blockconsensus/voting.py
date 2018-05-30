import json
import time

import peerproperty.nodeproperty
from peerproperty import nodeproperty
from storage import file_controller
from communication.p2p import sender
from communication.peermgr import peermgr
from monitoring import monitoring

TransactionCountForConsensus = 1
MajorityCount = 0

def blind_voting(merkle_root):

    vote_number = (int(merkle_root, 16) % nodeproperty.Total_peer_num) + 1
    voting = {'To': vote_number,
              'from': nodeproperty.My_IP_address, 'type': 'V'}
    jsonString = json.dumps(voting)

    if nodeproperty.My_peer_num == vote_number:
        file_controller.add_voting(jsonString)
    else:
        index = vote_number - 1
        ip_address = peerproperty.nodeproperty.ConnectedPeerList[index][1]
        sender.send(ip_address, jsonString, nodeproperty.My_receiver_port)


def result_voting():

    list = file_controller.get_voting_list()
    voting_count = len(list)
    MajorityCount = nodeproperty.Total_peer_num / 2

    print("MajorityCount: "+ str(MajorityCount))
    print("My number of votes: "+ str(voting_count))

    if voting_count > MajorityCount :
        difficulty = 1
        monitoring.log("log.result voting : "+ str(voting_count))
        return difficulty
    else:
        difficulty = 0
        return difficulty
