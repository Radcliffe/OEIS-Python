# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A372060

def A372060(n):
    if n<3: return n
    l1, l2, s, b, k = 2, 1, 3, set(), 3
    while True:
        for i in count(s):
            if not (i in b or i & l1) and i & l2:
                if i == n: return k
                k += 1
                l2, l1 = l1, i
                b.add(i)
                while s in b:
                    b.remove(s)
                    s += 1
                break # _Chai Wah Wu_, May 02 2024

