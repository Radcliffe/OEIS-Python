# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A346507

def aupto(lim): return sorted(set(a*b for a in range(11, lim//11+1, 10) for b in range(a, lim//a+1, 10)))
print(aupto(2761)) # _Michael S. Branicky_, Jul 22 2021

