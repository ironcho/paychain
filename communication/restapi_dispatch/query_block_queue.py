import threading
import logging
import time
from communication.restapi_dispatch import queue_strategy
from monitoring import monitoring

class QueryQueueThread(threading.Thread):
    def __init__(self, p_thrd_id, p_thrd_name, p_inq):
        threading.Thread.__init__(self)
        self.thrd_id = p_thrd_id
        self.thrd_name = p_thrd_name
        self.inq = p_inq

    def run(self):
        receive_event(self.thrd_name, self.inq)


def receive_event(p_thrd_name, p_inq):
    count = 1
    while True:
        monitoring.log("log.Waiting for event")
        (restapi_request_json, restapi_request_ip) = p_inq.get()

        # 어떤 노드에게 조회 요청을 보낸 후에, 해당 노드로부터 정보를 받은 후에 출력?
        # 또는 해당 노드에게 직접 접근해서 조회요청을 보내고, 정보를 받은 후에 출력
        # 낭종호 교수님 연구실에서 개발을 해야할 부분인듯한데...이는 1차년도 시연에서 제외하는 것이 맞는것인지 확인 필요 2017-09-27

        monitoring.log("log."+str(restapi_request_json))

        logging.debug(count)
        logging.debug(str(p_inq.qsize()))
        count = count + 1
        time.sleep(queue_strategy.QUERY_DEQUEUE_INTERVAL)
