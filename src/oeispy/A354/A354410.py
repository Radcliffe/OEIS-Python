# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354410

# after linked PARI by _Rémy Sigrist_
base, vv, nb = 10, [0], 0
def visit(v, s, z, r):
    global base, vv, nb
    if v and s==z:
        nb += 1
        if nb > len(vv): vv.append(len(vv))
        vv[nb-1] = v
    if s-z-r <= 0 and s-z+(base-1)*r >= 0:
        if v: visit(base*v, s, z+1, r-1)
        for d in range(1, base): visit(base*v+d, s+d, z, r-1)
def auptod(digits): visit(0, 0, 0, digits); return sorted(set(vv))
print(auptod(6)) # _Michael S. Branicky_, May 26 2022

