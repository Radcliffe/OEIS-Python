# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371440

from itertools import count, islice
def agen(): # generator of terms
    astr, k, mink = "01", 2, 1
    for i in count(0):
        if astr[-1] == "1": yield i
        for k in range(mink, len(astr)+1):
            if astr[1:].count(astr[:k]) == 0:
                break
        mink = max(mink, k)
        astr += astr[:k]
print(list(islice(agen(), 62))) # _Michael S. Branicky_, Mar 23 2024

