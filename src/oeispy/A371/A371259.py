# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A371259

def T_Lah(n, k):
    if k < 3 or k > n:
        return 0
    elif n == k == 3:
        return 1
    else:
        return T_Lah(n-1, k-1) + ((n+k-1)**2) * T_Lah(n-1, k)
print([T_Lah(n, k) for n in range(3, 12) for k in range(3, n+1)])

