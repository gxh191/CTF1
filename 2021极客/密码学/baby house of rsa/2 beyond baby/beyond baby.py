from Crypto.Util.number import *
import libnum



key3 =b'****'
m = bytes_to_long(key3)
#  取多个重复
a1= getPrime(512)

n = a1*a1*a1*a1

# 欧拉函数 套公式
phi = (a1**4-a1**3)

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

# 参数
# 没有捏~



