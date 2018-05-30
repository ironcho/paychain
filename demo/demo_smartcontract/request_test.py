import requests
import json


def deploy_smartContract(url,smartContract):
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }
    url = url
    print(url)
    response = requests.request("POST", url, data=json.dumps(smartContract), headers=headers)
    return response


def run_smartContract(url,runSmartContract):
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }
    url = url
    print(url)
    response = requests.request("POST", url, data=json.dumps(runSmartContract), headers=headers)
    return response

