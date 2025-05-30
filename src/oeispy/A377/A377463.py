# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377463

from gmpy2 import digits
def A377463(n):
    def f(x):
        s = digits(x,4)
        for i in range(l:=len(s)):
            if s[i]>'1':
                break
        else:
            return n+int(s,2)
        return n-1+(int(s[:i] or '0',2)+1<<l-i)
    m, k = n, f(n)
    while m != k: m, k = k, f(k)
    return m

