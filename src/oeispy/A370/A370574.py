# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370574

from sympy import integer_nthroot
def A370574(n):
    if n <= 2: return -1
    k, n_2 = 1, n**2
    while True:
        if (integer_nthroot(n_2 ^ k**2, 2))[1] and k != n: return k
        k += 1 # _Karl-Heinz Hofmann_, Mar 03 2024

