# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357005

from math import gcd
def A357005(n):
    p=[int(d) for d in format(n,'b')]
    m=len(p)
    p0=min([p[(k*i+j)%m] for i in range(m)] for k in range(1,m+1) if gcd(k,m)==1 for j in range(m) if p[j])
    return sum(p0[i]*2**(m-1-i) for i in range(m))

