class Message:

	def __init__(self, nickname, command, data, size = None):
		self.nickname = nickname
		self.command = command
		self.data = data

		if size is None:
			self.size = 18 + len(data)
		else:
			self.size = size

	def get_size(self):
		return self._size

	def set_size(self, value):
		if value < 0:
			raise ValueError("Size below 0 is not possible")
		self._size = value

	size = property(get_size, set_size)

	def get_nickname(self):
		return self._nickname

	def set_nickname(self, value):
		self._nickname = value

	nickname = property(get_nickname, set_nickname)

	def get_command(self):
		return self._command

	def set_command(self, value):
		self._command = value

	command = property(get_command, set_command)

	def get_data(self):
		return self._data

	def set_data(self, value):
		self._data = value

	data = property(get_data, set_data)

	def to_bytes(self):
		b = str(self.size).encode()
		b += self.str_to_byte(self.nickname, 8)
		b += self.str_to_byte(self.command, 8)
		b += self.data.encode()
		return b

	@classmethod
	def from_bytes(cls, b):
		return Message(str(b[2:10]).strip(), str(b[10:18]).strip(), str(b[18:]).strip(), int(str(b[:2])))

	def str_to_byte(self, attr, s):
		n = s - len(attr)
		return attr.encode + bytes(n)

from enum import Enum
import re

class Command(Enum):
	NAME = re.compile(r'nome\(.+\)')
	LIST = re.compile(r'lista\(\)')
	EXIT = re.compile(r'sair\(\)')
	PRIVATE = re.compile(r'privado\(.+\)')