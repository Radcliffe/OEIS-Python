# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A046831

from itertools import count, islice
def A046831_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:n%10 and str(n) in str(n**2), count(max(startvalue,0)))
A046831_list = list(islice(A046831_gen(),20)) # _Chai Wah Wu_, Apr 04 2023

