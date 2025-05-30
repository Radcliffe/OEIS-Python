# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A033863

from itertools import count, islice
def agen(LIMIT):
    adict, n = dict(), 0
    for k in count(1):
        c, m = 0, k
        while c <= LIMIT and m != (s:=int("".join(sorted(str(m))))):
            m += s; c += 1
        if c not in adict:
            adict[c] = k
            while n in adict and n <= LIMIT: yield adict[n]; n += 1
            if n > LIMIT: return
print(list(agen(40))) # _Michael S. Branicky_, Jan 16 2024

