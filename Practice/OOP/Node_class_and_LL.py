class Node:
    def __init__(self, inf):
        self.inf = inf
        self.next_ = None
    def __str__(self):
        return 'data: {}'.format(self.inf)
    def set_next_(self, next_):
        self.next_ = next_
class LinkedList:
    def __init__(self, head_data, tail_data):
        self.head = Node(head_data)
        self.tail = Node(tail_data)
        self.head.set_next_(self.tail)
LL = LinkedList('1', '2')
tmp = LL.head
while tmp != None:
    print(tmp)
    tmp = tmp.next_
