# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A358985

def A358985(n):
    if n == 1:
        return 10
    kset = set()
    for i in range(10**(n-2),10**(n-1)):
        for j in range(int((s:=str(i))[0])+1):
            kset.add(10*i+j+int(str(j)+s[::-1]))
    return len(kset) # _Chai Wah Wu_, Dec 09 2022

