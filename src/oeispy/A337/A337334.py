# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A337334

from sympy import primepi
a_last = 1
b_last = 1
for n in range(1, 1001):
    b = a_last + b_last
    a = primepi(b)
    print(a)
    a_last = a
    b_last = b

