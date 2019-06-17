'''
Sieve of Eratosthenes algorithm to find the primes below n
'''

# returns the list of prime numbers below n
def list_of_primes(n):
    sieve = [True for i in range(n+1)]
    sieve[0] = False
    sieve[1] = False
    # first prime
    p = 2
    while True:
        # setting prime * i = False
        for i in range(p, int(n/p)+1):
            sieve[i*p] = False

        # finding next prime p
        for j in range(p+1, n):
            if sieve[j] == True:
                p = j
                break

        # while loop break condition
        if p * 2 > n:
            break

    # selecting primes			
    primes = []
    for i in range(len(sieve)):
        if sieve[i] == True:
            primes.append(i)
    return primes


n = 1000
if __name__ == "__main__":
    primes = list_of_primes(n)
    print(f"Primes below {n} =\n{primes}.\n")
    print(f"Number of primes below {n} = {len(primes)}.")

