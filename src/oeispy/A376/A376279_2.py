# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A376279

from itertools import count, islice
from sympy import integer_nthroot
def A376279_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda k:not k%3 or integer_nthroot(k,3)[1],count(max(startvalue,0)))
A376279_list = list(islice(A376279_gen(),30))

