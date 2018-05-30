import requests

url = "http://192.168.0.45:5000/tx/save/"

payload = "{ \"index\": 1,\"tx_title\": \"tx from gw\", \"tx_body\": \"fghdfgdf\"}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "e5c5382c-999b-457a-76a2-01759e852420"
    }

print(type(payload))
response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)