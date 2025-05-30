# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376220

from itertools import count, islice
from math import gcd
from sympy import isprime
def A376220_gen(): # generator of terms
    c = 0
    for n in count(1):
        for l in count(1):
            if gcd(n,(m:=10**l)+1)==1:
                r = m//10
                a = m*(n+r)+r
                for k in range(r,m):
                    if isprime(a):
                        if k>c:
                            yield k
                            c = k
                        break
                    a += m+1
                else:
                    continue
                break
A376220_list = list(islice(A376220_gen(),22)) # _Chai Wah Wu_, Sep 19 2024

