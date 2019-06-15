'''
Inplace reversal of singly linked list
'''

class Node:

    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self):
        self.head = None

    def reverse(self):
        previous = None
        current = self.head
        while current is not None:
            next = current.next
            current.next = previous
            previous = current
            current = next
        self.head = previous

    def push(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def print_list(self):
        current = self.head
        while current:
            print(current.data, '->', end=' ')
            current = current.next
        print('NULL')



llist = LinkedList()
llist.push(1)
llist.push(2)
llist.push(3)
llist.push(4)
print('Linked list:')
llist.print_list()

llist.reverse()

print('Reversed linked list:')
llist.print_list()
