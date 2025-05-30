# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A318682

from sympy import factorint
def A318682(n):
    a_n = 0
    for i in range(1, n+1):
        a_n += (-1)**(sum(p*e for p, e in factorint(i).items())+1)
    return a_n

