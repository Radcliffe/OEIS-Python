# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A352927

def sgn(n): return 1 if n >= 0 else -1
def afull(): return sorted(int("".join(map(str, range(i, j+sgn(j-i), sgn(j-i))))) for i in range(1, 10) for j in range(1, 10))
print(afull()) # _Michael S. Branicky_, May 01 2022

