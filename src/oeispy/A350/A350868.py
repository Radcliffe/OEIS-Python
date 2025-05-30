# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350868

from sympy import prime, nextprime
def A350868(n):
    if n < 2:
        return 2+n
    qlist = [prime(i)-2 for i in range(2,n+2)]
    p = prime(n+1)
    mlist = [2*k**2 for k in range(1,n+1)]
    while True:
        if qlist == mlist:
            return p-mlist[-1]
        qlist = [q-qlist[0] for q in qlist[1:]]
        r = nextprime(p)
        qlist.append(r-p+qlist[-1])
        p = r # _Chai Wah Wu_, Jan 24 2022

