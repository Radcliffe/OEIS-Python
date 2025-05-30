# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371670

from itertools import combinations_with_replacement
from sympy import prevprime
def A371670(n):
    p = n**4
    while (p:=prevprime(p)):
        pset = set(q:=tuple(pow(x,n,p) for x in range(p)))
        if not all(any((k-a[0]-a[1])%p in pset for a in combinations_with_replacement(q,2)) for k in range(p)):
            return p # _Chai Wah Wu_, Apr 04 2024

