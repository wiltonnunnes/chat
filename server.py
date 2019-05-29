import socket
import _thread

def broadcast_data(socket, data):
	for client in clients:
		if client is not socket:
			client.sendall(data)

def client_thread(con):
	while(True):
		data = con.recv(4096)
		print(data.decode())
		broadcast_data(con, data)
	con.close()	

s = socket.socket()
host = ''
port = 12345
clients = []
s.bind((host, port))
s.listen(5)

while True:
	con, addr = s.accept()
	print(addr)
	clients.append(con)
	_thread.start_new_thread(client_thread, (con,))
s.close()
