from utils import *
import hashlib

@memoize
def fib(n):
    return n if n==0 or n==1 else fib(n-1)+fib(n-2)

if __name__ == "__main__":
    print(fib(100))
