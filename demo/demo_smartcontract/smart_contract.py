

def generate_smartcontract(contract_title,contract_body,contract_args):

    smartContract = {"contract_title":None,"contract_body":None,"contract_args":None}

    smartContract["contract_title"] =contract_title
    smartContract["contract_body"] = contract_body
    smartContract["contract_args"] = contract_args
    return smartContract

'''
if __name__ == '__main__':
    sample=generate_smartcontract('1','2','3')
    print(sample)
'''