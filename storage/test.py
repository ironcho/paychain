import os
import json
import hashlib
def read_all_line(file_name):

    f = open(file_name, 'r')
    line_list = []
    while True:
        line = f.readline()
        if not line:
            break
        else:
            line_list.append(line)
    f.close()
    return line_list


def search_block(block_id):
    block_storage_path = os.getcwd() + os.sep + '_BlockStorage' + os.sep

    for (path, dir, files) in os.walk(block_storage_path):
        block_list = files

    for i in block_list:
        search_block_tx_list = read_all_line(
            str(block_storage_path) + i)
        search_block = "\n".join(search_block_tx_list)
        a = json.loads(search_block)

        if block_id==a["block_header"]['block_id']:
            return a


if __name__ == '__main__':
    block=search_block("B20180525180916")
    a=hashlib.sha256(str(block["tx_list"]).encode('utf-8')).hexdigest()
    print(a)