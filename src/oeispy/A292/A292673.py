# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A292673

def A292673(n, b=3): # change b for A292672, ..., A292679
    m, S, N = 0, {1}, range(1, n+1)
    g = [[0 for j in range(n+b)] for i in range(n+b)]
    row, col = {i:set() for i in N}, {j:set() for j in N}
    offsets = [(i, j) for i in range(-b+1, 1) for j in range(-b+1, 1)]
    offsets += [(i, j) for i in range(-b+1, 0) for j in range(1, b)]
    for i in N:
        for j in N:
            rect = set(g[i+o[0]][j+o[1]] for o in offsets)
            e = min(S - row[i] - col[j] - rect)
            g[i][j] = e
            if e > m:
                m = e
                S.add(m+1)
            row[i].add(e)
            col[j].add(e)
    return m
print([A292673(n) for n in range(1, 101)]) # _Michael S. Branicky_, Apr 13 2023

