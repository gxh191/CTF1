# uncompyle6 version 3.7.4
# Python bytecode 3.7 (3394)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: easypy.py
# Compiled at: 2021-09-26 21:45:21
# Size of source mod 2**32: 1805 bytes


def Challenge():
    import sys
    print("Welcome to py's world")
    S = input('plz give me your flag:')
    Key = input('plz give me your key(string):')
    if len(S) != 51 or len(Key) != 8:
        print("the flag's or key's strlen...")
        sys.exit()
    else:
        tmp = S[4:50]
        KEY_cmp = 'Syclover'
        key = []
        key_cmp = ''
        for i in Key:
            key.append(ord(i))

        try:
            key_cmp += chr((key[1] * key[2] - key[5] * 72 - key[4] * 3 - key[3] ^ key[1] + (key[3] << 2) + key[2] * 6 - key[7] & key[6] - 1000) - 14)
            key_cmp += chr((key[5] * 7 + key[3] * 3 + key[2] + key[6] - (key[2] >> 2) - key[1] ^ key[0] + key[7] + (key[4] ^ key[1]) + (key[4] | key[7])) - 801)
            key_cmp += chr((key[6] * 5 + key[2] * 6 - key[3] * 7 + key[4] | key[5] + key[4] * 10 + key[0] ^ key[1] * 3 - key[7] + key[0] + key[1]) - 924)
            key_cmp += chr(key[1] * 3 + key[5] * 9 + key[0] + key[2] * 2 + key[3] * 5 - key[4] * (key[6] ^ key[7]) + 321 - 16)
            key_cmp += chr((key[5] * 12 - key[0] ^ key[6] - key[3] * 23 + key[4] * 3 + key[2] * 8 + key[1] - key[7] * 2 + key[6] * 4 + 1324) + 1)
            key_cmp += chr(key[3] * 54 - key[1] * 3 + key[2] * 3 + key[4] * 11 - key[5] * 2 + key[0] + key[7] * 3 - key[6] - 6298 + 40)
            key_cmp += chr(key[7] - key[6] * key[3] + key[2] * key[2] - key[4] * 32 + key[5] * (key[0] >> 2) - key[1] * key[1] - 6689 + 41)
            key_cmp += chr((key[5] - key[3] * 41 + key[6] * 41 + key[5] ^ (key[4] & key[6] | key[0]) - (key[7] * 24 | key[2]) + key[1] - 589) - 36)
        except ValueError:
            print("You know what I'm going to say...")
            sys.exit()

        if key_cmp != KEY_cmp:
            print("You know what I'm going to say...")
            sys.exit()
        flag = [
         113, 74, 71, 35, 29, 91, 29, 12, 114, 73, 60, 52, 69, 5, 113, 35, 95, 38, 20, 112, 95, 7, 74, 12, 102, 23, 7, 31, 87, 5, 113, 98, 85, 38, 16, 112, 29, 6, 30, 12, 65, 73, 83, 36, 12, 23]
        for i in range(46):
            if ord(tmp[i]) ^ key[((i + 1) % len(key))] != flag[i]:
                print("You know what I'm going to say...")
                sys.exit()

        print('Yeah!Submit your flag in a hurry~')


Challenge()
