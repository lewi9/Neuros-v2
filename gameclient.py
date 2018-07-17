import socket
from threading import Thread
import json

test_data = {
	"player name" : "Bob",
	"Health" : 100,
	"Attack" : 50
}

clean_data = json.dumps(test_data)


host, port = "localhost", 5000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((host, port))
data = s.recv(1024).decode("utf-8")
print(data)

def listener():
	while True:
		data = s.recv(1024).decode("utf-8")
		if not data:
			from sys import exit
			exit()
		print("Recieved from server: " + data)

s.sendall(clean_data.encode("utf-8"))

def broadcaster():
	while True:
		message = input("-> ")
		s.sendall(message.encode("utf-8"))
	s.close()

l = Thread(target = listener)
b = Thread(target = broadcaster)

l.start()
b.start()



