# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257587

def a(n): return sum(int(d)**2*(-1)**i for i, d in enumerate(str(n)))
print([a(n) for n in range(63)]) # _Michael S. Branicky_, Jul 11 2022

