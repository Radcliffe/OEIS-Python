# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A052545

TOP = 33
a = [1]*TOP
a[2]=4
for n in range(3,TOP):
    print(a[n-3], end=',')
    a[n] = 3*a[n-1] - a[n-3]
# _Alex Ratushnyak_, Aug 10 2012

