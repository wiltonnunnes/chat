import socket
import select

s = socket.socket()
host = 'localhost'
port = 12345
s.connect((host, port))

while True:
	inp, out, exc = select.select([s], [s], [s], 0)
	if inp:
		print(s.recv(4096))
	if out:
		data = input()
		s.sendall(data.encode())
s.close()
