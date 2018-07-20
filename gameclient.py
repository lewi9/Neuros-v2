import socket
import json
from threading import Thread
from Settings import PORT

class GameClient(socket.socket):
    """Ta klasa połącza się z serwerem i komunikuję się z iną instancją tej klasy"""

    def __init__(self, host, port): # param payload (dict)
        """Ta funkcja inicjalizuję tą klase"""

        super().__init__(socket.AF_INET, socket.SOCK_STREAM) # init parent class
        
        self.listenerThread = Thread(target = self.listener)
        # self.transmitterThread = Thread(target = self.transmitter) 
        
        try:
            self.connect((host, port)) # establish connection to server
            welcome_message = self.recv(1024).decode("utf-8")
            print(welcome_message)
        
        except Exception:
            pass

        # self.listenerThread.start()
        # self.transmitterThread.start()
    
    def listener(self):
        """Ta funkcja czeka na wiadomość od drugiego klienta za pomocą serwera"""
        
        while True:
            try:
                data = self.recv(1024).decode("utf-8")
                if not data:
                    from sys import exit
                    exit()
                print("Recieved from server: " + data)
            except Exception:
                pass

    def send_data(self, payload): 
        """Ta funkcja wysyła wiadomość do drugiego klienta za pomocą serwera"""

        data = self.serialize(payload)
        self.sendall(data.encode("utf-8"))

    def serialize(self, payload):
        """Zamienia pythonowe obiekty na json"""
        return json.dumps(payload)

    def deserialize(self):
        """Zamienia json obiekty na python"""
        return json.loads(self.recieved_payload)

    def activate_listner_thread(self):
        """Włącza listener funkcje jako thread"""
        self.listenerThread.start()









