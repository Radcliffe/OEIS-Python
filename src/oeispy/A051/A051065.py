# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A051065

TOP = 1000
a = [0]*TOP
for n in range(1, TOP):
    print(a[n-1], end=',')
    a[n] = (n + a[n//3]) % 2
# _Alex Ratushnyak_, Aug 17 2012

