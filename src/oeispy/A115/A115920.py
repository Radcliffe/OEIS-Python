# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A115920

from sympy import divisor_sigma
A115920_list = [n for n in range(1,10**4) if sorted(str(divisor_sigma(n))) == sorted(str(n))] # _Chai Wah Wu_, Dec 13 2015

