# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A135257

from itertools import count, islice
from sympy import factorint
def A135257_gen(): # generator of terms
    aset2, alist = set(), []
    for k in count(0):
        if sum(factorint(k).values()) == 2:
            bset2 = set()
            for a in alist:
                if (b:=k-a) in aset2:
                    break
                bset2.add(b)
            else:
                yield k
                alist.append(k)
                aset2.update(bset2)
A135257_list = list(islice(A135257_gen(),30)) # _Chai Wah Wu_, Sep 11 2023

