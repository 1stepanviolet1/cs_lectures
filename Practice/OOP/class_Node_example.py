class Node():
    data = None
    prev = None
    next = None

    def __init__(self, data, prev = None, next = None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self): # data: <data_>, prev: <prev_>, next: <next_>
        data_ = self.data
        if self.prev is not None: # Без этого условия будет ошибка: AttributeError: 'NoneType' object has no attribute 'data'
            prev_ = self.prev.data
        else:
            prev_ = None
        if self.next is not None:
            next_ = self.next.data
        else:
            next_ = None
        return "data: {}, prev: {}, next: {}".format(data_, prev_, next_)


node_1 = Node(1)
print(node_1, end='\n\n') # data: 1, prev: None, next: None

node_2 = Node(2, node_1)
node_1.next = node_2 # доступ к полю экземпляра класса Node
print('node_1:', node_1, '\nnode_2:', node_2, end='\n\n') # у первого элемента next ссылается на второй, у второго prev - на первый элемент

node_3 = Node(3, node_2, node_1)
node_2.next = node_3
node_1.prev = node_3
print('node_1:', node_1, '\nnode_2:', node_2, '\nnode_3:', node_3, end='\n\n') # Получилось кольцо