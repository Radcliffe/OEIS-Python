# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A279905

def t(n):
    s=0
    for a in range(0,n+1):
        for b in range(0,n+1):
            if a!=b:
                for c in range(0,n+1):
                    if a!=c and b!=c:
                        for d in range(0,n+1):
                            if d!=a and d!=b and d!=c:
                                if (a+d)%2==1:
                                    s+=1
    return s
for i in range(0,201):
    print str(i)+" "+str(t(i))

