import socket
import multiprocessing 
from random import shuffle
from Settings import PORT

class GameInstanceServer:
    """Ta klasa jest instancją gry pomiędzy dwoma graczami. Zajmuję się komunikcją klientów"""

    class RequestHandler(multiprocessing.Process):
        """Ta klasa jest komunikatorem każdego klienta"""
        def __init__(self, client, other_client):
            self.client = client
            self.other_client = other_client
            super().__init__(target = self.handler, args = (self.client, self.other_client))

        def handler(self, client, other_client):
            while True:		
                data = client.recv(16384).decode("utf-8")
                
                if not data:
                    break

                try:
                    other_client.sendall(data.encode("utf-8"))
                except BrokenPipeError:
                    pass

            client.shutdown(socket.SHUT_WR)
            client.close()

    def __init__(self, client1, client2):
        self.client1 = client1
        self.client2 = client2
        self.RequestHandler(self.client1, self.client2).start()
        self.RequestHandler(self.client2, self.client1).start()


class ManageGames(socket.socket):
    """Ta klasa jest managerem wszystkich instancji gier"""

    def __init__(self, localhost = False):
        super().__init__(socket.AF_INET, socket.SOCK_STREAM) # TCP
        
        self.localhost = localhost  # ip of current host .. change as necessary
        
        # try:
        # 	self.server_address = self.getMyIP_and_Port()
        # 	print(self.server_address) # address tego serwer'u
        # except Exception as e:
        # 	print(e)

        self.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1) # bez tego jest error
        
        if self.localhost:
            self.bind(("localhost", PORT)) 
        else:
            self.bind((self.server_address[0], PORT))
        
        self.amount_of_servers = 0
        self.servers = []

        self.client1 = None
        self.client1_addr = None
        self.client2 = None
        self.client2_addr = None

        self.clientsConnected = False

        if not self.clientsConnected: # czekamy na graczy 
            self.wait_for_clients()
        
    def getMyIP_and_Port(self):
        """Ta funkcja tworzy połączenie ze sobą (w sensie server) i pyta się o port i IP"""
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.connect(("8.8.8.8", 80))
        ip_addr = s.getsockname()[0]
        port = s.getsockname()[1]
        s.shutdown(socket.SHUT_WR)
        s.close()
        return (ip_addr, port)

    def wait_for_clients(self):
        """Ta funkja czeka na graczy a jak są to tworzy nową instancje gry"""
        message = "You have successfully connected :D\nWaiting for player..."

        players = ["Player_1", "Player_2"]
        shuffle(players)

        while not self.clientsConnected: # jeżeli nie ma graczy, to czekaj
            self.listen(5)

            if not self.client1:
                self.client1, self.client1_addr = self.accept()
                self.client1.send(players[0].encode("utf-8"))

            if not self.client2:
                self.client2, self.client2_addr = self.accept()
                self.client2.sendall(players[1].encode("utf-8"))
                self.clientsConnected = True

        print("Clients connected")
        g = GameInstanceServer(self.client1, self.client2) # tworzy instancje gry

        # resetowanie wartości
        self.client1 = None 
        self.client1_addr = None
        self.client2 = None
        self.client2_addr = None

        self.clientsConnected = False

    def display_server_status(self):
        """To będzie dynamicznie wyświetlało status serwerów"""
        print("not working lol")


    

