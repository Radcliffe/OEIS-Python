# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A167629

from sympy import primerange, primepi
k_upto = 25327
A167629, primeset = set(), set(primelist:= list(primerange(3, int(k_upto**0.5)+1)))
for x in range (primepi(k_upto**(1/3))):
    limit, y = k_upto // (a:=primelist[x]), x
    while (b:= primelist[(y:=y+1)]) * (c1:=(a * b - 2)) <= limit:
        if c1 in primeset : A167629.add(a * b * c1)
        if (c2 := b * 2 - a) in primeset : A167629.add(a * b * c2)
    y -= 1
    while (b:= primelist[(y:=y+1)]) * (c2:=(b * 2 - a)) <= limit:
        if c2 in primeset : A167629.add(a * b * c2)
print(A167629:=sorted(A167629)) # _Karl-Heinz Hofmann_, Jan 30 2025

