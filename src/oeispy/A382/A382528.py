# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382528

def T(n, A):
    return invPerm(J(n,A))
def J(n,A):
    l=[]
    for i in range(n):
        l.append(i+1)
    index = 0
    P=[]
    for i in range(n):
        index+=A[i]
        index=index%len(l)
        P.append(l[index])
        l.pop(index)
    return P
def invPerm(p):
    inv = []
    for i in range(len(p)):
        inv.append(None)
    for i in range(len(p)):
        inv[p[i]-1]=i+1
    return inv
def DDU(n):
    return [0] + [(i)%2 for i in range(n)]
def DUD(n):
    return DDU(n+1)[1:]
def UDD(n):
    return DUD(n+1)[1:]
seq = []
for i in range(1,10):
    seq += T(i, UDD(i))
print(", ".join([str(v) for v in seq]))

