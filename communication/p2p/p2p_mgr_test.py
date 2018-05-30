from peerproperty import nodeproperty
from communication.p2p import sender
from communication.p2p import receiver
from communication.p2p import node_mapping_table


class MainController(object):
    def __init__(self):
        return 0

    @staticmethod
    def command_line_interface():

        cmd = None

        while cmd != 'q':
            cmd = input('[t: send transaction, b: send block] > ')
            if cmd == 't':
                sender.sending_tx()

            if cmd == 'b':
                sender.sending_mining_block()


if __name__ == '__main__':
    node_mapping_table.initialize()
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.my_node.self_node, nodeproperty.My_receiver_port)
    recv_thread.start()

    MainController.command_line_interface()


def test_p2p_mgr():
    node_mapping_table.initialize()
    recv_thread = receiver.ReceiverThread(
        1, "RECEIVER", nodeproperty.my_node.self_node, nodeproperty.My_receiver_port)
    recv_thread.start()

    MainController.command_line_interface()
