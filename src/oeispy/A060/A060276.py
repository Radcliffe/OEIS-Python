# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A060276

from itertools import count, islice
from sympy import nextprime
def A060276_gen(): # generator of terms
    aset1, aset2, aset3, alist, k = set(), set(), set(), [], 2
    while True:
        bset2, bset3 = {k<<1}, {3*k}
        if 3*k not in aset3:
            for d in aset1:
                if (m:=d+(k<<1)) in aset3:
                    break
                bset2.add(d+k)
                bset3.add(m)
            else:
                for d in aset2:
                    if (m:=d+k) in aset3:
                        break
                    bset3.add(m)
                else:
                    yield k
                    alist.append(k)
                    aset1.add(k)
                    aset2.update(bset2)
                    aset3.update(bset3)
        k = nextprime(k)
A060276_list = list(islice(A060276_gen(),40)) # _Chai Wah Wu_, Sep 05 2023

