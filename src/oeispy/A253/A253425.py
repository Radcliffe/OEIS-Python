# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A253425

from itertools import islice
from sympy import divisors
def A253425_gen(): # generator of terms
    bset, l, m, s = {1}, 0, 2, 3
    while True:
        for d in divisors(s):
            if d not in bset:
                bset.add(d)
                if m in bset:
                    yield l
                    l = 1
                    while m in bset:
                        m += 1
                else:
                    l += 1
                s += d
                break
A253425_list = list(islice(A253425_gen(),20)) # _Chai Wah Wu_, Jan 25 2022

