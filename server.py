import socket
import _thread

class Server:

	def __init__(self, host='localhost', port=12345):
		self.server_socket = socket.socket()
		self.server_socket.bind((host, port))
		self.clients = []

	def broadcast_data(socket, data):
		for client in self.clients:
			if client is not socket:
				client.sendall(data)

	def client_thread(self, con):
		while(True):
			data = con.recv(4096)
			print(data.decode())
			broadcast_data(con, data)
		con.close()

	def run(self):
		while True:
			con, addr = self.server_socket.accept()
			_thread.start_new_thread(self.client_thread, (con,))

def main():
	server = Server()
	server.run()

if __name__ == "__main__":
	main()
