# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A263865

from gmpy2 import is_prime
def ok(k): return k&1 and all(not is_prime(abs((1<<m)-k)) for m in range(k))
print([k for k in range(1, 7000, 2) if ok(k)]) # _Michael S. Branicky_, May 22 2025

