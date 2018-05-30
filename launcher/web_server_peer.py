import threading
import time
import json
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from service.transactionmanager import transaction
from communication.p2p import receiver
from communication.p2p import sender
from communication.p2p import node_mapping_table


# restapi_node_launcher로 교체될 예정....
rulelist = [
    {
        'type' : 'T',
        'index': 1,
        'title': 'Testing-rule #1',
        'body': {
            "conditions": [
                []
            ],
            "actions": [
                [
                    {
                        "agent": "actuator",
                        "type": "led",
                        "method": {
                            "name": "LED 제어",
                            "id": "led",
                            "params": {
                                "command": {
                                    "cmd": "blink",
                                    "options": {
                                        "duration": 7000,
                                        "interval": 1500
                                    }
                                },
                                "notificationOption": "Failure",
                                "target": {
                                    "type": "gateway",
                                    "id": "b827ebda7b2a",
                                    "sensors": [
                                        "b827ebda7b2a-0-led"
                                    ]
                                }
                            }
                        }
                    }
                ]
            ],
            "severity": "information",
            "timezone": "+9.00",
            "name": "buttonLED700",
            "status": "activated",
            "trigger": {
                "agent": "sensorValue",
                "type": "onoff",
                "method": {
                    "name": "변경",
                    "id": "changed",
                    "params": {
                        "from": "0",
                        "to": "1",
                        "target": {
                            "type": "tag",
                            "id": "1",
                            "sensors": [
                                "b827ebda7b2a-0-button"
                            ]
                        }
                    }
                },
                "filter": {
                    "type": [
                        "series"
                    ],
                    "gateway": "*",
                    "sensor": [
                        "b827ebda7b2a-0-button"
                    ]
                }
            }
        }
    }
]

def main():
    'Remove all transaction in mempool'
    file_controller.remove_all_transactions()
    # file_controller.remove_all_Block()
    file_controller.remove_all_voting()

    print("Web Server Start")

    'Peer setting'
    nodeproperty.My_IP_address = file_controller.get_my_ip()
    set_peer.set_peer()
    print("my peer : " + nodeproperty.My_peer_num)

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()

    'Send to all node 10 transaction for one iteration'

    while True:
        transaction_count = 0
        # socket open

        while transaction_count < 30:
            # recv_addr = "1AVsffe"
            extra = "Coldchain service rule event"
            tx = transaction.Transaction(extra,transaction_count+1)
            temp = json.dumps(
                tx, indent=4, default=lambda o: o.__dict__, sort_keys=True)

            # send_to_all은 mapping table에 있는 정보로 broadcasting
            # send_to_all_node는 file_controller로 부터 IP List 가지고 와서 broadcasting
            # 테스트 후에 안전한 방식으로 선택
            sender.send_to_all(temp)
            #sender.send_to_all_node(temps, nodeproperty.my_ip_address, nodeproperty.port)

            transaction_count += 1

        'For block mining, time sleep'
        time.sleep(120)
        # socket close


if __name__ == '__main__':
    main()
