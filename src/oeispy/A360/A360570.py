# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A360570

from itertools import count, islice
from sympy import integer_nthroot
def A360570_gen(startvalue=1): # generator of terms >= startvalue
    for n in count(max(startvalue,1)):
        if integer_nthroot(m:=10*n,3)[1]:
            yield n
        else:
            a = 1
            while (k:=(integer_nthroot(a*(m+1)-1,3)[0]+1)**3-m*a)>=10*a:
                a *= 10
                if a > n:
                    break
            else:
                if k <= n:
                    yield n
A360570_list = list(islice(A360570_gen(),20))

