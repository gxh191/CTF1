from Crypto.Util.number import *
import random


flag = b'????????????'
l = len(bin(bytes_to_long(flag))[2:])

if l % 32 == 0:
    l //= 32
else:
    l = l // 32 + 1

rand = ''
Rand = []
for _ in range(l):
    pro = random.getrandbits(32)#返回三十二个比特位非负随机数
    rand += bin(pro)[2:].zfill(32)#返回指定字符串长度，向右对齐，自动补零
    Rand.append(pro)

s = bin(bytes_to_long(flag))[2:].zfill(len(rand))
c = ''
for i in range(len(s)):
    c += str(int(s[i]) ^ int(rand[i]))
print(c)


def change(number):
    number = number ^ (number >> 11)
    number = number ^ ((number << 7) & 2636928640)
    number = number ^ ((number << 15) & 4022730752)
    number = number ^ (number >> 18)

    return number & 0xffffffff


for i in range(len(Rand)):
    Rand[i] = change(Rand[i])
print(Rand)

# Rand = [389902299, 3515959351, 2216779731, 2601284435, 514154742, 4172047173, 2921107804, 2217826537, 4248207905, 1322376767]
# c = 01101100010001011100100011111110110000101111000001100001110010001100111000110010111101011111100101011100111011110100001010100111100000010101100011001000011111110111111001010000010000111000101000011111011101001011110001010100100011001010001001111110011111100101111010000010101011100010001111011001010010001010001110001111
