# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A279063

def t(n):
    s=0
    for a in range(0,n+1):
        for b in range(0,n+1):
            for c in range(0,n+1):
                for d in range(0,n+1):
                   if (a!=b  and a!=d and b!=d and c!=a and c!=b and c!=d):
                        if (a*d-b*c) in range(-n,n+1):
                            s+=1
    return s
for i in range(0,151):
    print str(i)+" "+str(t(i))

