import requests
import json
from demo.demo_savetx import transaction_generator

def post_transaction(url,tx):
    headers = {
        'content-type': "application/json",
        'cache-control': "no-cache",
    }
    url = url
    response = requests.request("POST",url, data=json.dumps(tx),headers=headers)
    return response
'''
if __name__ == "__main__":
    url = "http://192.168.0.45:5000/tx/save/"
    tx = transaction_generator.transaction_generator()
    #payload = "{ \"index\": 1,\"tx_title\": \"tx from gw\", \"tx_body\": \"fghdfgdf\"}"
    respone = post_transaction(url,tx)
    print(respone.text)
'''