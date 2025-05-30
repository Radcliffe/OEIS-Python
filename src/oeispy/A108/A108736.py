# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A108736

from itertools import count, islice, product
def a(): # generator of terms
    S = ""
    for Sm in ("".join(w) for i in count(1) for w in product("01", repeat=i)):
        if Sm in S: continue
        for i in range(1, len(Sm)+1):
            v = Sm[-i:]
            t = "" if len(v) == len(Sm) else S[-len(Sm)+i:]
            if t+v == Sm: break
        S += v
        yield from list(map(int, v))
print(list(islice(a(), 105))) # _Michael S. Branicky_, Oct 27 2023

