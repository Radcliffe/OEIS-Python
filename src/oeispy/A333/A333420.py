# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333420

from itertools import combinations, permutations
from sympy import factorial
def T(n,k): # T(n,k) for A333420
    if k == 1:
        return int(factorial(n))
    if n == 1:
        return k*(k+1)//2
    if k % 2 == 0 or (k >= n-1 and n % 2 == 1):
        return (k*(k*n+1)//2)**n
    if k >= n-1 and n % 2 == 0 and k % 2 == 1:
        return ((k**2*(k*n+1)**2-1)//4)**(n//2)
    nk = n*k
    nktuple = tuple(range(1,nk+1))
    nkset = set(nktuple)
    count = 0
    for firsttuple in combinations(nktuple,n):
        nexttupleset = nkset-set(firsttuple)
        for s in permutations(sorted(nexttupleset),nk-2*n):
            llist = sorted(nexttupleset-set(s),reverse=True)
            t = list(firsttuple)
            for i in range(0,k-2):
                itn = i*n
                for j in range(n):
                        t[j] += s[itn+j]
            t.sort()
            w = 1
            for i in range(n):
                w *= llist[i]+t[i]
            if w > count:
                count = w
    return count

