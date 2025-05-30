# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348076

from sympy import factorint
def aupto(limit):
    alst, cond = [], False
    for nxtk in range(3, limit+2):
        evenodd = [0, 0]
        for e in factorint(nxtk).values():
            evenodd[e%2] += 1
        nxtcond = (evenodd[0] == evenodd[1])
        if cond and nxtcond:
            alst.append(nxtk-1)
        cond = nxtcond
    return alst
print(aupto(2523)) # _Michael S. Branicky_, Sep 27 2021

