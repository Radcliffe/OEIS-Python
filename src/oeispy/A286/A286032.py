# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A286032

l=[1, 1]
a=b=1
i=2
while i<=30:
    l.append(b - i*a)
    b=l[-1]
    a=l[-2]
    i+=1
print(l) # _Indranil Ghosh_, May 01 2017

