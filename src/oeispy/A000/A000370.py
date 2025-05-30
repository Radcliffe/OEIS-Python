# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A000370

def partition_lin(n, d, depth=0):
  if d == depth:
    if n==0: yield ()
  else: yield from (item + (i,) for i in range(n+1) for item in partition_lin(n-i*(depth+1), d, depth=depth+1))
def get_num_equiv_bool_func(n, sc=False):
  import math, operator, functools
  from sympy import mobius
  def e(k): return sum((1<<d)*mobius(k//d) for d in range(1, k+1) if k % d == 0)//k
  def g(two_k): return sum((1<<(d//2))*mobius(two_k//d) for d in range(1, two_k+1) if two_k % d == 0 and two_k//2 % d != 0)//two_k
  return sum(math.factorial(n)*(1<<n)//functools.reduce(operator.mul, (math.factorial(ji)*(2*(n-i))**ji for i, ji in enumerate(j)), 1)*sum(functools.reduce(operator.mul, (0 if sc and d&1 else 1<<x for d, x in a), 1) for a in ([[(1,1)]] if n==0 else functools.reduce(lambda x, y: [[(math.lcm(p, q), math.gcd(p, q)*ip*jq) for p, ip in a for q, jq in b] for a in x for b in y], ([[(d, e(d)) for d in range(1, i+1) if i % d ==0], [(d, g(d)) for d in range(1, 2*i+1) if 2*i % d == 0 and i % d != 0]] for i in range(1, n+1) for _ in range(j[n-i]))))) for j in partition_lin(n, n))//(math.factorial(n)*(1<<n))
[(get_num_equiv_bool_func(n)+get_num_equiv_bool_func(n,True))//2 for n in range(0,10)] # _Gregory Morse_, Dec 23 2024

