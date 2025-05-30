# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370959

from itertools import count, islice
def A370959_gen(): # generator of terms
    a, aset, b, c = 0, set(), 0, -1
    for n in count(1):
        aset.add(a)
        if a==b:
            if n-1>c:
                c = n-1
                yield a
            while b in aset:
                b += 1
        a = next(a for a in count(a%n,n) if a not in aset)
A370959_list = list(islice(A370959_gen(), 20)) # _Chai Wah Wu_, Mar 28 2024

