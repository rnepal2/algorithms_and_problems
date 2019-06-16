'''
Prints the Pascal triangle of height h
'''

# returns n!
def factorial(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * factorial(n-1)


# prints the Pascal Triangle of height h
def triangle(h):
    # creating factorial memoization
    memo = []
    for i in range(h):
        memo.append(factorial(i))
    i = 0
    while i < h:
        if i == 0: space = h+1
        else: space -= 1
        print('  ' * space, end=' ')
        for j in range(i+1):
            # combinations: iCj
            nCr = int(memo[i] / (memo[i-j] * memo[j]))
            if i > 0 and j < i:
                print(nCr, end='   ')
            else:
                print(nCr, end='\n')
        i += 1


if __name__ == "__main__":
    triangle(10)

