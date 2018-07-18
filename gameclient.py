import socket
import json
from threading import Thread

host, port = "localhost", 5000

class GameClient(socket.socket):
	"""Ta klasa połącza się z serwerem i komunikuję się z iną instancją tej klasy"""

	def __init__(self, host, port): # param payload (dict)
		"""Ta funkcja inicjalizuję tą klase"""

		super().__init__(socket.AF_INET, socket.SOCK_STREAM) # init parent class
		#self.payload = dict with game info
		#self.recieved_payload = some data this klient recieves from other client
		self.listenerThread = Thread(target = self.listener)
		self.transmitterThread = Thread(target = self.transmitter) 
		
		self.connect((host, port)) # establish connection to server
		welcome_message = self.recv(1024).decode("utf-8")
		print(welcome_message)

		self.listenerThread.start()
		self.transmitterThread.start()
	
	def listener(self):
		"""Ta funkcja czeka na wiadomość od drugiego klienta za pomocą serwera"""
		
		while True:
			data = self.recv(1024).decode("utf-8")
			if not data:
				from sys import exit
				exit()
			print("Recieved from server: " + data)

	def transmitter(self): # add paramenter data instead of local var message (data will be json)
		"""Ta funkcja wysyła wiadomość do drugiego klienta za pomocą serwera"""

		while True:
			message = input("-> ")
			self.sendall(message.encode("utf-8"))
		self.close()

	def serialize(self):
		"""Zamienia pythonowe obiekty na json"""
		return json.dumps(self.payload)

	def deserialize(self):
		"""Zamienia json obiekty na python"""
		return json.loads(self.recieved_payload)


# a = GameClient(host, port)





