# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A354423

def a(n):
    R = dict()  # R[|s|-1][s] = reachable values using subset s
    for i in range(n+1): R[i] = dict()
    for i in range(1, n+1): R[0][(i,)] = {i}
    reach = set(range(1, n+1))
    for j in range(1, n):
        for i in range((j+1)//2):
            for s in R[i]:
                for t in R[j-1-i]:
                    if set(s) & set(t) == set():
                        u = tuple(sorted(set(s) | set(t)))
                        if u not in R[len(u)-1]:
                            R[len(u)-1][u] = set()
                        for a in R[i][s]:
                            for b in R[j-1-i][t]:
                                R[len(u)-1][u].update([a+b, a*b])
                                reach.update([a+b, a*b])
    k = n+1
    while k in reach: k += 1
    return k
print([a(n) for n in range(10)]) # _Michael S. Branicky_, May 30 2022

