# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A248753

from itertools import count, islice
def A248753_gen(startvalue=2): # generator of terms >= startvalue
    def f(n):
        y = 10*(x:=10**(len(str(n>>1))-1))
        return (c:=n-x)*x+int(str(c)[-2::-1] or 0) if n<x+y else (c:=n-y)*y+int(str(c)[::-1] or 0)
    for n in count(max(2,startvalue)):
        if str(n) in str(k:=f(n)):
            yield k
A248753_list = list(islice(A248753_gen(),32)) # _Chai Wah Wu_, Jul 24 2024

