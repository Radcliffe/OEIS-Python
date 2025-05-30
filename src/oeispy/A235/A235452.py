# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A235452

def A235452(n=100):
    a = set([])
    A235452 = {1: 1}
    for i in range(2, n):
        c = i
        a.add(c)
        while c != 1:
            if c % 2 == 1:
                c = 3 * c + 1
                a.add(c)
            c = c / 2
            a.add(c)
        k = 1
        while k in a:
            k += 1
        A235452[i] = k - 1
    return A235452
seq_map = A235452()
for n in range(1, len(seq_map) + 1):
    print(seq_map[n], end=", ")

