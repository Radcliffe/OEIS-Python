# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A215488

a = [1]*1000
for n in range(1,777):
    print a[n-1],
    a[n]= a[n-1] + a[2*n & n]

