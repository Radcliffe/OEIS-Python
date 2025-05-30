# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382381

from fractions import Fraction
from itertools import chain, combinations, count, islice
def powerset(s): # skipping empty set
    return chain.from_iterable(combinations(s, r) for r in range(1, len(s)+1))
def agen(): # generator of terms
    an, alst, vset = 1, [1], set()
    while True:
        yield an
        P = list(powerset(alst))
        Xlst, X2lst = [sum(s) for s in P], [sum(si**2 for si in s) for s in P]
        for k in count(an+1):
            ok, vnew = True, set()
            for i, s in enumerate(P):
                mu, X2 = Fraction(Xlst[i] + k, len(s)+1), X2lst[i] + k**2
                v = Fraction(X2, len(s)+1) - mu**2
                if v in vset or v in vnew:
                    ok = False
                    break
                else:
                    vnew.add(v)
            if ok:
                break
        an = k
        vset |= vnew
        alst.append(an)
print(list(islice(agen(), 13))) # _Michael S. Branicky_, Mar 31 2025

