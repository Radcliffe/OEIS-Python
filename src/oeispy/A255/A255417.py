# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A255417

def A255417(n, S=510510, P=5760):
    try: n -= 1; return A255417.L[n]
    except IndexError: return A255417.L[n%P] + n//P*S
    except AttributeError: L = [x+5-x%2 for x in range(0, S, 3)]
    for k in L[:4]: L = [x for i,x in enumerate(L) if i%k]
    A255417.L = L[::17]; return A255417(n+1) # _M. F. Hasler_, Nov 17 2024

