import time

Transactions = None

Merkle_root = None


class Transaction(object):
    """
    Construct new transaction class

    """

    # def __init__(self, p_recv_addr, p_extra):
    def __init__(self, p_tx_type, p_sender_ip, p_extra):
        """

        :param p_recv_addr:
        :param p_extra:
        """
        self.type = p_tx_type
        self.sender_ip = p_sender_ip
        self.timestamp = time.strftime('%Y%m%d%H%M%S', time.localtime())
        self.tx_id = "B" + self.timestamp
        self.extra_data = p_extra
        # self.transaction_count = transaction_count
        # self.message = ''
        # self.pub_key = ''
        # self.signature = ''




# =====MODULE TEST=====
'''
if __name__ == '__main__':
    import json
    recv_addr = "1AVsffe"
    extra = 0x01
    tx = Transaction(recv_addr, extra)
    temp = json.dumps(tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)
    temps = json.loads(temp)

    print (temps, type(temps), type(temp))

'''
