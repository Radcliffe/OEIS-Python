# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A125577

a = 1
for n in range(1,77):
    print(a, end=',')
    a = n*n - a

