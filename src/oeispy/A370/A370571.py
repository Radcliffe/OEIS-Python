# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370571

from itertools import count
def a(n): return next(d for k in count(1) if ("0" in (b:=bin(k)[2:])) and (d:=int(b))%n==0)
print([a(n) for n in range(1, 24)]) # _Michael S. Branicky_, Feb 22 2024

