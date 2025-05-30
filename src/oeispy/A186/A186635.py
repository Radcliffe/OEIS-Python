# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A186635

from sympy import isprime, n_order
is_A186635 = lambda n: isprime(n) and (n<7 or n_order(10, n)%2)
[n for n in range(1234) if is_A186635(n)] # _M. F. Hasler_, Nov 19 2024

