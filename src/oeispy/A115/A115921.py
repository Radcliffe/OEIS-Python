# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A115921

from sympy import totient
A115921_list = [n for n in range(1,10**4) if sorted(str(totient(n))) == sorted(str(n))] # _Chai Wah Wu_, Dec 13 2015

