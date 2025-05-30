# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A375156

def mfm_encode(data):
    prev_enc_bit, enc = "0", ""
    for i in range(len(data)):
        enc += ("1" if data[i] == "0" and prev_enc_bit == "0" else "0")
        enc += data[i]
        prev_enc_bit = enc[-1]
    return enc
def a(n):
    enc = mfm_encode(bin(n)[2:])
    return int("".join(map(str, enc)), 2)
print([a(n) for n in range(0, 55)])

