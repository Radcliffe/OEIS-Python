# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A254042

# Output doesn't include a(0).
def A254042():
    index = 1
    k = 0
    f = 1
    u = '1'
    while True:
        sf = str(f)
        if u in sf and u+'1' not in sf:
            print("A254042("+str(index)+") = " +str(k))
            index += 1
            k = 0
            f = 1
            u +='1'
        k += 1
        f *= k
    return

