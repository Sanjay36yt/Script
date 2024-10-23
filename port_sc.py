#!/bin/python3

import sys
import socket
from datetime import datetime as dt #alise as (dt)

port_num=[80,443,3306,21,25,8005,1417,79,105,106,110,143,22,2224,8080,40563,40564,8000,53,2221]

#cli argument
if len(sys.argv) == 2:
    target = str(sys.argv[1])
    print(target)
else:
    print("Enter the <ip>")
    print("Syntex: python3 port_sc.py <ip>")


#banner prity
print("_"*50)
print("Target ip : "+str(target))
print("Started time :"+str(dt.now())) # using alise
print("_"*50)

#scanning part
try:
    for ports in port_num:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,ports))
        if result == 0:
            print(f" The port {ports} is open")
        s.close()

except KeyboardInterrupt:
    print("Execting the code")
    exit()

except socket.gaierror:
    print("host coud not resolve")
    exit()

except socket.error:
    print("Coud not connect the server")
    exit()
