# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A145522

from itertools import count
from sympy import integer_nthroot, isprime, primepi
def A145522(n):
    total = 0
    for p in count(2):
        if 2**p > A145521(n): break
        if isprime(p): total += primepi(integer_nthroot(A145521(n), p)[0])
    return total # _Jason Yuen_, Jan 31 2024

