# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A379740

counter = 0
def K(x: int, y: int) -> int:
    global counter; counter += 1
    if x < 10 or y < 10: return x * y
    digits = max(len(str(x)), len(str(y))) // 2
    base = 10 ** digits
    a, b = divmod(x, base)
    c, d = divmod(y, base)
    x = K(b, d)
    y = K(a + b, c + d)
    z = K(a, c)
    return z * 10**(digits * 2) + (y - z - x) * base + x
def a(n: int) -> int:
    from sympy import fibonacci
    global counter; counter = 0
    K(fibonacci(n), fibonacci(n + 1))
    return counter
print([a(n) for n in range(1, 66)])

