# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A062140

import math
f=math.factorial
def C(n,r):
    return f(n)//f(r)//f(n-r)
i=0
for n in range(26):
    for m in range(n+1):
        print(i, (-1)**m*f(n)*C(n+4,n-m)//f(m))
        i+=1 # _Indranil Ghosh_, Feb 23 2017

