# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356757

from math import factorial
def a(n): return int(str(factorial(n)).replace("0", ""))
print([a(n) for n in range(27)]) # _Michael S. Branicky_, Aug 26 2022

