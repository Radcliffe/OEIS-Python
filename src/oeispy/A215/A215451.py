# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A215451

s = a = 1
for n in range(1,333):
    print(a, end=', ')
    a = s % (a+n)
    s += a

