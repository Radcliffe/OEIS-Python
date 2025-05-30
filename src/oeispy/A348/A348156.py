# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A348156

nn = 300
s = [True]*((nn)//3 + 1)
for i in range(4, nn, 3):
    if s[(i-1)//3]:
        for t in range(4, (nn)//i, 3):
            s[(i*t-1)//3] = False
print([3*i + 1 for i in range(1, (nn + 3)//3) if s[i]])

