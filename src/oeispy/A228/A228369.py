# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A228369

a = [[[]], [[1]]]
for s in range(2, 9):
    a.append([])
    for k in range(1, s+1):
        for ss in a[s-k]:
            a[-1].append([k]+ss)
print(a)
# _Andrey Zabolotskiy_, Jul 19 2017

