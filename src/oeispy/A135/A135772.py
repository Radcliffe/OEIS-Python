# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A135772

from sympy import divisor_count
def ok(n): return divisor_count(n) == n.bit_length()
print(list(filter(ok, range(1, 977)))) # _Michael S. Branicky_, Jul 29 2021

