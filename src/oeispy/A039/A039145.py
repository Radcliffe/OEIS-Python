# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A039145

from itertools import count, islice
def A039145_gen(startvalue=0): # generator of terms >= startvalue
    return filter(lambda k:(s:=str(k)).count('4')==s.count('9'),count(max(startvalue,0)))
A039145_list = list(islice(A039145_gen(),40)) # _Chai Wah Wu_, Mar 05 2024

