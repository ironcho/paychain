import logging
import platform

import peerproperty.nodeproperty
from peerproperty import nodeproperty
from storage import file_controller
from monitoring import monitoring


def init_myIP():
    monitoring.log("log.Set the peer's own IP address.")
    os = platform.system()
    if os == 'Linux':
        monitoring.log("log.Peer's os is Linux.")
        # For raspberry pi, we use wlan,
        # so we need to figure out the IP address in a different way.
        nodeproperty.My_IP_address = file_controller.get_my_ip_rpi()
    elif os == 'Windows':
        monitoring.log("log.Peer's os is Windows.")
        nodeproperty.My_IP_address = file_controller.get_my_ip()

        monitoring.log("log.Peer's IP: " + nodeproperty.My_IP_address)


# deprecated function
def set_peer():
    if nodeproperty.My_IP_address == None:
        init_myIP()
    if nodeproperty.My_IP_address == nodeproperty.Peer1:
        nodeproperty.My_peer_num = 1
    elif nodeproperty.My_IP_address == nodeproperty.Peer2:
        nodeproperty.My_peer_num = 2
    elif nodeproperty.My_IP_address == nodeproperty.Peer3:
        nodeproperty.My_peer_num = 3
    elif nodeproperty.My_IP_address == nodeproperty.Peer4:
        nodeproperty.My_peer_num = 4
    # elif nodeproperty.my_ip_address == nodeproperty.Peer5:
    #     nodeproperty.my_peer_num = 5
    # elif nodeproperty.my_ip_address == nodeproperty.Peer6:
    #     nodeproperty.my_peer_num = 6
    # elif nodeproperty.my_ip_address == nodeproperty.Peer7:
    #     nodeproperty.my_peer_num = 7
    # elif nodeproperty.my_ip_address == nodeproperty.Peer8:
    #     nodeproperty.my_peer_num = 8
    # elif nodeproperty.my_ip_address == nodeproperty.Peer9:
    #     nodeproperty.my_peer_num = 9
    else:
        nodeproperty.My_peer_num = "API_Peer"


def set_total_peer_num() -> int:
    nodeproperty.Total_peer_num = len(
        peerproperty.nodeproperty.ConnectedPeerList)
    monitoring.log("log.total peer num: " + str(nodeproperty.Total_peer_num))
    return nodeproperty.Total_peer_num


def set_my_peer_num() -> int:
    if nodeproperty.My_IP_address == None:
        init_myIP()
    p_num = 1
    for i in peerproperty.nodeproperty.ConnectedPeerList:
        if i[1] == nodeproperty.My_IP_address:
            nodeproperty.My_peer_num = p_num
        else:
            p_num = p_num + 1

    monitoring.log("log.my peer num: " + str(nodeproperty.My_peer_num))
    return nodeproperty.My_peer_num
