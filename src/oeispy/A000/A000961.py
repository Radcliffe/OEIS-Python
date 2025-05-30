# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000961

from sympy import primerange
def A000961_list(limit): # following Python style, list terms < limit
    L = [1]
    for p in primerange(1, limit):
        pe = p
        while pe < limit:
            L.append(pe)
            pe *= p
    return sorted(L) # _Chai Wah Wu_, Sep 08 2014, edited by _M. F. Hasler_, Jun 16 2022

