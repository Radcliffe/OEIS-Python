# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A034002

from sympy import flatten
l=[1]
L=[1]
n=s=1
y=''
while n<21:
    x=str(l[n - 1]) + ' '
    for i in range(len(x) - 1):
        if x[i]==x[i + 1]: s+=1
        else:
            y+=str(s)+str(x[i])
            s=1
    x=''
    n+=1
    l.append(int(y))
    L.append([int(a) for a in list(y)])
    y=''
    s=1
print(l) # A005150
print(flatten(L)) # _Indranil Ghosh_, Jul 05 2017

