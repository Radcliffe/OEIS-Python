# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362566

x1, x2, y1, y2, ex, ey, a = 0, 1, 0, 0, 1, 0, [0]
for n in range(40):
    ex, ey = ex-ey, ey+ex
    x1r, x2r, y1r, y2r = y1+ex, y2+ex, -x2+ey, -x1+ey
    x1, x2, y1, y2 = min(x1, x1r), max(x2, x2r), min(y1, y1r), max(y2, y2r)
    a.append((x2-x1)*(y2-y1))
print(a) # _Andrey Zabolotskiy_, May 03 2023

