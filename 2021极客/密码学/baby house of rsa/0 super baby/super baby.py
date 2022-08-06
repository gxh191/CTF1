from Crypto.Util.number import *
import libnum



key1 =b'******'
m = bytes_to_long(key1)
#  取两个素数
p,q = getPrime(512),getPrime(512)
n = p*q

# 欧拉函数
phi = (p-1)*(q-1)

# 取一个与phi互素的素数
e = 0x10001
print(f'最大公约数:{libnum.gcd(e,phi)}')

# 计算私钥 即e关于phi的逆元d
d = libnum.invmod(e,phi)

# 计算加密: m^e = c mod n
c = pow(m,e,n)
fr = open('./data','w+')

# 公钥
print(f'e={e}',file=fr)
print(f'n={n}',file=fr)

# 密文
print(f'c={c}',file=fr)

# 私钥
print(f'd={d}',file=fr)



