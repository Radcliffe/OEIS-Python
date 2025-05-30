# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A032789

from itertools import count, islice
def ispal(n): s = str(n); return s == s[::-1]
def agen():
    for k in count(0):
        q, r = divmod(k*(k+2), 3)
        if r == 0 and ispal(q):
            yield k, q
print([k for k, q in islice(agen(), 31)]) # _Michael S. Branicky_, Jan 24 2022

