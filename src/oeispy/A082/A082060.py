# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A082060

from sympy import totient
A082060_list = [n for n in range(1,10**4) if set(str(totient(n))) == set(str(n))] # _Chai Wah Wu_, Dec 13 2015

