# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A280876

from itertools import chain, count, islice
from sympy import isprime, primepi
def A280876_gen(): # generator of terms
    return filter(lambda n:isprime(n) and isprime(primepi(n)), chain.from_iterable(chain((int((s:=str(d))+s[-2::-1]) for d in range(10**l,10**(l+1))), (int((s:=str(d))+s[::-1]) for d in range(10**l,10**(l+1)))) for l in count(0)))
A280876_list = list(islice(A280876_gen(),20)) # _Chai Wah Wu_, Jun 23 2022

