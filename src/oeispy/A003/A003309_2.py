# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A003309

def A003309(): # generator of the infinite list of ludic numbers
    L = [2, 3]; yield 1; yield 2; yield 3
    while k := len(L)//2: # could take min{k | k >= L[-1-k]-1}
        for j in L[-1-k::-1]: k += 1 + k//(j-1)
        L.append(k+2); yield k+2
A003309_upto = lambda N=99: [t for t,_ in zip(A003309(),range(N))]
# _M. F. Hasler_, Nov 02 2024

