# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A350574

import numpy as np
# preliminary functions we will use in building our list
def is_prime(n):
    for d in range(2,int(np.sqrt(n))+1):
        if n % d == 0:
            return False
    return True
def asc(n): # returns integer with digits of n in ascending order
    n_list = [int(digit) for digit in str(n)] # separate digits of n into a list
    n_list.sort() # rearrange numbers in ascending order
    asc_n = int(''.join([str(digit) for digit in n_list])) # concatenate the sorted digits
    return asc_n
def desc(n): # returns integer with digits of n in descending order
    n_list = [int(digit) for digit in str(n)]
    n_list.sort(reverse=True)
    desc_n = int(''.join([str(digit) for digit in n_list]))
    return desc_n
N = 5
# get list of integers n such that n, asc(n), and desc(n) are all distinct primes
condition_1 = [n for n in range(2,10**N)
               if is_prime(n)
               and is_prime(asc(n))
               and is_prime(desc(n))
               and n not in (asc(n),desc(n))]
# refine so that our list includes only the minimum permutation of a given set of digits satisfying condition 1
condition_2 = []
for num in condition_1:
    if asc(num) not in [asc(n) for n in condition_2]:
        condition_2.append(num)
print(condition_2)

