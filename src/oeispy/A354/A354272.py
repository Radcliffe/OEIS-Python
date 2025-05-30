# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354272

from itertools import product
def mult_pol(s1, s2):
    res = [0]*(len(s1)+len(s2)-1)
    for o1,i1 in enumerate(s1):
        for o2,i2 in enumerate(s2):
            res[o1+o2] += i1*i2
    return res
out = []
for d in range(0, 5):
    startp = [1,]
    for i in product((1,-1),repeat = d):
        startp = mult_pol(startp, list(i)+[1,])
    out.extend(startp)
print(out)

