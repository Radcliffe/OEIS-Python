# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350277

def A349325(n):
    prevc = c = n
    h = 1
    while c > 1:
        if c % 2:
            c = (3*c+1) // 2
            if prevc < n and c > n: h += 1
        else:
            c //= 2
            if prevc > n and c < n: h += 1
        prevc = c
    return h
rec, rec_idx = -1, []
for i in range(1, 10000):
    r = A349325(i)
    if r > rec:
        rec = r
        rec_idx.append(i)
print(rec_idx)

