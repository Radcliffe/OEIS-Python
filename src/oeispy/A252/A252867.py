# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A252867

A252867_list, l1, l2, s, b = [0,1,2], 2, 1, 3, set()
for _ in range(10**2):
    i = s
    while True:
        if not (i in b or i & l1) and i & l2:
            A252867_list.append(i)
            l2, l1 = l1, i
            b.add(i)
            while s in b:
                b.remove(s)
                s += 1
            break
        i += 1 # _Chai Wah Wu_, Dec 27 2014

