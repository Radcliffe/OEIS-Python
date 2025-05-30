# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A287178

from itertools import count, islice
def A287178_gen(): # generator of terms
    aset1, aset2, alist, n = set(), set(), [], 0
    for k in count(1,2):
        bset2 = {k<<1}
        if (k<<1) not in aset2:
            for d in aset1:
                if (m:=d+k) in aset2:
                    break
                bset2.add(m)
            else:
                yield k-n
                n = k
                alist.append(k)
                aset1.add(k)
                aset2.update(bset2)
A287178_list = list(islice(A287178_gen(),41)) # _Chai Wah Wu_, Sep 05 2023

