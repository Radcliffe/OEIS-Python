# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A214588

from sympy import isprime
i=1
while i<=600:
    if  isprime(i)==True and (i%16)<8:
        print(i, end=", ")
    i+=1 # _Indranil Ghosh_, Jan 18 2017

