# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A213088

def f(x, y):
    if not x and y % 2:
        y = y + 1
    elif not y and not x % 2:
        x = x + 1
    elif x == y:
        if x % 2:
            x = x - 1
        else:
            y = y - 1
    elif y < x:
        if x % 2:
            y = y + 1
        else:
            y = y - 1
    else:
        if y % 2:
            x = x - 1
        else:
            x = x + 1
    return x, y
res = []
x = y = 0
for i in range(100):
    res.append(x + y)
    x, y = f(x, y)
print(res)

