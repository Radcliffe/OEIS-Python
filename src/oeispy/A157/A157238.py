# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A157238

x = [0]
while len(x) < 1000:
    t = x[-1]
    z = 1
    while 2 * z + 1 <= len(x):
        if x[-z:] == x[-(2 * z + 1) : -(z + 1)]:
            t = x[-(z + 1)]
        z += 1
    x.append(1 - t)
print(x)

