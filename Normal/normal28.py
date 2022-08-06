# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: E:\CTF\Geek-python\python2\python2.py
# Compiled at: 2019-10-22 19:40:16
import struct, time

def fun(start, end, s):
    a = 32310901
    b = 1729
    c = s
    m = end - start# 254
    while True:
        d = int((a * c + b) % m)
        yield d
        c = d


if __name__ == '__main__':
    arr = [
     77, 263, 394, 442, 463, 512, 667, 641, 804, 752, 885, 815, 1075, 1059, 1166, 1082, 1429, 1583, 1696, 1380,
     1987, 2263, 2128, 2277, 2387, 2670, 2692, 3255, 3116, 3306, 3132, 3659, 3139, 3422, 3600, 3584, 3343, 3546,
     3299, 3633, 3281, 3146, 2990, 2617, 2780, 2893, 2573, 2584, 2424, 2715, 2513, 2324, 2080, 2293, 2245, 2309,
     2036, 1944, 1931, 1817, 1483, 1372, 1087, 1221, 893, 785, 697, 586, 547, 324, 177, 184]
    flag = raw_input('plz input your flag:')
    length = len(flag)
    a = struct.unpack('<I', flag[length - 4:].encode())[0] & 255# 小端 unsigned int
    b = []
    c = fun(1, 255, a)
    for i in range(32):
        b.append(next(c))

    d = [ 0 for i in range(72) ]
    for i in range(length):
        for j in range(32):
            a = ord(flag[i]) ^ b[j]
            d[(i + j)] += a

    for i in range(len(d)):
        if d[i] != arr[i]:
            print('fail')
            time.sleep(5)
            exit(0)

    print('success')
    time.sleep(5)
    exit(0)