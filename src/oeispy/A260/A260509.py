# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A260509

# a_1(n) and a_2(n) both count the same sequence, in two different ways.
def a_1(n) :
    # Output the number of 2-rooted graphs in (a) with n+2 vertices
    if n == 0 :
        return 1
    else :
        return 2**((n*n + 3*n) // 2) - (2**n - 1) * a_1(n-1)
def a_2(n) :
    # Output the number of 2-rooted graphs in (a) with n+2 vertices
    # Formula: \sum_{k=0}^n (\prod_{i=1}^k 2^{i+1}) (\prod_{i=k+1}^n (1 - 2^i))
    curr_sum = 0
    for k in range(0,n+1) :
        curr_prod = 1
        for i in range(1,k+1) :
            curr_prod *= (2**(i+1))
        for i in range(k+1,n+1) :
            curr_prod *= (1 - (2**i))
        curr_sum += curr_prod
    return curr_sum

