# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A116430

from math import prod, isqrt
from sympy import primerange, integer_nthroot, primepi
def A116430(n):
    if n<=1: return 3*n+1
    def g(x,a,b,c,m): yield from (((d,) for d in enumerate(primerange(b,isqrt(x//c)+1),a)) if m==2 else (((a2,b2),)+d for a2,b2 in enumerate(primerange(b,integer_nthroot(x//c,m)[0]+1),a) for d in g(x,a2,b2,c*b2,m-1)))
    return int(sum(primepi(10**n//prod(c[1] for c in a))-a[-1][0] for a in g(10**n,0,1,1,n))) # _Chai Wah Wu_, Aug 23 2024

