# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A071604

from sympy import integer_log
def A071604(n):
    c = 0
    for i in range(integer_log(n,7)[0]+1):
        i7 = 7**i
        m = n//i7
        for j in range(integer_log(m,5)[0]+1):
            j5 = 5**j
            r = m//j5
            for k in range(integer_log(r,3)[0]+1):
                c += (r//3**k).bit_length()
    return c # _Chai Wah Wu_, Sep 16 2024

