# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A274087

from sympy import sin
def A274087(n):
    return int((n**2*sin(n)).round()) # _Chai Wah Wu_, Jun 10 2016

