'''
This problem was asked by Google.

The area of a circle is defined as πr^2. Estimate π to 3 decimal places using a Monte Carlo method.

Hint: The basic equation of a circle is x2 + y2 = r2.
'''

import numpy as np     

# returns estimated value of pi
def pi(n):
    xs = 2.0 * np.random.rand(n, ) - 1.0
    ys = 2.0 * np.random.rand(n, ) - 1.0
    count = 0
    for x, y in zip(xs, ys):
        # if the point lies inside the circle
        if x**2 + y**2 <= 1:
            count += 1
    # area of circle / area of square = pi/4
    return float(4 * count/n)

    
n = 1000000
ans = round(pi(n), 3)
print(f'Monte-Carlo steps = {n}')
print(f'Estimated value of pi = {ans}')
    



