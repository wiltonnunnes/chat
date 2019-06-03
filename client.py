import socket
import select
from protocol import *
import re

def create_message(data):
	command = data.strip().split()[0]
	if n_command:
		m = Message(dst, n_command, data)
	elif re.match(r'[a-z]+\(.*\)', command):
		m = Message(dst, command, '')
	else:
		m = Message(dst, '', data)
	return m

s = socket.socket()
host = 'localhost'
port = 12345
s.connect((host, port))
dst = None
n_command = None

while True:
	inp, out, exc = select.select([s], [s], [s], 0)
	if inp:
		m = Message(s.recv(4096))
		if m.command == 'destinatario':
			dst = m.data
		print(m.data)
	if out:
		data = input()
		s.sendall(create_message(data).to_bytes())
s.close()
