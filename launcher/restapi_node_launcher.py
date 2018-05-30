
import logging
import sys
from flask import Flask
from flask import jsonify
from flask import request
from flask import abort
from queue import Queue
from peerproperty import nodeproperty
from peerproperty import set_peer
from storage import file_controller
from communication.p2p import node_mapping_table
from communication.restapi_dispatch import query_block_queue, save_tx_queue

app = Flask(__name__)

query_q = Queue()
savetx_q = Queue()


rulelist = [
    {
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


def initialize_blockdbinfo():
    logging.info('Remove all transactions in mempool')
    file_controller.remove_all_transactions()
    file_controller.remove_all_blocks()
    logging.info('Remove all voting info ')
    file_controller.remove_all_voting()


def initialize_netinfo():
    nodeproperty.My_IP_address = file_controller.get_my_ip()
    set_peer.set_peer()
    # logging.info("my peer : " + nodeproperty.my_peer_num)

    # node_mapping_table.set_node()와 set_peer()는 중복 기능이나, 일단 디버깅용으로 중복으로 유지함
    node_mapping_table.set_node()


@app.route('/rules/', methods=['GET'])
def get_rules():
    logging.debug('request(query rulelist) rcvd...')
    query_q.put("rulelist")
    logging.debug(str(query_q))
    logging.debug(query_q.qsize())
    return jsonify({'rulelist': rulelist})


# @app.route('/rules/<int:rule_id>', methods=['GET'])
# def get_rule(rule_id):
#     logging.debug('request(query rule) rcvd...')
#     query_q.put("rule_id")
#     logging.debug(str(query_q))
#     logging.debug(query_q.qsize())
#     return jsonify({'rule': rule_id})


@app.route('/rules/', methods=['POST'])
def create_rule():
    logging.debug('request(create rule) rcvd...')
    savetx_q.put(request.json)
    logging.debug(str(savetx_q))
    logging.debug(savetx_q.qsize())

    if not request.json or not 'title' in request.json:
        abort(400)
    rule = {
        'index': rulelist[-1]['index'] + 1,
        'title': request.json['title'],
        'body': request.json.get('body', "")
    }
    rulelist.append(rule)

    return jsonify({'rule': rule}), 201


@app.route("/")
def hello():
    return "LogChain's REST API node"


# REST API Node launcher function
if __name__ == "__main__":
    logging.basicConfig(stream = sys.stderr, level = logging.DEBUG)
    initialize_blockdbinfo()
    initialize_netinfo()

    queryqueue_thread = query_block_queue.QueryQueueThread(
        1, "QueryQueueThread", query_q
    )
    queryqueue_thread.start()
    logging.debug('QueryQueueThread started')

    savetxqueue_thread = save_tx_queue.RESTAPIReqSaveTxQueueThread(
        1, "SaveTxQueueThread", savetx_q
    )
    savetxqueue_thread.start()
    logging.debug('SaveTxQueueThread started')

    app.run(host='0.0.0.0')
