# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A263314

A263314_list = []
for i in range(10**4):
    s = str(i)
    for d in s:
        j = int(d)
        if j :
            for e in s:
                if int(e) % j:
                    break
            else:
                A263314_list.append(i)
                break
# _Chai Wah Wu_, Oct 21 2015

