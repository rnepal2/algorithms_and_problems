'''
Implementing a doubly liked list
Append and prepend methods
'''

# single node: an element of linked list
class Node:
    def __init__(self, data=None):
        self.data = data
        self.prev = None
        self.next = None


# doubly linked list 
class LinkedList:
    def __init__(self, head, tail):
        self.head = head
        self.tail = tail
        self.head.next = self.tail
        self.tail.prev = self.head

    def append(self, node):
        # if head is None
        if self.head.data is None: 
            node.prev = Node(data=None)
            self.head = node
            self.tail = Node(data=None)
            return

        # travel to last node
        last = self.head
        while last.next:
            last = last.next
        last.next = node
        node.prev = last

    def prepend(self, node):
        # if head is none
        if self.head.data is None:
            node.next = self.head
            node.prev = Node(data=None)
            self.head = node
            self.tail = Node(data=None)
            return 

        node.next = self.head
        node.prev = Node(data=None)
        if self.head.data is not None:
            self.head.prev = node
        self.head = node

    # print the current doubly liked list
    def print_ls(self):
        node = self.head
        while node:
            self.print_node(node)
            node = node.next

    # print single node
    def print_node(self, node):
        if node.prev and node.next:
            print(node.prev.data, '<-', node.data, '->', node.next.data)
        if not node.next:
            print(node.prev.data, '<-', node.data, '->', None)


ls = LinkedList(Node(data=None), Node(data=None))

# append and prepend
ls.append(Node(1))
ls.append(Node(2))
ls.prepend(Node(3))
ls.append(Node(4))
ls.append(Node(5))
ls.prepend(Node(6))
ls.append(Node(7))

# print the linked list
ls.print_ls()




