

def generate_runSmartContract(contract_addr,contract_function,contract_args):

    runSmartContract = {"contract_addr":None,"contract_function":None,"contract_args":None}

    runSmartContract["contract_addr"] =contract_addr
    runSmartContract["contract_function"] = contract_function
    runSmartContract["contract_args"] = contract_args
    return runSmartContract

'''
if __name__ == '__main__':
    sample=generate_smartcontract('1','2','3')
    print(sample)
'''