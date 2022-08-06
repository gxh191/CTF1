# uncompyle6 version 3.7.4
# Python bytecode 3.8 (3413)
# Decompiled from: Python 3.7.0 (v3.7.0:1bf9cc5093, Jun 27 2018, 04:59:51) [MSC v.1914 64 bit (AMD64)]
# Embedded file name: easypyc.py
# Compiled at: 1995-09-28 00:18:56
# Size of source mod 2**32: 272 bytes
whatbox = [
 0] * 256

def aaaaaaa(a, b):
    k = [
     0] * 256
    t = 0
    for m in range(256):
        whatbox[m] = m
        k[m] = ord(a[(m % b)])
    else:
        for i in range(256):
            t = (t + whatbox[i] + k[i]) % 256
            temp = whatbox[i]
            whatbox[i] = whatbox[t]
            whatbox[t] = temp


def bbbbbbbbbb(a, b):
    q = 0
    w = 0
    e = 0
    for k in range(b):
        q = (q + 1) % 256
        w = (w + whatbox[q]) % 256
        temp = whatbox[q]
        whatbox[q] = whatbox[w]
        whatbox[w] = temp
        e = (whatbox[q] + whatbox[w]) % 256
        a[k] = a[k] ^ whatbox[e] ^ 102


def ccccccccc(a, b):
    for i in range(b):
        a[i] ^= a[((i + 1) % b)]
    else:
        for j in range(1, b):
            a[j] ^= a[(j - 1)]


if __name__ == '__main__':
    kkkkkkk = 'Geek2021'
    tttttt = [117, 62, 240, 152, 195, 117, 103, 74, 240, 151, 173, 162, 17, 75, 141, 165, 136, 117, 113, 33, 98, 151, 174, 4, 48, 25, 254, 101, 185, 127, 131, 87]
    ssss = input('Please input your flag:')
    inp = [0] * len(ssss)
    if len(ssss) != 32:
        print('Length Error!!!!')
        exit(0)
    for i in range(len(ssss)):
        inp[i] = ord(ssss[i])
    else:
        aaaaaaa(kkkkkkk, len(kkkkkkk))
        bbbbbbbbbb(inp, 32)
        ccccccccc(inp, 32)
        for m in range(32):
            if tttttt[m] != inp[m]:
                raise Exception('sorry your flag is wrong')
            print('success!!!!!!')
            print('your flag is {}'.format(ssss))