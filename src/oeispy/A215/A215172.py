# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A215172

a = 1
for n in range(1,13):
    print(a, end=', ')
    a = a*(4**n) + 2**n - 1

