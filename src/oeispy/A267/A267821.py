# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A267821

from sympy import isprime
A267821_list = [int(d,9) for d in (str(i**2) for i in range(1,10**6)) if max(d) < '9' and isprime(int(d,9))] # _Chai Wah Wu_, Feb 22 2016

