# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A381839

def a(n):
    b = bin(n)[2:]
    zl, zr = b.find('0'), b.rfind('0')
    return n if abs(zl-zr) < 2 else int(b[:zl+1]+"".join('0' if bi == '1' else '1' for bi in b[zl+1:zr])+b[zr:], 2)
print([a(n) for n in range(70)]) # _Michael S. Branicky_, Mar 09 2025

