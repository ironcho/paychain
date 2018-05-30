import hashlib

def tx_validation(hash_value,block):

    block_transaction = hashlib.sha256(str(block["tx_list"]).encode('utf-8')).hexdigest()

    if hash_value == block_transaction:
        validation = "valid transaction"
    else:
        validation = "tampered transaction!!"
    return hash_value,block_transaction,validation