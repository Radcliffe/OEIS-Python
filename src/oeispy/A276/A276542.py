# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A276542

from sympy import divisor_count
for n in range(1,20):
    if divisor_count(n*(n+1)/2)==divisor_count((n+1)*(n+2)/2):
        print(n, end=', ') # _Stefano Spezia_, Dec 06 2018

