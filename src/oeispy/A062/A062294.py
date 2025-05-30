# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062294

from itertools import islice
from sympy import nextprime
def A062294_gen(): # generator of terms
    aset2, alist, k = set(), [], 0
    while (k:=nextprime(k)):
        bset2 = set()
        for a in alist:
            if (b:=a+k) in aset2:
                break
            bset2.add(b)
        else:
            yield k
            alist.append(k)
            aset2.update(bset2)
A062294_list = list(islice(A062294_gen(),30)) # _Chai Wah Wu_, Sep 11 2023

