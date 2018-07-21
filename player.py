from card import Card
from base_of_card import *
from random import shuffle

class Player:
    
    def __init__ (self, deck = [], hand = [], data = {}, my_turn = False, graveyard = []):
        self.deck = deck
        self.hand = hand
        self.data = data
        self.my_turn = my_turn
        self.graveyard = graveyard

    def fill_deck(self):
        for i in range(13):
            for ii in range(4):
                self.deck.append(list_of_card[i][ii])
    
    def shuffle_deck(self):
        shuffle(self.deck)

    def prepare_hand(self):
        for i in range(20):
            self.hand.append(self.deck[0])
            self.deck.pop(0)

    def draw_card(self):
        if len(self.deck) > 0:
            self.hand.append(self.deck[0])
            self.deck.pop(0)
        else:
            print("You haven't more cards in deck")
    

    #Nie miałem pomysłu jak to zrobić
    def player_data(self):
        self.data = {
            "myTurn" : self.my_turn,
            "deck" : self.deck,
            "hand" : self.hand,
            "graveyard" : self.graveyard
        }

        return self.data

    def end_turn(self):
        self.my_turn = False

    def start_turn(self):
        self.my_turn = True



    