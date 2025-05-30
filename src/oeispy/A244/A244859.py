# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A244859

def a(n):
    if n == 0: return 0
    moddict = {0: 0}
    for e in range(1, n+2):
        repe = (10**e-1)//9
        r = repe%n
        if r in moddict:
            return repe - moddict[r]
        else:
            moddict[r] = repe
print([a(n) for n in range(29)]) # _Michael S. Branicky_, Feb 22 2024

