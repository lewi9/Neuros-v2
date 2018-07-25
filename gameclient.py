import socket
import json
import pprint
from time import sleep
from threading import Thread
from Settings import PORT


class GameClient(socket.socket):
    """Ta klasa połącza się z serwerem i komunikuję się z iną instancją tej klasy"""

    def __init__(self, host, port): # param payload (dict)
        """Ta funkcja inicjalizuję tą klase"""
        self.host = host
        self.port = port
        self.recv_data = None
        self.data_to_be_sent = None
        self.listening = True
        self.sending = True
        self.received_name = ""

        super().__init__(socket.AF_INET, socket.SOCK_STREAM) # init parent class
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.listenerThread = Thread(target = self.listener)
        self.senderThread = Thread(target = self.sender)
        
        try:
            self.connect((self.host, self.port)) # establish connection to server
            self.received_name = self.recv(1024).decode("utf-8")
        
        except Exception as e: 
            print(e)

        self.listenerThread.start()
        self.senderThread.start()

    def listener(self):
        """Ta funkcja czeka na wiadomość od drugiego klienta za pomocą serwera"""

        while self.listening:
            conn = self.recv(16384).decode("utf-8")
            if not conn:
                self.listening = False
                try:
                    self.shutdown(socket.SHUT_WR)
                    self.close()
                except OSError:
                    pass

            try:
                data = self.deserialize(conn)
                if data:
                    self.recv_data = data
                # pp = pprint.PrettyPrinter()
                # pp.pprint(self.recv_data)
                # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
            except json.decoder.JSONDecodeError:
                # pp = pprint.PrettyPrinter()
                # pp.pprint(conn)
                # print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n")
                print("json sie zdupil")

    def sender(self):
        """This method constantly sends information with a slight delay"""
        while self.sending:
            self.send_data(self.data_to_be_sent)
            sleep(0.5)

    def update_data_to_be_sent(self, data):
        self.data_to_be_sent = data

    def send_data(self, payload): 
        """Ta funkcja wysyła wiadomość do drugiego klienta za pomocą serwera"""
        data = self.serialize(payload)
        self.sendall(data.encode("utf-8"))

    def serialize(self, payload):
        """Zamienia pythonowe obiekty na json"""
        return json.dumps(payload)

    def deserialize(self, payload):
        """Zamienia json obiekty na python"""
        return json.loads(payload)

    def get_received_name(self):
        return self.received_name

