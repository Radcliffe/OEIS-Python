# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A066369

from sympy import subsets
def noap4(n):
    avoid=list()
    for skip in range(1,(n+2)//3):
        for start in range (1,n+1-3*skip):
            avoid.append(set({start,start+skip,start+2*skip,start+3*skip}))
    s=list()
    for i in range(4):
        for smallset in subsets(range(1,n+1),i):
            s.append(smallset)
    for i in range(4,n+1):
        for temptuple in subsets(range(1,n+1),i):
            tempset=set(temptuple)
            status=True
            for avoidset in avoid:
                if avoidset <= tempset:
                    status=False
                    break
            if status:
                s.append(tempset)
    return s
# Counts all such sets
def a(n):
    return len(noap4(n)) # _David Nacin_, Mar 05 2012

