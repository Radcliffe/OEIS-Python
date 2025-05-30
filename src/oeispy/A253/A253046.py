# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A253046

from sympy import isprime, nextprime, prevprime
def A253046(n):
    q2, r2 = divmod(n,2)
    if not r2 and isprime(q2):
        return 3*nextprime(q2)
    else:
        q3, r3 = divmod(n,3)
        if not r3 and isprime(q3):
            return 2*prevprime(q3)
        return n # _Chai Wah Wu_, Dec 27 2014

