from math import *
from string import *
from itertools import *
from bisect import *

def bitmasks(n):
    "is generator function which return bitmask"
    for i in xrange(1<<n):
        ret = []
        for j in xrange(n):
            ret.append(1 if (i&(1<<j)) else 0)
        yield ret[::-1]

def generate_primes(n):
    "generate prime list less than n"
    is_prime = [True]*n
    primes = []
    for i in xrange(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, n, i):
                is_prime[j] = False
    return primes

def is_prime(n):
    for i in xrange(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True 