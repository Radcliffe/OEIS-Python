# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379265

def A379265_list(nterms):
    A = []
    A379266 = []
    for n in range(nterms):
        if n != 0:
            a += (a==A379266[-1])
        else:
            a = 0
        b = sum(1 for x,y in zip(A,reversed(A379266)) if x==y)
        A.append(a)
        A379266.append(b)
    return A

