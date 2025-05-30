# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A035928

from itertools import count, islice
def A035928_gen(startvalue=1): # generator of terms >= startvalue
    return filter(lambda n:n==int(format(~n&(1<<(m:=n.bit_length()))-1,'0'+str(m)+'b')[::-1],2),count(max(startvalue,1)))
A035928_list = list(islice(A035928_gen(),30)) # _Chai Wah Wu_, Jun 30 2022

