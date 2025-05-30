# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A342545

from itertools import product
from functools import reduce
from sympy.utilities.iterables import multiset_permutations
from sympy import integer_nthroot
def A342545(n):
    for a in range(1,n):
        p, q = integer_nthroot(a*n**n,2)
        if q: return p
    l = 1
    while True:
        cmax = n**(l+n+1)
        for a in range(1,n):
            c = cmax
            for b in product(range(1,n),repeat=l):
                for d in multiset_permutations((0,)*n+b):
                    p, q = integer_nthroot(reduce(lambda c, y: c*n+y, [a]+d),2)
                    if q: c = min(c,p)
            if c < cmax:
                return c
        l += 1 # _Chai Wah Wu_, Apr 07 2021

