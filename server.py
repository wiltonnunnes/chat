import socket
import _thread
from protocol import *
import re
import select

class Server:

	def __init__(self, host='', port=12345):
		self.server_socket = socket.socket()
		self.server_socket.bind((host, port))
		self.clients = {}

	def broadcast_data(self, socket, data):
		for client in self.clients:
			if client is not socket:
				m = Message(self.clients[socket][0], '', data)
				client.sendall(m.to_bytes())

	def client_thread(self, con):
		con.sendall(Message('', '', 'Escolha um nickname').to_bytes())
		while(True):
			data = con.recv(4096)
			self.exec_command(socket, data)

	def exec_command(self, socket, msg):
		m = Message.from_bytes(msg)

		command = m.command
		if self.clients[socket][0] is None:
			if Command.NAME.value.match(command):
				self.clients[socket][0] = nickname
				print('%s entrou...' % (nickname))
			else:
				socket.sendall(Message('', '', 'Escolha um nickname').to_bytes())
		else:
			if Command.NAME.value.match(command):
				nickname = command.split('(')[1].strip(')')
				old_nickname = self.clients[socket][0]
				self.clients[socket][0] = nickname
				print('%s agora é %s' % (old_nickname, nickname))
			elif Command.LIST.value.match(command):
				m = Message(self.clients[socket], '', self.clients.values())
				socket.sendall(m.to_bytes())
			elif Command.EXIT.value.match(command):
				socket.close()
				del self.clients[socket]
				print('%s saiu!' % (self.clients[socket][0]))
			elif Command.PRIVATE.value.match(command):
				nickname = command.split('(')[1].strip(')')
				m = Message(nickname, 'private(' + self.clients[socket][0] + ')', "O cliente " + self.clients[socket][0] + "quer se conectar com você, digite 'S' para aceitar ou 'N' para rejeitar: ")
				sock = self.getSocketByNickname(nickname).sendall(m.to_bytes())
				resp = Message.from_bytes(sock.recv(4096)).data
				dst = ''
				if resp == 'S':
					dst = self.clients[socket][0]
				sock.sendall(Message('', 'destinatario', dst).to_bytes())
			else:
				data = '%s escreveu: %s' % (self.clients[socket][0], m.data)
				print(data)
				self.broadcast_data(socket, data)

	def check_nickname(self, nickname):
		return nickname in self.clients.values()

	def send_data(self, socket, msg):
		socket.sendall(msg.encode())

	def getSocketByNickname(self, nickname):
		for k, v in self.clients.items():
			if nickname in v:
				return k
		return None

	def server_thread(self, name):
		while True:
			data = input('%s: '%(name))
			if data == 'lista()':
				print(self.clients.values())
			elif data == 'sair()':
				break
		_thread.interrupt_main()

	def run(self):
		_thread.start_new_thread(self.server_thread, ('Servidor',))
		while True:
			con, addr = self.server_socket.accept()
			_thread.start_new_thread(self.client_thread, (con,))

def main():
	server = Server()
	server.run()

if __name__ == "__main__":
	main()
