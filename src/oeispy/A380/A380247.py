# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A380247

from num2words import num2words as n2w
def spell(n):
    return sum(1 for c in n2w(n).replace(" and", "").replace(" ", "").replace(chr(44), "").replace("-", ""))
def inverse_permutation(p):
    inv = [0] * len(p)
    for i, x in enumerate(p):
        inv[x-1] = i +1
    return inv
def nthRow(n):
    l = []
    for i in range(0,n):
        l.append(0)
    zp = 0
    for j in range(1,n+1):
        zc = 0
        while zc <= spell(j):
            if l[zp] == 0:
                zc += 1
            zp += 1
            zp = zp % n
        l[zp-1] = j
    return l
l = []
for i in range(1,15):
    l += inverse_permutation(nthRow(i))
print(l)

