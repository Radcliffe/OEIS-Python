# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A162614

def A162614(n,k):
    return n+k*(n**3-1)
print([A162614(n,k) for n in range(20) for k in range(n+1)])
# _R. J. Mathar_, Oct 20 2009

