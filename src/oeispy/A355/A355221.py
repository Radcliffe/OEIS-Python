# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A355221

def a(n):
    s, m = str(n), "9"
    return int("".join((m:=min(m, s[k])) for k in range(len(s))))
print([a(n) for n in range(68)]) # _Michael S. Branicky_, Jun 24 2022

