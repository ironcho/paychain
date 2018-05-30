import random

def transaction_generator():
    tx= {"tx_title":None,"tx_body":None}

    temp =  round(random.uniform(0,35),2)
    humidity = random.randint(50,100)
    latitude = round(random.uniform(28,50),4)
    sensorValue  = {"temp":temp,"humidity": str(humidity)+"%","latitude":latitude,"Type": "led", "agent": "actuator", "duration": "7000"}

    tx["tx_body"] =sensorValue
    tx["tx_title"] = "tx from gateway node"
    return tx

'''
if __name__ == '__main__':
    transaction_generator()
'''