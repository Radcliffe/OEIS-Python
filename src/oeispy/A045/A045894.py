# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A045894

import math
def C(n,r):
    f=math.factorial
    return f(n)/f(r)/f(n-r)
def A045894(n):
    return (n+11)*4**(n+2)-(n+5)*C(2*(n+4),(n+4))/2 # _Indranil Ghosh_, Feb 18 2017

