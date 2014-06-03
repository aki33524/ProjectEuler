from math import *
from string import *
from itertools import *
from bisect import *

def bitmasks(n):
    "is generator function which return bitmask"
    for i in range(1<<n):
        ret = []
        for j in range(n):
            ret.append(1 if (i&(1<<j)) else 0)
        yield ret[::-1]

def generate_primes(n):
    "generate prime list less than n"
    n += 1
    is_prime = [True]*n
    is_prime[0] = False
    is_prime[1] = False
    primes = []
    for i in range(2, n):
        if is_prime[i]:
            primes.append(i)
            for j in range(2*i, n, i):
                is_prime[j] = False
    return primes

def is_prime(n):
    """check if n is primenumber"""
    for i in range(2, int(n**0.5)+1):
        if n%i == 0:
            return False
    return True

def memoize(func):
    """decorator that chaches"""
    memoized_values = {}
    def wrapper(*args):
        nonlocal memoized_values
        key = args
        if key not in memoized_values:
            memoized_values[key] = func(*args)
        return memoized_values[key]
    return wrapper

class UnionFind():
    def __init__(self, n):
        self._i2g = [i for i in range(n)]
        self._g2i = [[i] for i in range(n)]
    
    def merge(self, ia, ib):
        ga = self._i2g[ia]
        gb = self._i2g[ib]
        if len(self._g2i[ga]) < len(self._g2i[gb]):
            ga, gb = gb, ga
        for v in self._g2i[gb]:
            self._i2g[v] = ga
        self._g2i[ga] += self._g2i[gb]
        self._g2i[gb] = []
        
    def is_same_group(self, ia, ib):
        return self._i2g[ia] == self._i2g[ib]
    
