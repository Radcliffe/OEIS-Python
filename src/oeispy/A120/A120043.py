# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A120043

from math import isqrt, prod
from sympy import primerange, integer_nthroot, primepi
def A120043(n):
    def g(x,a,b,c,m): yield from (((d,) for d in enumerate(primerange(b,isqrt(x//c)+1),a)) if m==2 else (((a2,b2),)+d for a2,b2 in enumerate(primerange(b,integer_nthroot(x//c,m)[0]+1),a) for d in g(x,a2,b2,c*b2,m-1)))
    def almostprimepi(n,k): return int(sum(primepi(n//prod(c[1] for c in a))-a[-1][0] for a in g(n,0,1,1,k)) if k>1 else primepi(n))
    return -almostprimepi(m:=1<<n,12)+almostprimepi(m<<1,12) # _Chai Wah Wu_, Aug 31 2024

