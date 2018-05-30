# self node 부분에서 아이디를 새로 생성, ip 받아오기 등을 해서 self_node에 넣어줘야 한다.
# self_node = None, self.index = [], linked_node = [], state = []  index는 언제든 빼도 된다. list index search로 하여 간단하게 처리도 가능 하기 때문에.
import json
import socket
from peerproperty import nodeproperty
from storage import file_controller
from monitoring import monitoring

class Table:
    count = 0

    def __init__(self):
        self.self_node = None
        self.index = []
        self.linked_node = []
        self.state = []

    def table_create(self, self_node):
        self.self_node = self_node
        print('MAKE TABLE %s peer' % (self.self_node))
        print(" ")
        # self.self_node = self_node

    def table_add(self, linked_node, state):

        self.index.append(Table.count)
        self.linked_node.append(linked_node)
        self.state.append(state)
        Table.count += 1

    def table_update(self, linked_node, state):
        print('update table %s with %s' % (linked_node, state))
        ind = self.linked_node.index(linked_node)
        self.state[ind] = state

# 출력 확인용 -> 추후에 파일 입출력으로 변환 예정.
    def print_table(self):
        num = Table.count

        print("  ")
        print("==================================")
        # 여긴 로그로 보여주는 것이 아니라 노드 리스트에 목록을 추가해야함

        print('Number of linked node %d' % (num))

        print('index         self_node              linked_node             state')
        for i in range(num):
            print('  %d           %s            %s          %s' % (
                self.index[i] + 1, self.self_node,  self.linked_node[i], self.state[i]))

        print("  ")

    def write_table(self):
        nodeinfo = json.dumps(self, default=lambda o: o.__dict__)
        print(nodeinfo)
        f = open('nodeinfo.txt', 'w')
        f.write(nodeinfo)
        f.close()


def read_nodeinfo():
    f = open('nodeinfo.txt', 'r')
    info = f.read()
    nodeinfo = json.loads(info)
    return nodeinfo

# 만약 새로운 노드라면 ~, 아니고 기존 노드라면 ~ 이러한 정보를 text로 부터 읽고 판단 하여야 한다.
# 만약 최초 네트워크 참여가 아니라면, 블록 갯수, 트랜잭션의 갯수 동기화 작업을 한번씩 해줘야 한다. 최초 참여일 경우와 아닐 경우를 나눠서 해야함.
# 이니셜라이즈 와 싱크로나이즈 로 시나리오가 두개 존재 해야함.

# 동기화 : 기존에 네트워크 참여했던 경우
# 동기화 부분에서 블록, 트랜잭션 동기화를 위해 체크를 하는 부분 구현 해야함.


def synchronize():
    print("synchronize")
    info = read_nodeinfo()
    print(info)
    nodeproperty.my_node = Table()
    # ip 정보가 바뀔경우를 생각 해야함.
    nodeproperty.my_node.table_create(
        socket.gethostbyname(socket.gethostname()))
    for i in info['index']:
        nodeproperty.my_node.table_add(
            info['linked_node'][i], info['state'][i])

    nodeproperty.my_node.print_table()

# 초기화 : 최초에 네트워크 참여하는 경우


def initialize():
    nodeproperty.my_node = Table()

    # nodeproperty.my_node.table_create(
    #     socket.gethostbyname(socket.gethostname()))
    nodeproperty.my_node.table_create(
        nodeproperty.My_IP_address)

    # add 에서 txt를 읽어 최초로 connection 일어날수 있게. 적어도 하나 이상의 컴퓨터는 항상 켜져있는상태.
    # super node ip 정보는 파일로 부터 읽어 들이기.
    # f = open('supernode.txt','r')
    # supernode = f.read()

    nodeproperty.my_node.table_add(nodeproperty.My_IP_address, 'stable')

    nodeproperty.my_node.table_add("192.168.0.40", 'stable')
    nodeproperty.my_node.table_add("192.168.0.43", 'stable')
    nodeproperty.my_node.table_add("192.168.0.49", 'stable')
    nodeproperty.my_node.table_add("192.168.0.46", 'stable')
    # nodeproperty.my_node.table_add("163.239.200.182", 'stable')
    # nodeproperty.my_node.table_add("163.239.200.173", 'stable')
    # nodeproperty.my_node.table_add("163.239.200.174", 'stable')
    # nodeproperty.my_node.table_add("163.239.200.176", 'stable')
    # nodeproperty.my_node.table_add("163.239.200.179", 'stable')

    # Sender.sending_connection('192.168.0.96')
    # 요기부분이.
    nodeproperty.my_node.print_table()


def set_node():
    # nodeproperty.my_ip_address = socket.gethostbyname(
    #     socket.gethostname())
    # nodeinfo.txt 에 내용이 없다면 최초 참여(initialize), 있다면 동기화(synchronize)
    initialize()


''' nodeinfo.txt 파일을 노드마다 다르게 작성한 후에 테스트 필요
    try:
        f = open('nodeinfo.txt', 'r')
        tmp = f.read()
        f.close()
        if tmp == '':
            initialize()
        else:
            synchronize()

    except IOError as e:
        print("file open error - nodeinfo.txt", e)
        initialize()
'''

if __name__ == '__main__':
    nodeproperty.My_IP_address = file_controller.get_my_ip_rpi()
    set_node()
    # Property.my_node.write_table()
