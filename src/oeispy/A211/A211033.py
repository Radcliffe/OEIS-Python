# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A211033

from __future__ import division
def A211033(n):
    x,y,z = n//3 + 1, (n-1)//3 + 1, (n-2)//3 + 1
    return x**4 + 4*x**3*y + 4*x**3*z + 4*x**2*y**2 + 8*x**2*y*z + 4*x**2*z**2 + y**4 + 6*y**2*z**2 + z**4 # _Chai Wah Wu_, Nov 28 2016

