import socket
import sys
from random import *
from math import floor
host = '127.0.0.1'
port = 2805
address = (host, port)

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_socket.bind(address)

server_socket.listen(5)

print ("Connecting to the client. . .")

conn, address = server_socket.accept()

print ("Client has been connected ", address)


with open("values.txt") as file_open:

	array=file_open.read().strip().split(" ")
N=int(array[0])

v=int(array[1])

print("v=",v)

output=""

while output!="ABORT":

    x = int(conn.recv(2048).decode())
    print("x=",x)
    e=str(floor(uniform(1,10))%2)
    print("e=",e)
    conn.send(e.encode())
    y=int(conn.recv(2048).decode())
    print("y=",y)
    rslt = x*pow(v,int(e),N)
    print("rslt=",rslt)
    intr=abs(y*y-rslt)
    if intr%N==0:
    	print("Authorized Access")
    else:
    	print("unauthorized Access")

