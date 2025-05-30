# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376584

from itertools import count, islice
from math import gcd
from sympy import isprime
def A376584_gen(): # generator of terms
    aset, a, b = {1,2}, 2, 3
    yield from (1,2)
    for i in count(3):
        c = b
        if isprime(a):
            while c in aset or gcd(c,a)>1:
                c+=1
        else:
            while c in aset or gcd(c,a)==1:
                c+=1
        aset.add(a:=c)
        if i == c:
            yield i
        while b in aset:
            b += 1
A376584_list = list(islice(A376584_gen(),20)) # _Chai Wah Wu_, Sep 30 2024

