# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A333312

for m in range(3, 1000):
    anz = 0
    for i in range(m // 2 + 1, m):
        l = (2 * i * i - 2 * i - m * (m - 1)) / (2 * (m - 2 * i))
        if l - int(l) == 0 and l >= 0:
            anz = anz + 1
    if anz > 1:
        print(m)

