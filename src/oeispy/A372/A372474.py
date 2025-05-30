# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372474

from itertools import count
from sympy import isprime, primepi
from sympy.utilities.iterables import multiset_permutations
def A372474(n):
    for l in count(n):
        m = 1<<l
        for d in multiset_permutations('0'*n+'1'*(l-n)):
            k = m+int('0'+''.join(d),2)
            if isprime(k):
                return primepi(k) # _Chai Wah Wu_, May 13 2024

