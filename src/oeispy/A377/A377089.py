# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A377089

def ssd(n): return sum(int(d)**2 for d in str(n))
def f(n): return (d:=list(map(int, str(n))))[0] * sum(di*di for di in d)
def happy(n):
    if n == 1: return True
    s = list(map(int, str(n)))
    while n not in [1, 4]: n = ssd(n) # iterate until fixed point or cycle
    return n == 1
def elated(n):
    if n == 1: return True
    traj = {n}
    while (n:=f(n)) not in traj: traj.add(n)
    return 1 in traj
def ok(n): return happy(n) and elated(n)
print([k for k in range(1, 2001) if ok(k)]) # _Michael S. Branicky_, Oct 16 2024

