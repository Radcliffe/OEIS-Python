# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A257501

import math
f=math.factorial
def C(n,r): return f(n)/f(r)/f(n-r)
i=1
for n in range(1,126):
    for k in range(1,n+1):
        print str(i)+" "+str(2*k*C(2*(n+k),n-k)/(n+k))
        i+=1 # _Indranil Ghosh_, Mar 04 2017

