#!/usr/bin/env python3

#Paul Croft
#August 25, 2021

import random
import string

chr_table = list(string.ascii_letters)
random.shuffle(chr_table)
chr_table = ''.join(chr_table)
prehalf, posthalf = chr_table[:26], chr_table[26:]
ttable = str.maketrans(string.ascii_lowercase, prehalf)
rttable = str.maketrans(prehalf,string.ascii_lowercase)

def encrypt(instr, deslen=20):
    retval = list(instr.translate(ttable))
    retlen = len(retval)
    while retlen < deslen:
        idx = random.randint(0,retlen)
        retval.insert(idx,random.choice(prehalf))
        retval.insert(idx,random.choice(posthalf))
        retlen += 2
    return ''.join(retval)

def decrypt(instr):
    retval = []
    temp = list(instr)[::-1]#reversed
    while temp:
        test_val = temp.pop(0)
        if test_val in prehalf:
            retval.append(test_val)
        else:
            retval.pop()
    return ''.join(retval[::-1]).translate(rttable)

def main():
    teststring = "hellothere"
    print(teststring)
    print(string.ascii_lowercase)
    print(prehalf)
    encrypted_test = encrypt(teststring)
    print(encrypted_test)
    decrypted_test = decrypt(encrypted_test)
    print(decrypted_test)


if __name__ == '__main__':
    exit(main())
