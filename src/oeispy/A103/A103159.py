# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A103159

from math import gcd
def a(n): return gcd(int(str(n)[::-1]), int(str(n+1)[::-1]))
print([a(n) for n in range(1, 106)]) # _Michael S. Branicky_, Dec 12 2021

