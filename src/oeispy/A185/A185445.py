# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A185445

from math import isqrt, prod
from sympy import isprime, primepi, primerange, integer_nthroot, prime, divisors
def A185445(n):
    def mult_factors(n):
        if isprime(n):
            return [(n,)]
        c = []
        for d in divisors(n,generator=True):
            if 1<d<n:
                for a in mult_factors(n//d):
                    c.append(tuple(sorted((d,)+a)))
        return list(set(c))
    def f(x): return int(n+x-sum(primepi(x//(k*m))-b for a,k in enumerate(primerange(integer_nthroot(x,3)[0]+1)) for b,m in enumerate(primerange(k,isqrt(x//k)+1),a)))
    m, k = n, f(n)
    while m != k:
        m, k = k, f(k)
    return min((prod(prime(i)**(j-1) for i,j in enumerate(reversed(d),1)) for d in mult_factors(m)),default=1) # _Chai Wah Wu_, Aug 17 2024

