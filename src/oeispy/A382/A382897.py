# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A382897

def A(n):
    m = n
    for i in map(int, str(n)):
        if i != 0 and m % i == 0:
            m //= i
    return n // m
def A382897(n):
    return [A(i) for i in range(1, n + 1)]
print(A382897(100))

