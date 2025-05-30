# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A023142

from sympy import totient, n_order, divisors
def A023142(n):
    m = n>>(~n & n-1).bit_length()
    a, b = divmod(m,5)
    while not b:
        m = a
        a, b = divmod(m,5)
    return sum(totient(d)//n_order(10,d) for d in divisors(m,generator=True) if d>1)+1 # _Chai Wah Wu_, Apr 09 2024

