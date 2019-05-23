import socket
import threading

def client_thread(conn):
	

s = socket.socket()
host = ''
port = 12345
users = {}

s.bind((host, port))

s.listen(5)
clients = []

while True:
	c, addr = s.accept()
	print('Got connection from', addr)
	msg = s.recv(1024)
	print('Mensagem do cliente : ', msg)
	c.send(msg)
	c.close()
