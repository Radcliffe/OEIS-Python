# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A258915

from gmpy2 import is_prime, digits
def a(n):
    if n < 3: return 0
    Rn = (10**n-1)//9
    return len(set(t for d in range(1, 10) for i in range(n if d in {1, 3, 7, 9} else 1) for c in set(range(-d, 10-d))-{0} if len(digits(t:=d*Rn+c*10**i))==n and is_prime(t)))
print([a(n) for n in range(1, 73)]) # _Michael S. Branicky_, Jun 28 2025

