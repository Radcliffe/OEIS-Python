# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A008549

import math
def C(n,r):
    f=math.factorial
    return f(n)/f(r)/f(n-r)
def A008549(n):
    return int((4**n)-C(2*n+1,n)) # _Indranil Ghosh_, Feb 18 2017

