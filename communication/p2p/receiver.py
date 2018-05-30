import threading
import json
import time
from socket import *
import logging
from peerproperty import nodeproperty
from storage import file_controller
from service.blockconsensus import merkle_tree
from service.blockconsensus import block_generator
from service.blockconsensus import voting
from queue import Queue
from communication.msg_dispatch import t_type_queue_thread
from communication.msg_dispatch import b_type_queue_thread
from communication.msg_dispatch import v_type_queue_thread

from communication.msg_dispatch import dispatch_queue_list
from monitoring import monitoring

Data_jobj = None


class ReceiverThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_ip, p_port):
        """

        :param p_thrd_id:
        :param p_thrd_name:
        :param p_ip:
        :param p_port:
        """
        threading.Thread.__init__(self)
        self.thrd_name = p_thrd_name
        self.thrd_id = p_thrd_id
        self.thrd_ip = p_ip
        self.thrd_port = p_port

    def run(self):
        receive_data(self.thrd_name, self.thrd_ip, self.thrd_port)


def receive_data(p_thrd_name, p_ip, p_port):
    """

    :param p_thrd_name:
    :param p_ip:
    :param p_port:
    :return:
    """
    # t_type_queue_thread.start()
    # print('msg-queue threads started')

    addr = (p_ip, p_port)
    buf_size = 100
    # to check my node info
    # print(p_thrd_name, p_ip, p_port)
    #
    tcp_socket = socket(AF_INET, SOCK_STREAM)
    tcp_socket.bind(addr)
    tcp_socket.listen(5)
    transaction_count = 0
    num_block = 0
    count = 1
    while True:
        monitoring.log("log.Waiting for connection...")
        request_sock, request_ip = tcp_socket.accept()

        # # Node Add
        # monitoring.add_peer('Node' + count, request_ip, 'node.png')
        # count = count + 1

        while True:
            rcvd_total = []
            while True:
                rcvd_pkt = request_sock.recv(buf_size)
                if not rcvd_pkt:
                    break
                rcvd_total.append(rcvd_pkt)

            temp = ""
            for i in rcvd_total:
                temp += i.decode('utf-8')

            recv_data = temp
            monitoring.log("log.Rcvd data: " + recv_data)

            if recv_data == "":
                break

            Data_jobj = json.loads(recv_data)

            try:
                if Data_jobj['type'] in ('T','CT', 'RT') :
                    dispatch_queue_list.T_type_q.put((recv_data,request_sock))
                    break
            except Exception as e:
                print(" ")


            try:
                if Data_jobj['type'] == 'V':
                    dispatch_queue_list.V_type_q.put((recv_data,request_sock))
                    monitoring.log("log." + "Voting received: " + recv_data)
                    break
            except Exception as e:
                print(" ")

            try:
                if Data_jobj['block_header']['type'] == 'B':
                    monitoring.log("log.Block received.")
                    # block verification thread
                    dispatch_queue_list.B_type_q.put((recv_data,request_sock))
                    break
            except Exception as e:
                print(recv_data)

            try:
                if Data_jobj['type'] == 'C':
                    file_controller.add_blockconfirm(recv_data)
                    request_sock.close()
                    break

            except Exception as e:
                print("Exception @receiver - data_jobj['type'] == 'C'", e)

            print("No data in socket")
            print(2)
            break

    # close - listening server
    tcp_socket.close()
