# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A369625

# requires Normaliz from version 3.10.2
import math
import PyNormaliz
from PyNormaliz import *
NmzSetNumberOfNormalizThreads(1)
def function(N):
    L = []
    sN1 = math.isqrt(N//3)
    sN = math.isqrt(N)
    for i1 in range(3, sN1):
        m1 = min(sN, N - i1**2, i1**2 + 1)
        for i2 in range(i1+1, m1):
            m2 = min(sN, N - i1**2 - i2**2, i2**2 + 1)
            for i3 in range(i2+1, m2):
                n = 1 + i1**2 + i2**2 + i3**2
                if n <= N:
                    C = Cone(fusion_type = [[1,i1,i2,i3]])
                    l = C.FusionRings()
                    if len(l)>0:
                        L.append(n)
    L.sort()
    return(L)
print(function(1000))

