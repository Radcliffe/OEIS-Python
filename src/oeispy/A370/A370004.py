# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370004

from itertools import count
def a(n): return next(k for k in count(1) if str(k+n) in str(k*k))
print([a(n) for n in range(71)]) # _Michael S. Branicky_, Feb 07 2024

