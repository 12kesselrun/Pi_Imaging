import socket
import sys

# Query both the localhost and the networked node found at 169.254.141.246
HOST = '169.254.141.246'
PORT = 10000
s = socket.socket()
s.connect((HOST, PORT))
HOST = '127.0.0.1'
PORT = 10000
d = socket.socket()
d.connect((HOST, PORT))
HOST='169.254.218.239'
PORT=10000
f = socket.socket()
f.connect((HOST, PORT))
HOST='169.254.246.215'
PORT=10000
g=socket.socket()
g.connect((HOST, PORT))

print s
print d
print f
print g

# Send commands to both instances of the socket() class
while 1:
    msg = raw_input("Command To Send: ")
    if msg == "close":
       s.close()
       d.close()
       f.close()
       g.close()
       sys.exit(0)
    s.send(msg)
    d.send(msg)
    f.send(msg)
    g.send(msg)