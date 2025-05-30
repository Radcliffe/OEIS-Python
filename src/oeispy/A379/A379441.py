# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379441

from sympy import factorint
from itertools import islice
from collections import Counter
fcache = dict()
def myfactors(n):
    global fcache
    if n in fcache: return fcache[n]
    ans = Counter({p:e for p, e in factorint(n).items()})
    fcache[n] = ans
    return ans
def agen(): # generator of terms
    yield 1
    an, a, m = 2, {1, 2}, 3
    while True:
        yield an
        k, fan = m-1, myfactors(an)
        sfan = set(fan)
        while True:
            k += 1
            if k in a: continue
            fk = myfactors(k)
            sfk = set(fk)
            if sfk & sfan and all(abs(fk[p]-fan[p])==1 for p in sfan):
                an = k
                break
        a.add(an)
print(list(islice(agen(), 88))) # _Michael S. Branicky_, May 25 2025

