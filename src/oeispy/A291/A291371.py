# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A291371

# Python version 2.7
rot_sym = [
  0, 1, 4, 131, 14118, 2976853, 1013582110, 508233789579, 352755124921122,
  324039613564554401, 380751174738424280720, 557175918657122229139987,
  993806827312044893602464496, # A291172
]
def u(n):
  if n < 0:
    return 0
  if n <= 1:
    return 1
  sum = 0
  sum -= (4 * n - 1) * u(n - 1)
  sum += n * (2 * n - 3) * (10 * n - 9) * u(n - 2)
  sum += 5 * (2 * n - 3) * (2 * n - 4) * (2 * n - 5) * u(n - 3)
  sum -= 2 * (2 * n - 3) * (2 * n - 4) * (2 * n - 5) * (2 * n - 6) * (2 * n - 7) * u(n - 4)
  return sum / (n + 1)
for i in range(1, 13):
  print (2 * rot_sym[i] + u(i) + u(i - 1) * (2 * i - 1)) / 4

