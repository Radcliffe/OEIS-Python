# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A262571

def a(n): return int("".join(map(str, range(2, n+1))))
print([a(n) for n in range(2, 20)]) # _Michael S. Branicky_, Feb 23 2021

