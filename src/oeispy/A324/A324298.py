# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A324298

def aupto(lim): return sorted(set(a*b//10 for a in range(6, 10*lim//6+2, 10) for b in range(a, 10*lim//a+2, 10) if a*b//10 <= lim))
print(aupto(249)) # _Michael S. Branicky_, Aug 21 2021

