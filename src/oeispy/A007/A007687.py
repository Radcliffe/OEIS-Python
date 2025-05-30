# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A007687

from itertools import product
def colorings(n, zp):
    result = 0
    for f in product(range(n), repeat=zp):
        for j1 in range(zp):
            for j2 in range(zp):
                if (f[j1]+f[j2])%n == f[(j1+j2)%zp]:
                    break
            else:
                continue
            break
        else:
            result += 1
    return result
print([colorings(4, k) for k in range(1, 12)])
# _Andrey Zabolotskiy_, Jul 12 2017

