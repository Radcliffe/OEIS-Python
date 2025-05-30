# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375758

from itertools import count, islice
def agen(): # generator of terms
    aset, m = set(), 1
    for n in count(1):
        n1 = int(str(n)[0])
        an = next(k for k in count(m) if k not in aset and k%n1 == 0)
        yield an
        aset.add(an)
        while m in aset: m += 1
print(list(islice(agen(), 67))) # _Michael S. Branicky_, Jan 27 2025

