# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A188215

l = []
for i in range(17):
    b = bin(i)[2:]
    l.append(b)
    l.sort()
    print(l.index(b))

