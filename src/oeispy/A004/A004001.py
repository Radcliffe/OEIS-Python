# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A004001

def a004001(n):
    A = {1: 1, 2: 1}
    c = 1 #counter
    while n not in A.keys():
        if c not in A.keys():
            A[c] = A[A[c-1]] + A[c-A[c-1]]
        c += 1
    return A[n]
# _Edward Minnix III_, Nov 02 2015

