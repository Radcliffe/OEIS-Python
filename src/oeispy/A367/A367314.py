# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367314

import math
def a(n):
    p=[1]
    for i in range(n):
        p.append(math.lcm(*p))
        for x in range(0, len(p)-1):
            p[x]+=1
    return p[-1]

