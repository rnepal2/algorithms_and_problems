'''
Given k sorted singly linked lists, write a function to merge all the lists into 
one sorted singly linked list.
'''

# a single node
class Node:

	def __init__(self, data=None):
		self.data = data
		self.next = None

# prints a linked list
def print_llist(llist):
	while llist.next:
		print(llist.data, '->', end=' ')
		llist = llist.next
	print(f'{llist.data} -> NULL')

# merges two linked lists
def merge_llists(llist1, llist2):

	merged = None

	if llist1 == None:
		return llist2

	elif llist2 == None:
		return llist1

	# picking one and recurring
	if (llist1.data <= llist2.data):
		merged = llist1
		merged.next = merge_llists(llist1.next, llist2)
	else:
		merged = llist2
		merged.next = merge_llists(llist1, llist2.next)

	return merged 

# merged k linked lists passed as a list
def merge_kllists(llists):
	merged = None
	for l in llists:
		merged = merge_llists(merged, l)
	return merged

# merging k sorted linked lists

k = 3

# list of link lists
llist = [0] * k

llist[0] = Node(1)
llist[0].next = Node(3)
llist[0].next.next = Node(7)
llist[0].next.next.next = Node(13)

llist[1] = Node(2)
llist[1].next = Node(4)
llist[1].next.next = Node(6)
llist[1].next.next.next = Node(8)

llist[2] = Node(5)
llist[2].next = Node(11)
llist[2].next.next = Node(12)
llist[2].next.next.next = Node(14)

print(f'Linked lists to merge:')
for l in llist:
	print_llist(l)

print(f'Merged linked list:')
ans = merge_kllists(llist)
print_llist(ans)
