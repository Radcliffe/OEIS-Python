# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A330038

# Kevin Ryde's first formula
def a(n): return sum(bin(i).count("1") for i in range(n)) + n
print([a(n) for n in range(1, 61)]) # _Michael S. Branicky_, Dec 16 2021

