# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A341092

seq=[]
for n in range(2,101):
    k=int(((n)*(n+1))/2)
    m=int(((n+1)*(n+2))/2)-4+k
    if n==2:
        seq.append(m+2)
    else:
        seq.append(m)
        seq.append(m+2)
print(seq)

