# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A284318

for n in range(1, 51):
    print([i for i in range(1, n + 1) if n%i==0 and (i**n)%n==0]) # _Indranil Ghosh_, Mar 25 2017

