import socket
import thread

def client_thread(con):
	while(True):
		data = con.recv(4096)
		con.sendall(data)
	con.close()	

s = socket.socket()
host = ''
port = 12345
users = {}
s.bind((host, port))
s.listen(5)

while True:
	con, addr = s.accept()
	thread.start_new_thread(client_thread, con)
s.close()
