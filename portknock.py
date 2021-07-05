#!/usr/bin/env python
from socket import *

ip = "172.16.171.134"

s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, 1337))

r = eval(s.recv(1024))
print "received:", r

for p in r: 
    try:
        print "knocking on port:", p
        s2 = socket(AF_INET, SOCK_STREAM)
        s2.connect((ip, p))
        print s2.recv(1024)
    except:
        pass
print "done"