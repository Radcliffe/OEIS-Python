# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A237882

for n in range(1000):
    b = bin(n).lstrip("0b")
    L0 = L1 = 0
    s = '0'
    if n==0: b=s
    while b.find(s)>=0:
        s += '0'
        L0 += 1
    s = '1'
    while b.find(s)>=0:
        s += '1'
        L1 += 1
    if L0>L1: print str(n)+',',

