# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A324054

from math import prod
from itertools import accumulate
from collections import Counter
from sympy import prime
def A324054(n): return prod(((p:=prime(len(a)+1))**(b+1)-1)//(p-1) for a, b in Counter(accumulate(bin(n)[2:].split('1')[:0:-1])).items()) # _Chai Wah Wu_, Mar 10 2023

