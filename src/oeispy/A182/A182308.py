# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A182308

a=7
for i in range(55):
    print(a, end=',')
    a += a//7

