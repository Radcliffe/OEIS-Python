# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A127827

from sympy import isprime
from itertools import count, islice, combinations_with_replacement as mc
def bgen(d):
    nd = ("".join(m) for m in mc("123456789", d))
    yield from filter(isprime, map(int, nd))
def ok(ndp):
    s = str(ndp)
    return len(set(s)) != 1 and isprime(int(s[::-1]))
def agen():
    yield from (next(filter(ok, bgen(d))) for d in count(2))
print(list(islice(agen(), 22))) # _Michael S. Branicky_, Jun 26 2022

