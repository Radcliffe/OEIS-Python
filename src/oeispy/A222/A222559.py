# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A222559

a=0
for n in range(1,33):
    print(a, end=',')
    if n&1:
        a *= n
    else:
        a += n

