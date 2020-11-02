import socket
import time
from random import *
from math import floor

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(("127.0.0.1", 2805))

with open("values.txt") as file_open:
	array=file_open.read().strip().split(" ")
S=15
N=int(array[0])
v=int(array[1])

ser=""
while ser!="ABORT":
	r=floor(uniform(2,10))
	print("r=",r)
	x=str(pow(r,2,N))
	print("x=",x)
	client_socket.send(x.encode())
	e = int(client_socket.recv(2048).decode())
	print("e=",e)
	y=str(r*pow(S,e,N))
	print("y=",y)
	client_socket.send(y.encode())
	ser=input("resume ? ")