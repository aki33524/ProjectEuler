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
    is_prime = [True]*n
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
    import functools
    @functools.wraps(func)
    def wrapper(*args):
        func._memoized_values = getattr(func, '_memoized_values', {})
        key = (func,args)
        if key not in func._memoized_values:
            func._memoized_values[key] = func(*args)
        return func._memoized_values[key]
    return wrapper