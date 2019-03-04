import socket

s = socket.socket()
host = socket.gethostname()
port = 12345
s.bind((host, port))

s.listen(5)
while True:
	c, addr = s.accept()
	print('Got connection from', addr)
	msg = s.recv(1024)
	print('Mensagem do cliente : ', msg)
	c.send(msg)
	c.close()