#precondition : Receiver is activated
import logging
from socket import *

import peerproperty.nodeproperty
from communication.p2p import node_mapping_table
from storage import file_controller

from peerproperty import nodeproperty
# port num이나 이런 것들은 추후에 계속 정해야 한다. 현재는 같은 네트워크 망 안에서 있을 때만 통신이 가능..
from communication.peermgr import peermgr

from monitoring import monitoring

import json


def sending_tx():
    # need make transaction call

    f = open("transaction_new0.txt", 'r')
    transaction = f.read()

    send_to_all(transaction)
    #Property.tx_count += 1
    f.close()


def sending_mining_block():
    # need make block call
    f = open("block0.txt", 'r')
    block = f.read()
    send_to_all(block)


def sending_connection(p_ip):
    msg = "new node"
    send(p_ip, msg, nodeproperty.My_receiver_port)


def send(p_ip, p_msg, p_port, *args):

    # if p_ip == nodeproperty.my_node.self_node:
    #     # print "Error"
    #     receiver_addr = (p_ip, p_port)
    #
    #     tcp_socket = socket(AF_INET, SOCK_STREAM)
    #
    #     try:
    #
    #         tcp_socket.connect(receiver_addr)
    #         tcp_socket.settimeout(5)
    #         tcp_socket.send(p_msg.encode('utf-8'))
    #
    #     except Exception as e:
    #         print(e)
    #
    #     tcp_socket.close()
    #
    # else:

    receiver_addr = (p_ip, p_port)
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    print("receiver addr =" + str(p_ip) + " , " + str(p_port))
    monitoring.log("log." + "receiver addr =" + str(p_ip) + " , " + str(p_port))

    print(" ")
    try:
        tcp_socket.connect(receiver_addr)
        print("connected........")
        monitoring.log("log." + "connected........")
        tcp_socket.settimeout(2)
        print(p_msg)
        monitoring.log("log." + p_msg)
        tcp_socket.send(p_msg.encode('utf-8'))
        monitoring.log("log.end send")
    except Exception as e:
        print(e)

    tcp_socket.close()

    monitoring.log("log.Sending complete")


def send_to_all(p_msg):
    # Property.my_node.print_table()

    for connected_node in nodeproperty.my_node.linked_node:
        send(connected_node, p_msg, nodeproperty.My_receiver_port)


# Send to all peers in ConnectedPeerList
def send_to_all_peers(p_msg, p_port):
    monitoring.log("log.Send to all peers in ConnectedPeerList")
    for peer in peerproperty.nodeproperty.ConnectedPeerList:
        try:
            send(peer[1], p_msg, p_port)
        except Exception as e:
            print(e)

        monitoring.log("log.ConnectedPeerList ID: " + peer[0])
        monitoring.log("log.ConnectedPeerList IP: " + peer[1])



# Send to all peers except yourself
def send_to_all_peers_except_itself(p_msg, p_port):
    monitoring.log("log.Send to all peers in ConnectedPeerList")
    for peer in peerproperty.nodeproperty.ConnectedPeerList:
        if peer[1] == peerproperty.nodeproperty.My_IP_address:
            monitoring.log("log.Do not send msg it to peer itself.")
        else:
            try:
                send(peer[1],p_msg, p_port)
            except Exception as e:
                print(e)

            monitoring.log("log.ConnectedPeerList ID: "+ peer[0])
            monitoring.log("log.ConnectedPeerList IP: " + peer[1])




def send_to_all_node(message, my_ip, my_port):

    address_list = file_controller.get_ip_list()
    for addr in address_list:
        try:
            send(addr, message, my_port)
        except Exception as e:
            print(e)

    monitoring.log("log." + "send block")
