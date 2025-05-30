# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A362020

from itertools import count, islice
def A362020_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda n:n%10 and n==int(''.join((s:=str(n**2))[len(s)&1^1::2])),count(max(startvalue,0)))
A362020_list = list(islice(A362020_gen(),50))

