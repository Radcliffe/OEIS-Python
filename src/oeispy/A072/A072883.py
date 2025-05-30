# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A072883

from sympy import isprime
def A072883(n):
    if is_A097792(n): return int(n==4)
    for k in range(1,99**9):
        if isprime(k**n+n): return k # _M. F. Hasler_, Jul 07 2024

