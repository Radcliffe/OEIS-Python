# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A285470

def a(n): s = str(n); return int(s[0] + "2" + s[1:])
print([a(n) for n in range(1, 68)]) # _Michael S. Branicky_, Dec 22 2021

