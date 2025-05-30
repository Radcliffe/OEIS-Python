# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A001003

# The objective of this implementation is efficiency.
# n -> [a(0), a(1), ..., a(n)]
def A001003_list(n):
    a = [0 for i in range(n)]
    a[0] = 1
    for w in range(1, n):
        s = 0
        for j in range(1, w):
            s += a[j]*a[w-j-1]
        a[w] = a[w-1]+2*s
    return a
# _Peter Luschny_, May 17 2011

