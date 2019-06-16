'''
There exists a staircase with N steps, and you can climb up either 1 or 2 steps at a time. 
Given N, write a function that returns the number of unique ways you can climb the staircase. 
The order of the steps matters.

For example, if N is 4, then there are 5 unique ways:
1, 1, 1, 1
2, 1, 1
1, 2, 1
1, 1, 2
2, 2

What if, instead of being able to climb 1 or 2 steps at a time, you could climb any number from a
set of positive integers X? For example, if X = {1, 3, 5}, you could climb 1, 3, or 5 steps at a time.
'''

import numpy as np


# recursive O(2^n)
def count_ways(n_steps):
    if n_steps == 0 or n_steps == 1:
        return 1
    else:
        return count_ways(n_steps-1) + count_ways(n_steps-2)
    

# O(n) time and space
def _count_ways(n_steps):

    count_steps = [0] * (n_steps+1)
    count_steps[0] = 1
    count_steps[1] = 1

    for i in range(2, n_steps+1):
        count_steps[i] += count_steps[i-1] + count_steps[i-2]

    return count_steps[n_steps]


#  O(n) time and O(1) space
def _count_ways_(n_steps):
    count_steps = np.empty(3, dtype=np.int) #[0] * 3
    count_steps[0] = 1; count_steps[1] = 1
    for _ in range(2, n_steps+1):
        count_steps[2] = count_steps[1] + count_steps[0]
        # swapping positions
        count_steps[0] = count_steps[1]
        count_steps[1] = count_steps[2]
    return count_steps[2]


# with step list: X
def total_ways(n_steps, X):
    if n_steps == 0:
        return 1
    else:
        return sum(_count_ways(n_steps-xi) for xi in X)

N = 10
ways = total_ways(n_steps=N, X=[1, 3, 5])
print('number of ways: ', ways)

