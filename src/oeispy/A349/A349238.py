# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A349238

def NumToFib(n): # n > 0
    f0, f1, k = 1, 1, 0
    while f0 <= n:
        f0, f1, k = f0+f1, f0, k+1
    s = ""
    while k > 0:
        f0, f1, k = f1, f0-f1, k-1
        if f0 <= n:
            s, n = s+"1", n-f0
        else:
            s = s+"0"
    return s
def RevFibToNum(s):
    f0, f1 = 1, 1
    n, k = 0, 0
    while k < len(s):
        if s[k] == "1":
            n = n+f0
        f0, f1, k = f0+f1, f0, k+1
    return n
n, a = 0, 0
print(a, end = ", ")
while n < 71:
    n += 1
    print(RevFibToNum(NumToFib(n)), end = ", ") # _A.H.M. Smeets_, Nov 14 2021

