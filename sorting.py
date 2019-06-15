'''
-Sorting: merge sort
-Binary search algorithm in a sorted list
'''

import random

# Sorting with merge sort
def merge_sort(_list):
	length = len(_list)
	if length > 1:
		left_part = _list[:int(length/2)]
		right_part = _list[int(length/2): length]
		
		merge_sort(left_part)
		merge_sort(right_part)
		
		i = 0; j = 0; k = 0
		while i < len(left_part) and j < len(right_part):
			if left_part[i] < right_part[j]:
				_list[k] = left_part[i]
				i += 1
			else:
				_list[k] = right_part[j]
				j += 1
			k += 1
			
		while i < len(left_part):
			_list[k] = left_part[i]
			i += 1
			k += 1
			
		while j < len(right_part):
			_list[k] = right_part[j]
			j += 1
			k += 1
	return _list
	
# Binary search algorith
def binary_search(n, sorted_list):
	''' returns the index of an element n of a sorted_list '''
	if len(sorted_list) < 1:
		print("No elements in the list.")
		return 
		
	begin = 0
	end = len(sorted_list)
	i = 1
	while True:
		mid = int((begin + end)/2)
		if sorted_list[mid] == n:
			break
		elif n > sorted_list[mid]:
			begin = mid
			end = end
		elif n < sorted_list[mid]:
			end = mid
			begin = begin
		i += 1
	#print("Number of times sliced: ", i)
	return mid#sorted_list[mid]


# Sorting	
_list = [random.randint(0, 100) for i in range(10)]
print(f"The original input list= {_list}")
merged = merge_sort(_list)
print(f"The sorted merged list = {merged}.")

# Searching
search = merged[4]
ans = binary_search(search, merged)
print(f"The index of {search} in the sorted list = {ans}")