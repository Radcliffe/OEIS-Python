# This file is auto-generated from OEIS data.
# Please do not edit this file directly.
# OEIS sequence: A370470

def A370470(n):
    s = bin(n)[2:]
    run_length = 0
    runs = []
    last_char = '2'
    for j in range(len(s)):
        if(s[j] != last_char):
            last_char = s[j]
            runs.append(run_length)
            run_length = 1
        else:
            run_length+=1
    runs.append(run_length)
    k = ''
    for j in range(1, len(runs)):
        k+=str(chr(ord('0')+(j%2)))*abs(runs[j]-runs[j-1])
    return int(k, 2)

