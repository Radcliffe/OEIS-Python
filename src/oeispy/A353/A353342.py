# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353342

from itertools import count, islice, product
def agen(): # generator of terms
    for digits in count(1):
        for p in product("02468", repeat=digits):
            if len(p) > 1 and p[0] == "0": continue
            k = int("".join(p))
            if set(str(k**3)) <= set("02468"):
                yield k
print(list(islice(agen(), 40))) # _Michael S. Branicky_, May 06 2022

