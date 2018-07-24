from card import Card
from base_of_card import *
from random import shuffle
from init_dimensions import *

class Player:
    
    def __init__ (
            self, deck = [], 
            hand = [], 
            data = {}, 
            my_turn = False, 
            graveyard = [],
            ):

        self.barracks = {
            0 : None,
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None
        }
        self.attacks = {
            0 : None,
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None
        }
        self.defense = {
            0 : None,
            1 : None,
            2 : None,
            3 : None,
            4 : None,
            5 : None,
            6 : None,
            7 : None,
            8 : None,
            9 : None
        }
        self.player_name = ""
        self.deck = deck
        self.hand = hand
        self.data = data
        self.my_turn = my_turn
        self.graveyard = graveyard


    def set_player_name(self, name):
        self.player_name = name

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
        def format_info(info):
            dump_info = {}

            if type(info) == type(dict()):
                for key in info:
                    if info[key] == None:
                        dump_info[key] = None
                    else:
                        dump_info[key] = info[key].name
                return dump_info						

            elif type(info) == type(list()):
                for card in info:
                    card_info = card.get_data()
                    dump_info[card.name] = card_info
                return dump_info


        deck_info = format_info(self.deck)
        hand_info = format_info(self.hand)
        graveyard_info = format_info(self.graveyard)
        attacks_info = format_info(self.attacks)
        defense_info = format_info(self.defense)
        barracks_info = format_info(self.barracks)

        data = {
            "player_name" : self.player_name,
            "myTurn" : self.my_turn,
            "deck" : deck_info,
            "hand" : hand_info,
            "graveyard" : graveyard_info,
            "attack_area" : attacks_info,
            "defense_area" : defense_info,
            "barracks_area" : barracks_info
        }

        return data

    def set_player_name(self, name):
        self.player_name = name

    def end_turn(self):
        self.my_turn = False

    def start_turn(self):
        self.my_turn = True

    def is_player_turn(slef):
        if self.my_turn == True:
            return True

    def was_clicked_in_hand(self, position, leftx, rightx, upy, downy, player):



        if len(leftx) > 3:
            if leftx[2] < rightx[1]:
                for i in range(len(player.hand)-2):
                    if position[0] > leftx[i] and position[0] < leftx[i+1]:
                        if position[1] < downy and position[1] > upy:
                            for i in range(len(player.hand) - 1):
                                if player.hand[i].clicked:
                                    player.hand[i].clicked = False
                            player.hand[i].clicked = True
                            print(player.hand[i].clicked)
                last = len(player.hand) - 2
                if position[0] > leftx[last] and position[0] < rightx[last]:
                    if position[1] < downy and position[1] > upy:   
                        for i in range(len(player.hand) - 1):
                                if player.hand[i].clicked:
                                    player.hand[i].clicked = False
                        player.hand[i].clicked = True         
                        print(player.hand[i].clicked)
            else:
                for i in range(len(player.hand)-1):
                    if position[0] > leftx[i] and position[0] < rightx[i]:
                        if position[1] < downy and position[1] > upy:
                            for i in range(len(player.hand) - 1):
                                if player.hand[i].clicked:
                                    player.hand[i].clicked = False
                            player.hand[i].clicked = True
                            print(player.hand[i].clicked)
        else:
            for i in range(len(player.hand)-1):
                if position[0] > leftx[i] and position[0] < rightx[i]:
                    if position[1] < downy and position[1] > upy:
                        for i in range(len(player.hand) - 1):
                                if player.hand[i].clicked:
                                    player.hand[i].clicked = False
                        player.hand[i].clicked = True
                        print(player.hand[i].clicked)
    def place_card(self, position, player):
        for i in range(len(player.hand)-1):
            if player.hand[i].clicked:
                for ii in range(10):
                    if position[0] > left_x_of_card[ii] and position[0] < right_x_of_card[ii]:
                        
                        if position[1] < down_attack_down_y and position[1] > down_attack_up_y:
                            player.hand[i].clicked = False
                            self.attacks[ii] = player.hand[i]
                            print(player.hand[i].name)
                            player.hand.pop(i)
                        elif position[1] < down_defense_down_y and position[1] > down_defense_up_y:
                            player.hand[i].clicked = False
                            print(player.hand[i].name)
                            self.defense[ii] = player.hand[i]
                            player.hand.pop(i)
                        elif position[1] < down_barrack_down_y and position[1] > down_barrack_up_y:
                            player.hand[i].clicked = False
                            print(player.hand[i].name)
                            self.barracks[ii] = player.hand[i]
                            player.hand.pop(i)