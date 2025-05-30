# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A110772

from gmpy2 import is_prime
from itertools import count, islice
def agen(): # generator of terms
    an, s, aset, mink = 2, "2", {2}, 3
    while True:
        yield an
        an = next(k for k in count(mink, 2) if k not in aset and is_prime(int(s+str(k))))
        s += str(an)
        aset.add(an)
        while mink in aset: mink += 2
print(list(islice(agen(), 60))) # _Michael S. Branicky_, May 11 2023

