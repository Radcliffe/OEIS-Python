# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A268544

from num2words import num2words
def ok(n): return num2words(n).count('e') == 4
print([k for k in range(321) if ok(k)]) # _Michael S. Branicky_, Mar 25 2025

