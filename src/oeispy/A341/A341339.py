# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341339

import sympy
# k = 1,2,3,...
# n = 2,3,4,...
def a(k, n):
    a = 2**k
    while a > 0 and sympy.divisor_count(a) != n:
        a = a - 1
    return a

