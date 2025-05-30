# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A038206

def expr(t, d): # can you express target t with digits d, only adding +'s
    if t < 0: return False
    if t == int(d): return True
    return any(expr(t-int(d[:i]), d[i:]) for i in range(1, len(d)))
def ok(n): return expr(n, str(n*n))
print(list(filter(ok, range(7500)))) # _Michael S. Branicky_, Sep 27 2021

