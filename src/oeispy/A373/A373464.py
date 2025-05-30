# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A373464

from itertools import islice
from fractions import Fraction
from sympy import nextprime
def A373464_gen(): # generator of terms
    p, plist, pset = 1, [], set()
    while True:
        p = nextprime(p)
        for q in plist:
            r = Fraction(q+1,p+1)
            q2 = r*(q+1)-1
            if q2 < 2:
                break
            if q2.denominator == 1:
                q2 = int(q2)
                if q2 in pset:
                    q3 = r*(q2+1)-1
                    if q3 < 2:
                        break
                    if q3.denominator == 1 and int(q3) in pset:
                        yield p
        plist = [p]+plist
        pset.add(p)
A373464_list = list(islice(A373464_gen(),20)) # _Chai Wah Wu_, Jul 16 2024

