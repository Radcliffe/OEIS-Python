# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352462

def ok(n): s = str(n); return s.endswith(str(sum(map(int, s))))
print([k for k in range(1, 4517) if ok(k)]) # _Michael S. Branicky_, Mar 17 2022

