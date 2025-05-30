# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A325945

# returns [q,k,D,cFlag]
# q is smallest non-Carmichael composite q that forms an idempotent
# factorization with p_bar
# q=k*DP+1
# # D is DP unless DP is 1 in which case D is DQ
# cFlag is False, indicates number is not Carmichael
# assumes p_bar is squarefree
# max_k limits # values checked, -1 means no limit.
# Returns [-1,-1,-1,False] if no q found before limit reached
# D_(p_bar) is lambda(p_bar)/gcd(lambda(p_bar),p_bar-1)
# uses numbthy python library
# some functions defined elsewhere, hopefully names indicate what they do
def findSmallestNonCarmichaelQbar(p_bar,min_k,max_k):
    DP = D_(p_bar)
    k = min_k
    if min_k != 0:
        k = min_k-1     # ensures min_k is tried
    Found = False
    while not Found:
        if k > max_k and max_k != -1:
            return [-1,-1,-1,False]
        k += 1
        if k % 10000000 == 0:
            print("   ",k)
        q = k*DP+1
        if not numbthy.gcd(p_bar,q) == 1:
            continue
        try:
            q_factors = numbthy.factor(q)
        except:
            print("problem factoring",q)
            prompt()
        if not is_square_free_with_list(q,q_factors):
            continue
        DQ = D_with_list(q,q_factors)
        if DQ == 1: # q is prime or Carmichael, skip it
            continue
        else:
            if p_bar % DQ == 1:
                if DP != 1:
                    return [q,k,DP,False]
                else:
                    return [q,k,DQ,False]

