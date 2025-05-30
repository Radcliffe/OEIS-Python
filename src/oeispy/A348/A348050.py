# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348050

from sympy import factorint
from itertools import product
def palsthru(maxdigits):
    midrange = [[""], [str(i) for i in range(10)]]
    for digits in range(1, maxdigits+1):
        for p in product("0123456789", repeat=digits//2):
            left = "".join(p)
            if len(left) and left[0] == '0': continue
            for middle in midrange[digits%2]:
                yield int(left+middle+left[::-1])
def afind(maxdigits):
    record = -1
    for p in palsthru(maxdigits):
        f = factorint(p, multiple=True)
        if p > 0 and len(f) > record:
            record = len(f)
            print(p, end=", ")
afind(10) # _Michael S. Branicky_, Oct 25 2021

