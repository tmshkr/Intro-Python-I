"""
Determines the primality of a number provided as a command-line argument
Prints True if it is prime, False if it is not
"""

import sys


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True


if len(sys.argv) == 2:
    print(is_prime(int(sys.argv[1])))

"""
Sieve of Eratosthenes
Prints all primes from 2 to n
https://upload.wikimedia.org/wikipedia/commons/b/b9/Sieve_of_Eratosthenes_animation.gif
"""


def sieve(n):
    composites = []
    # start at 2, the first prime number
    for num in range(2, n + 1):
        # if num is not in the list of composites,
        # then it is prime
        if num not in composites:
            print(num)
            # add each multiple of the prime number,
            # starting at its square for optimization
            for multiple in range(num ** 2, n + 1, num):
                composites.append(multiple)


if len(sys.argv) == 1:
    sieve(120)
