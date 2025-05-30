# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348078

from sympy import factorint
def cond(n):
    evenodd = [0, 0]
    for e in factorint(n).values():
        evenodd[e%2] += 1
    return evenodd[0] == evenodd[1]
def afind(limit, startk=5):
    condvec = [cond(startk+i) for i in range(4)]
    for kp3 in range(startk+3, limit+4):
        condvec = condvec[1:] + [cond(kp3)]
        if all(condvec):
            print(kp3-3, end=", ")
afind(125*10**4) # _Michael S. Branicky_, Sep 27 2021

