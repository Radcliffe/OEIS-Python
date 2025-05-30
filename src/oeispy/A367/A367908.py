# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A367908

from itertools import count, islice, product
def bin_i(n): #binary indices
    return([(i+1) for i, x in enumerate(bin(n)[2:][::-1]) if x =='1'])
def a_gen(): #generator of terms
    for n in count(1):
        p = list(product(*[bin_i(k) for k in bin_i(n)]))
        x,c = len(p),0
        for j in range(x):
            if len(set(p[j])) == len(p[j]): c += 1
            if j+1 == x and c == 1: yield(n)
A367908_list = list(islice(a_gen(), 100)) # _John Tyler Rascoe_, Feb 10 2024

