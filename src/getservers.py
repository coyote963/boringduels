import socket
import urllib.request, urllib.error, urllib.parse

types = {
	'0':'Capture the Flag', 
	'1': 'Deathmatch', 
	'2': 'Climb', 
	'3': 'Zombrains', 
	'4': 'Survival', 
	'5': 'Team Deathmatch', 
	'6': 'Weapons Deal', 
	'8': 'Takeover'}

class Parser:
	def get(self, connection):
		self.data = ''
		needed = int(connection.recv(1).encode("hex"), 16) / 2
		while needed:
			chunk = connection.recv(needed)
			needed -= len(chunk)
			self.data += chunk
		self.data = self.data.encode("hex")
		if len(self.data) == 4:
			return self.data
		return self.parse(self.data)

	def parse(self, data):
		self.data = data
		self.index = 0
		self.read(4)
		return self.read_entry()

	def read(self, size=None, eat_null=True):
		if not size:
			size = self.data.find("00", self.index) - self.index
			if size % 2: size += 1 # make sure not to stop one early from a preceding hex char with a trailing zero
		chunk = self.data[self.index: self.index + size]
		self.index += len(chunk)
		if eat_null: self.read(2, False)
		return chunk

	def read_message(self):
		length = self.read_int() + 1

	def read_null(self):
		self.read(2)  # Hmm... something isn't 100% right, this assert fails.
		#assert self.read(2) == '00'

	def read_int(self, size=2):
		return int(self.read(size), 16)

	def read_string(self):
		return self.read().decode('hex')

	def read_bool(self):
		return str(bool(self.read_string()))

	def read_entry(self):
		entry = {}
		entry["ip"] = self.read_string()
		entry["name"] = self.read_string()
		entry["locked"] = self.read_bool()
		entry["type"] = types.get(str(self.read_int(2)), 'Unknown')
		entry["map"] = self.read_string()
		entry["players"] = self.read_int()
		entry["max"] = self.read_int()
		entry["unknown"] = self.read(4, eat_null=False)
		return entry


def build_server_request(version):
	command = "1501"
	null = "00"
	version = version.encode("hex")
	message = command + null + version + null
	return message.decode("hex")

def get_latest_version():
	return urllib.request.urlopen('http://www.spasmangames.com/version.html').read()

def get_servers(version=None):
	version = version or get_latest_version()
	servers = []
	parser = Parser()
	
	connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	connection.connect(("spasmangames.com", 7781))
	connection.settimeout(1.0)
	connection.send(build_server_request(version))
	try:
		while True:
			message = parser.get(connection)
			if isinstance(message, dict):
				servers.append(message)
	except socket.timeout as exc:
		pass

	connection.close()
	servers.sort(key=lambda x: x.get('name'))
	return servers

if __name__=='__main__':
	print(get_servers())