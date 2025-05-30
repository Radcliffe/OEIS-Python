# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A336282

from itertools import permutations
def isHeapable(seq):
    sig = [0 for _ in range(len(seq))]
    sig[0] = 2
    for j in seq[1:]:
        sig[j] = 2
        while j > -1:
            j -= 1
            if sig[j] > 0:
                sig[j] -= 1
                break
        if j == -1:
            return False
    return True
def A336282(n):
    if n == 0: return 1
    x = permutations(range(n))
    return sum(1 for h in x if isHeapable(h))
print([A336282(n) for n in range(12)])

