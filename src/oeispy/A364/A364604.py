# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A364604

def A364604(N):
    a = [0]*N; z=s=0
    while(s<N):
        z+=1; m=0; i=s
        while(i<N):
            if not a[i]:
                a[i]=z; i+=2**m; m+=1
            i+=1
        s+=1
    return a

