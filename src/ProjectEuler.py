from utils import *

@memoize
def fib(n):
    return n if n==0 or n==1 else fib(n-1)+fib(n-2)

if __name__ == "__main__":
    uf = UnionFind(10)
    uf.merge(1, 2)
    print(uf.is_same_group(1, 2))
    print(uf.is_same_group(2, 4))
