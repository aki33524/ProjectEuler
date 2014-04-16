from utils import *
import hashlib

P = [None]*10
P[3] = [i*(i+1)/2 for i in range(45, 141)]
P[4] = [i**2 for i in range(32, 101)]
P[5] = [i*(3*i-1)/2 for i in range(26, 82)]
P[6] = [i*(2*i-1) for i in range(23, 71)]
P[7] = [i*(5*i-3)/2 for i in range(21, 64)]
P[8] = [i*(3*i-2) for i in range(19, 59)]

for elements in permutations([P[x] for x in range(3, 9)], 6):
    dp = [[[] for i in element] for element in elements]
    print dp 
    
    for i, e1 in enumerate(elements):
        e2 = elements[(i+1)%6]
        
        for j, u in enumerate(e1):
            for k, v in enumerate(e2):
                if u%100 == v/100:
                    dp[(i+1)%6][k].append()
                    
                
        pass
