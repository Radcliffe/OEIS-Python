# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376157

from sympy.ntheory import factorint
c = 2
while c < 10000:
    charsum = 0
    for char in str(c):
        charsum += int(char)
    pf = factorint(c)
    cand = 0
    for p in pf.keys():
        cand += p
        cand += pf[p]
    if charsum == cand:
        print(c)
        print(pf)
    c += 1

