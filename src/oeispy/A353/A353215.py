# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A353215

def f(n):
    return (3*n - 1)//2;
def a(pow, n):
    if (pow == 0): return n;
    else: return a(pow-1, f(n));
l = [a(n, n) for n in range(21)];

