# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A384770

def row(n):
    i, J, out = 0, list(range(1, n+1)), []
    while len(J) > 1:
        i = (i + 3)%len(J)
        out.append(J.pop(i))
    out += [J[0]]
    return [out.index(j)+1 for j in list(range(1, n+1))]
print([e for n in range(1, 14) for e in row(n)])

