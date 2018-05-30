

# http://host:5000/info/tx/
SavedTxList = []

# http://host:5000/info/contract/deployed/
DeployedSmartContractList = []

# http://host:5000/info/contract/deployed/result/
DeployedSmartContractResultList = []


# http://host:5000/info/contract/executed/
ExecutedSmartContractList = []

# http://host:5000/info/contract/executed/result/
ExecutedSmartContractResultList = []



def addSavedTx(transaction):
    # saved_tx = {
    #     'tx_id': transaction.tx_id,
    #     'tx_from_ip': transaction.sender_ip,
    #     'tx_body': transaction.extra_data
    # }
    SavedTxList.append(transaction)





def addDeployedContract(deployed_contract):
    # deployed_cont = {
    #     'tx_id': deployed_contract.tx_id,
    #     'tx_from_ip': deployed_contract.sender_ip,
    #     'tx_body': deployed_contract.extra_data
    # }
    DeployedSmartContractList.append(deployed_contract)

def addDeployedContractResult(deployed_contract_result):
    DeployedSmartContractResultList.append(deployed_contract_result)




def addExecutedContract(executed_contract):
    # deployed_cont = {
    #     'tx_id': executed_contract.tx_id,
    #     'tx_from_ip': executed_contract.sender_ip,
    #     'tx_body': executed_contract.extra_data
    # }
    ExecutedSmartContractList.append(executed_contract)

def addExecutedContractResult(executed_contract_result):
    ExecutedSmartContractResultList.append(executed_contract_result)


