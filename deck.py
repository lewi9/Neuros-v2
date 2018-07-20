from card import Card
from base_of_card import *

class Deck:
    
    def __init__ (self, deck = []):
        self.deck = deck

    def fill_base(self):
        for i in range(13):
            for ii in range(4):
                self.deck.append(list_of_card[i])