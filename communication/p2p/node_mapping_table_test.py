# self node 부분에서 아이디를 새로 생성, ip 받아오기 등을 해서 self_node에 넣어줘야 한다.
# self_node = None, self.index = [], linked_node = [], state = []  index는 언제든 빼도 된다. list index search로 하여 간단하게 처리도 가능 하기 때문에.


class Table:
    count = 0

    def __init__(self):
        self.self_node = None
        self.index = []
        self.linked_node = []
        self.state = []

    def table_create(self, self_node):
        print('MAKE TABLE %s' % (self.self_node))
        self.self_node = self_node

    def table_add(self, linked_node, state):
        print('ADD TABLE %s' % (linked_node))
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
        print('Number of linked node %d' % (num))
        print('index    self_node   linked_node      state')
        for i in range(num):
            print('  %d           %s            %s          %s' % (
                self.index[i], self.self_node,  self.linked_node[i], self.state[i]))

# 만약 새로운 노드라면 ~, 아니고 기존 노드라면 ~ 이러한 정보를 text로 부터 읽고 판단 하여야 한다.


def test_mapping_table():
    mynode = Table()
    mynode.table_create("A")
    mynode.table_add("B", "Stable")
    mynode.table_add("C", "Stable")
    mynode.table_add("D", "Stable")
    mynode.table_add("E", "Stable")
    mynode.table_add("F", "Stable")
    mynode.print_table()

    mynode.table_update('B', "Comm error")
    mynode.table_update('D', "Comm error")
    mynode.table_update('D', "Dead")
    mynode.print_table()
    # 확인용
