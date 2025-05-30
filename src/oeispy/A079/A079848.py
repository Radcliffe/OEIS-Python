# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A079848

from itertools import count, islice
from sympy import nextprime
def A079848_gen(): # generator of terms
    aset2, alist, k = set(), [], 0
    while (k:=nextprime(k)):
        bset2 = set()
        for a in alist:
            if (b:=k-a) in aset2:
                break
            bset2.add(b)
        else:
            yield k
            alist.append(k)
            aset2.update(bset2)
A079848_list = list(islice(A079848_gen(),30)) # _Chai Wah Wu_, Sep 11 2023

