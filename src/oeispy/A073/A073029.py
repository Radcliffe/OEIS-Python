# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A073029

from num2words import num2words
def row(n): return [ord(c)-96 for c in num2words(n).replace(" and", "") if c.isalpha()]
print([e for n in range(17) for e in row(n)]) # _Michael S. Branicky_, Apr 22 2023

