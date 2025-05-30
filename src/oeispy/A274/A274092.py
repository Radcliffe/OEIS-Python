# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A274092

from sympy import sin, sqrt, pi
def A274092(n):
    k, j = divmod(n,3)
    return int((k**2*sin(sqrt(k)+j*pi/2)).round()) # _Chai Wah Wu_, Jun 10 2016

