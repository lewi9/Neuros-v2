import socket
import json
from multiprocessing import Process
from Settings import PORT


class GameClient(socket.socket):
    """Ta klasa połącza się z serwerem i komunikuję się z iną instancją tej klasy"""

    def __init__(self, host, port): # param payload (dict)
        """Ta funkcja inicjalizuję tą klase"""
        self.host = host
        self.port = port
        self.data = None
        self.listening = True

        super().__init__(socket.AF_INET, socket.SOCK_STREAM) # init parent class
        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        
        self.listenerThread = Process(target = self.listener)
        
        try:
            self.connect((self.host, self.port)) # establish connection to server
            welcome_message = self.recv(1024).decode("utf-8")
            print(welcome_message)
        
        except Exception as e: 
            print(e)

        self.listenerThread.start()

    def listener(self):
        """Ta funkcja czeka na wiadomość od drugiego klienta za pomocą serwera"""

        while self.listening:
            try:
                conn = self.recv(1024).decode("utf-8")
                if not conn:
                    self.listening = False
                    try:
                        self.shutdown(socket.SHUT_WR)
                        self.close()
                    except OSError:
                        pass

                self.data = deserialize(conn)

            except Exception as e:
                print(e)
                self.listening = False
                try:
                    self.shutdown(socket.SHUT_WR)
                    self.close()
                except OSError:
                    pass

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

