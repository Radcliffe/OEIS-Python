# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A078267

from math import gcd
def a(n): b = 10**len(str(n)); return b//gcd(n, b)
print([a(n) for n in range(1, 103)]) # _Michael S. Branicky_, Oct 05 2021

