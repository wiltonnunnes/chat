import socket

s = socket.socket()
host = socket.gethostname()
port = 12345

s.connect((host, port))
try:
	msg = input()
	s.send(msg.encode())
	print(s.recv(1024))
	s.close()
except ConnectionAbortedError as e:
	print('Ocorreu uma exceção: ', e)