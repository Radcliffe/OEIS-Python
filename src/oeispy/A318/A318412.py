# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A318412

fine=70
zc = []
ris=""
def nclass(v):
    n=0
    l=[]
    for item in v:
        if item not in l:
            l.append(item)
            n+=1
    return n
for z in range(1,fine):
    for k in range(z): zc.append(0)
    for i in range(z):
        for j in range(z):
            r=(i*j)%z
            zc[r]+=1
    ris = ris + "," + str(nclass(zc))
    zc = []
print(ris)

