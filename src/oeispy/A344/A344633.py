# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A344633

a ="1234567890"
for k in range(10):
    a = a + a
sol = ""
for n in range(1, len(a)):
    if int(a[0:n]) % n == 0:
        sol = sol + str(n) + ", "
print(sol)

