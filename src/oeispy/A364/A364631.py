# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364631

from sympy.ntheory.factor_ import totient
from sympy import isprime, primefactors, prod
def psi(n):
    plist = primefactors(n)
    return n*prod(p+1 for p in plist)//prod(plist)
def a(n):
    i = 1
    r = n
    while (True):
        rc = totient(psi(r))
        if (rc == r):
            break;
        r = rc
        i += 1
    return i

