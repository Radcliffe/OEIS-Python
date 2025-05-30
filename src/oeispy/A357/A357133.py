# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A357133

from itertools import islice
from sympy import isprime, nextprime
def agen():
    n, plst0 = 3, [2, 3, 5]
    while True:
        plst = plst0[:]
        while True:
            q, r = divmod(sum(plst), n)
            if r == 0 and isprime(q): yield q; break
            plst = plst[1:] + [nextprime(plst[-1])]
        plst0.append(nextprime(plst0[-1]))
        n += 1
print(list(islice(agen(), 60))) # _Michael S. Branicky_, Sep 14 2022

