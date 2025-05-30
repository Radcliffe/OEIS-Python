# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350535

from itertools import count, islice
def A350535_gen(startvalue=1): # generator of terms >= startvalue
    for n in count(max(startvalue,1)):
        flag = True
        for x in range(1,n+1):
            if 3*x+x**3 > n or not flag:
                break
            for y in range(x,n+1):
                if x+2*y+x*y**2 > n:
                    break
                if (n-x-y)%(1+x*y) == 0 and x+y*(2+x*y)<= n:
                    flag = False
                    break
        if flag:
            yield n
A350535_list = list(islice(A350535_gen(),30)) # _Chai Wah Wu_, Oct 21 2022

