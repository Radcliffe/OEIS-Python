# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A055412

from math import prod
from sympy import factorint
def A055412(n):
    c = 1
    for m in range(1,n**2+1):
        f = [(p,e,(0,1,0,-1)[p&3]) for p,e in factorint(m).items()]
        c += (prod((p**(e+1<<1)-a)//(p**2-a) for p, e, a in f)<<2)-prod(((k:=p**2*a)**(e+1)-1)//(k-1) for p, e, a in f)<<2
    return c # _Chai Wah Wu_, Jun 21 2024

