import socket

from peerproperty import nodeproperty
from communication.p2p import sender
from communication.p2p import receiver
import json


class MainController(object):
    def __init__(self):
        return 0

    @staticmethod
    def set_node():

        nodeproperty.My_IP_address = socket.gethostbyname(socket.gethostname())
        return True

    @staticmethod
    def command_line_interface():

        cmd = None

        while cmd != 'q':
            cmd = input('[t: send transaction, b: send block] > ')
            # 추후에 노드 관리를 하는 부분을 이용하여 매인 시나리오를 잘 돌릴수 있도록..nodeinfo.txt를 생성.
            if cmd == 't':
                # receiver, message가 결국 내용이다. '내가 누구에게 무슨 내용을 보낸다.' 라는 내용의 트랜잭션
                #receiver = raw_input('Receiver IP: ')
                #message = raw_input('Message: ')
                # 이미 만들어진 트랜잭션을 이용하여 전송. new_transaction.txt.로 저장이 되어있다면.
                #trx_jstr = TransactionCotroller.create_transaction(Property.pub_key, Property.pri_key, receiver, message)

                # new_transaction.txt open
                f = open("transaction_new0.txt", 'r')
                transaction = f.read()
                transactions = json.loads(transaction)

                sender.send_to_all(transaction)
                # print trx_jstr
                # Sender.send_to_all(trx_jstr)
                nodeproperty.tx_count += 1
                f.close()
            if cmd == 'b':
                f = open("block0.txt", 'r')
                block = f.read()

                sender.send_to_all(block)

           # elif cmd =='s': #이 커맨드가 새로 네트워크에 참여할때의 커맨드
           #  Sender.send('192.168.99.1','tttt',10654)


if __name__ == '__main__':
    MainController.set_node()
    print(nodeproperty.My_IP_address)
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.My_receiver_port)
    recv_thread.start()

    MainController.command_line_interface()


def test_receiver_sender():
    MainController.set_node()
    print(nodeproperty.My_IP_address)
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.My_IP_address, nodeproperty.My_receiver_port)
    recv_thread.start()

    MainController.command_line_interface()
