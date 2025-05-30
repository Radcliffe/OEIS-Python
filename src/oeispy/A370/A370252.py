# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370252

from itertools import count
from sympy import nextprime
def A370252(n):
    c, p = n, 2
    while p < n:
        if n%p:
            for m in count(2):
                if (p**m-1)//(p-1) > n:
                    break
                for r in count(1):
                    q = (p**(m*r)-1)//(p**r-1)
                    if q > n:
                        break
                    if not n % q:
                        c *= p
                        break
                else:
                    continue
                if q <= n:
                    break
        else:
            c *= p if p&1 or n%6 else p**2
        p = nextprime(p)
    return c # _Chai Wah Wu_, Mar 10 2024

