# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A356291

def A356291_list(size: int):
    F, R, C = 1, [0], [1] + [0] * (size - 1)
    for n in range(1, size):
        F *= n
        for k in range(n, 0, -1):
            C[k] = C[k - 1] * k
        C[0] = -sum(C[k] for k in range(1, n + 1))
        R.append(F + C[0])
    return R
print(A356291_list(23))
# The test predicate, not suitable for calculation:
def reducible(p) -> bool:
    return any(i for i in range(0, len(p))
        if all(p[j] < p[k]
                for j in range(0, i)
                    for k in range(i, len(p))
    ))
from itertools import permutations
for n in range(8): print(len([p for p in permutations(range(n)) if reducible(p)]))

