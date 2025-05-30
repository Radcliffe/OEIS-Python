# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A359437

from sympy import sqrt_mod_iter, nextprime, isprime
def A359437(n):
    p = 1
    while (p:=nextprime(p)):
        if len(set(filter(lambda x:isprime(p*(x+1)-x),((d**2+p)//(p+1) for d in sqrt_mod_iter(-p,p+1) if isprime(d)))) | set(filter(lambda x: isprime(p*(x-1)+x),((d**2-p)//(p-1) for d in sqrt_mod_iter(p,p-1) if isprime(d)))))==n:
            return p # _Chai Wah Wu_, May 06 2024

