# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A329603

from math import prod
from itertools import accumulate
from collections import Counter
from sympy import prime, primepi, factorint
def A329603(n): return prod(prime(len(a)+1)**b for a, b in Counter(accumulate(bin(1+3*sum((1<<primepi(p)-1)<<i for i, p in enumerate(factorint(n,multiple=True))))[2:].split('1')[:0:-1])).items()) # _Chai Wah Wu_, Mar 11 2023

