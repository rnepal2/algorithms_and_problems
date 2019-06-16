'''
Implementing stack data structure.
Using stack to reverse a string.
'''

class Node:

    def __init__(self, data=None):
        self.data = data
        self.next_node = None

class Stack:

    def __init__(self):
        self.top = Node()
        self.size = 0

    def is_empty(self):
        return self.top.data == None

    def peek(self):
        return self.top.data

    def push(self, data):
        new_node = Node(data=data)
        if self.top.data:
            new_node.next_node = self.top
        self.top = new_node
        self.size += 1

    def pop(self):
        if not self.top.data:
            return None
        value = self.top.data
        self.top = self.top.next_node
        self.size -= 1
        return value


stack = Stack()
print('stack isEmpty: ', stack.is_empty())
print('peek: ', stack.peek())
print('pop: ', stack.pop())

stack.push(10)
stack.push(20)
stack.push(30)
stack.push(40)

print('stack isEmpty: ', stack.is_empty())
print('stack size: ', stack.size)
print('peek: ', stack.peek())
print('pop: ', stack.pop())

print('stack isEmpty: ', stack.is_empty())
print('peek: ', stack.peek())



# function to reverse a string:
def reverse_string(string):
    to_list = [s for s in string]
    reverse = ''
    while len(to_list) > 0:
        reverse += to_list.pop()
    return reverse


string = 'Rabindra Nepal'
print(reverse_string(string))
