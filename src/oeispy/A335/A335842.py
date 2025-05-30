# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A335842

import math
n_max = 10000000
d_max = 10000
list1 = []
n = 1
while n <= n_max:
  a_tetr = n*(n + 1)*(n + 2)//6
  m_min = math.floor(math.pow(a_tetr, 1/3))
  m = m_min
  a_cube_max = n*(n + 1)*(n + 2)//6 + d_max
  m_max = math.ceil(math.pow(a_cube_max, 1/3))
  while m <= m_max:
      a_cube = m**3
      d = a_cube - a_tetr
      if d >= 0 and d <= d_max and d not in list1:
          list1.append(d)
      m += 1
  n += 1
list1.sort()
print(list1)

