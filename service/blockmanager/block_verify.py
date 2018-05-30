import json
from service.smartcontract import contractmanager
from communication.restapi_dispatch import infopage

def verify_tx_list(tx_list):
    contract_manager = contractmanager.ContractManager()
    for transaction in tx_list:
        data_jobj = json.loads(transaction)
        if data_jobj['type'] == 'CT':
            deployed_result = contract_manager.deploy_contract(
                data_jobj['timestamp'],
                data_jobj['extra_data']['contract_body'],
                data_jobj['extra_data']['contract_args'],
                data_jobj['tx_id']
            )
            infopage.addDeployedContract(data_jobj)
            infopage.addDeployedContractResult(deployed_result)
        elif data_jobj['type'] == 'RT':
            executed_result = contract_manager.execute_contract(
                data_jobj['extra_data']['contract_addr'],
                data_jobj['extra_data']['contract_function'],
                data_jobj['extra_data']['contract_args'],
                data_jobj['tx_id']
            )
            infopage.addExecutedContract(data_jobj)
            infopage.addExecutedContractResult(executed_result)
        elif data_jobj['type'] == 'T':
            infopage.addSavedTx(data_jobj)


        # data = json.dumps(transaction, indent=4, default=lambda o: o.__dict__, sort_keys=True)
        # if data['type'] == 'CT':
        #     contract_manager.deploy_contract(data['extra_data']['contract_body'], data['extra_data']['contract_args'])
        #
        # elif data['type'] == 'RT':
        #     contract_manager.execute_contract(data['extra_data']['contract_addr'], data['extra_data']['contract_function'], data['extra_data']['contract_args'])

#
# def verify(block):
#     contract_manager = contractmanager.ContractManager()
#     for transaction in block.tx_list:
#         data = json.dumps(transaction, indent=4, default=lambda o: o.__dict__, sort_keys=True)
#         if data['type'] == 'CT':
#             contract_manager.deploy_contract(data['extra_data']['contract_body'], data['extra_data']['contract_args'])
#
#         elif data['type'] == 'RT':
#             contract_manager.execute_contract(data['extra_data']['contract_addr'], data['extra_data']['contract_function'], data['extra_data']['contract_args'])