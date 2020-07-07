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


sieve(120)
