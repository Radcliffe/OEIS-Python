# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369099

from sympy import factorint,nextprime,primepi
def A369099(n):
    f = {A369099(primepi(p)):e for p,e in factorint(n).items()}
    a = p = 1
    for k in sorted(f,reverse=True):
        for i in range(f[k]):
            p = nextprime(p)
            a *= p**k
    return a

