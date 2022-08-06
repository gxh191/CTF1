# uncompyle6 version 3.8.0
# Python bytecode 2.7 (62211)
# Decompiled from: Python 3.8.9 (tags/v3.8.9:a743f81, Apr  6 2021, 14:02:34) [MSC v.1928 64 bit (AMD64)]
# Embedded file name: E:/Code/python/Geek-python/python1.py
# Compiled at: 2019-10-22 16:59:55
import struct, time

def b(a):
    return a & FFFFFFFFFFFFFFFF


def c(str):
    return struct.unpack('<Q', str)[0]  #小端 unsigned long long 8字节 64位


def d(a):
    for i in range(64):
        a = a * 2#偶
        if a > FFFFFFFFFFFFFFFF:
            a = b(a)#去掉多出来的位数
            a = b(a ^ 0xB0004B7679FA26B3)#1011000000000000010010110111011001111001111110100010011010110011 异或完，奇数变偶数，偶数变奇数

    return a#奇变偶 偶变奇


if __name__ == '__main__':
    cmp_data = [7966260180038414229, 16286944838295011030, 8598951912044448753, 7047634009948092561, 7308282357635670895]
    input = input('plz input your flag:')
    if len(input) % 8 != 0:
        for i in range(8 - len(input) % 8):
            input += '\x00'#不够八位补零

    arr = []
    for i in range(len(input) / 8):
        value = d(c(input[i * 8:i * 8 + 8]))
        arr.append(value)

    for i in range(5):
        if arr[i] != cmp_data[i]:
            print('fail')
            time.sleep(5)
            exit()

    print('success')
    time.sleep(5)
    exit()

