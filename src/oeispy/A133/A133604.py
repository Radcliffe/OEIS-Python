# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A133604

from itertools import count, islice
def A133604_gen(): # generator of terms
    aset2, alist = set(), []
    for k in count(1):
        bset2 = {r:=k<<1}
        if r not in aset2:
            for d in alist:
                if (m:=d+k) in aset2:
                    break
                bset2.add(m)
            else:
                if k in aset2:
                    yield k
                alist.append(k)
                aset2.update(bset2)
A133604_list = list(islice(A133604_gen(),30)) # _Chai Wah Wu_, Sep 11 2023

