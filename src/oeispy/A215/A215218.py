# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A215218

from math import isqrt
from sympy import primepi, primerange, integer_nthroot
def A215218(n): return int(sum(primepi(10**n//(k*m))-b for a,k in enumerate(primerange(integer_nthroot(10**n,3)[0]+1),1) for b,m in enumerate(primerange(k+1,isqrt(10**n//k)+1),a+1))) # _Chai Wah Wu_, Aug 26 2024

