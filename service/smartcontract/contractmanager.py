import pickle
import importlib
import os

CONTRACT_ADDR = "_ContractStorage"+os.sep
SOURCE_ADDR = "service"+os.sep+"smartcontract"+os.sep+"Sources"+os.sep
SOURCE_PACKAGE = "service.smartcontract.Sources."


class ContractManager:
    def deploy_contract(self, time_stamp, source, args, tx_id):
        contract_addr = "C"+time_stamp

        # 소스파일을 만들어주고
        f_contract = open(SOURCE_ADDR + contract_addr + ".py", 'w')
        f_contract.write(source)
        f_contract.close()

        # 그 모듈을 가져와서 클래스를 인스턴스화 해준다
        contract = getattr(importlib.import_module(SOURCE_PACKAGE + contract_addr), 'Contract')


        if args is None:
            instance = contract()
        elif args == '':
            instance = contract()
        else:
            if type(args) is list:
                instance = contract(*args)
            else:
                instance = contract(args)

        # 인스턴스화된 클래스를 직렬화해서 저장한 뒤 _ContractStorage에 저장한다
        f_contract = open(CONTRACT_ADDR + contract_addr, 'wb')
        pickle.dump(instance, f_contract)
        f_contract.close()

        # 주소 값 및 상태 값을 리턴해줌
        return {'tx_id': tx_id, 'contract_addr': contract_addr, 'state': "Deployed"}




    def execute_contract(self, contract_addr, function_name, args, tx_id):
        f_contract = open(CONTRACT_ADDR + contract_addr, 'rb')
        contract = pickle.load(f_contract)

        method = getattr(contract, function_name)

        # run method
        if args is None:
            result = method()
        elif args == '':
            result = method()
        else:
            if type(args) is list:
                result = method(*args)
            else:
                result = method(args)

        f_contract.close()

        # save state
        f_contract = open(CONTRACT_ADDR + contract_addr, 'wb')
        pickle.dump(contract, f_contract)
        f_contract.close()

        # load state
        f_contract = open(CONTRACT_ADDR + contract_addr, 'rb')
        state = f_contract.read()

        f_contract.close()

        return {'tx_id': tx_id, 'contract_addr': contract_addr, 'contract_function': function_name, 'result': result, 'state': "Executed"}
