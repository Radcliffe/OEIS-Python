# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A255855

from sympy import primefactors, resultant, nthroot_mod
from sympy.abc import x
def A255855(n):
    if n == 0: return 1
    k = 0
    for p in primefactors(resultant(x**n+5,(x+1)**n+5)):
        for d in (a for a in sorted(nthroot_mod(-5,n,p,all_roots=True)) if pow(a+1,n,p)==-5%p):
            k = min(d,k) if k else d
            break
    return int(k) # _Chai Wah Wu_, May 08 2024

