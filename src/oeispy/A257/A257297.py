# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257297

def a(n): s = str(n); return 0 if len(s) < 2 else int(s[0])*int(s[1:])
print([a(n) for n in range(104)]) # _Michael S. Branicky_, Sep 01 2021

