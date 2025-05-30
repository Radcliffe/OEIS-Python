# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341541

from sympy import prime, isprime
from math import sqrt, ceil
def neib(m):
    if m == 1: L = [4, 6, 8, 2]
    else:
        n = int(ceil((sqrt(m) + 1.0)/2.0))
        z1 = 4*n*n - 12*n + 10; z2 = 4*n*n - 10*n + 7; z3 = 4*n*n - 8*n + 5
        z4 = 4*n*n - 6*n + 3; z5 = 4*n*n - 4*n + 1
        if m == z1:             L = [m + 1, m - 1, m + 8*n - 9, m + 8*n - 7]
        elif m > z1 and m < z2: L = [m + 1, m - 8*n + 15, m - 1, m + 8*n - 7]
        elif m == z2:           L = [m + 8*n - 5, m + 1, m - 1, m + 8*n - 7]
        elif m > z2 and m < z3: L = [m + 8*n - 5, m + 1, m - 8*n + 13, m - 1]
        elif m == z3:           L = [m + 8*n - 5, m + 8*n - 3, m + 1, m - 1]
        elif m > z3 and m < z4: L = [m - 1, m + 8*n - 3, m + 1, m - 8*n + 11]
        elif m == z4:           L = [m - 1, m + 8*n - 3, m + 8*n - 1, m + 1]
        elif m > z4 and m < z5: L = [m - 8*n + 9, m - 1, m + 8*n - 1, m + 1]
        elif m == z5:           L = [m - 8*n + 9, m - 1, m + 8*n - 1, m + 1]
    return L
step_max = 20; L_last = [1]; L2 = L_last; L3 = [[1]]
for step in range(1, step_max + 1):
    L1 = []
    for j in range(0, len(L_last)):
        m = L_last[j]; k = 0
        while k <= 3 and isprime(m) == 0:
            m_k = neib(m)[k]
            if m_k not in L1 and m_k not in L2: L1.append(m_k)
            k += 1
    L2 += L1; L3.append(L1); L_last = L1
i = 1
while i:
    if isprime(neib(i)[0])*isprime(neib(i)[1])*isprime(neib(i)[2])*isprime(neib(i)[3]) == 1: print(-1)
    elif i not in L2: break
    for j in range(0, len(L3)):
        if i in L3[j]: print(j); break
    i += 1

