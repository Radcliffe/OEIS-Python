# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A361417

def a(n):
    r=400
    for x in range(1, 400):
        for y in range(x+1,400):
            zz=x**3+n*x*y+y**3
            z=round(zz**(1/3))
            if zz==z**3 and z<r:
                r=z
    return(r)
print([a(n) for n in range(1, 31)])

