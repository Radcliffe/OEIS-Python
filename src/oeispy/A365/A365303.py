# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A365303

def GreedyBh(h, seed, stopat):
    A = [set() for _ in range(h+1)]
    A[1] = set(seed)    # A[i] will hold the i-fold sumset
    for j in range(2,h+1): # {2,...,h}
        for x in A[1]:
            A[j].update([x+y for y in A[j-1]])
    w = max(A[1])+1
    while w <= stopat:
        wgood = True
        for k in range(1,h):
            if wgood:
                for j in range(k+1,h+1):
                    if wgood and (A[j].intersection([(j-k)*w + x for x in A[k]]) != set()):
                        wgood = False
        if wgood:
            A[1].add(w)
            for k in range(2,h+1): # update A[k]
                for j in range(1,k):
                    A[k].update([(k-j)*w + x for x in A[j]])
        w += 1
        return A[1]
GreedyBh(7,[0],10000)

