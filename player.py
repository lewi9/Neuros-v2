from card import Card
from base_of_card import *
from random import shuffle
from init_dimensions import *
from Settings import *

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
            dump_info_dict = {}
            dump_info_list = []

            if type(info) == type(dict()):
                for key in info:
                    if info[key] == None:
                        dump_info_dict[key] = None
                    else:
                        dump_info_dict[key] = info[key].name
                return dump_info_dict						

            elif type(info) == type(list()):
                for card in info:
                    card_info = card.get_data()
                    dump_info_list.append(card_info)

                return dump_info_list


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
        Card.end_turn_minus_frozen(self, self.barracks)

    def start_turn(self):
        self.my_turn = True

    def is_player_turn(slef):
        if self.my_turn == True:
            return True

    def unclick(self, tab, tab_2 ):
        for i in range(len(tab)-1):
                if tab[i].clicked:
                    tab[i].clicked = False
        for i in range(10):
            if tab_2[i] != None:
                if tab_2[i].clicked:
                    tab_2[i].clicked = False


    def was_clicked_in_hand(self, position, leftx, rightx, upy, downy, player):
        if len(leftx) > 3:
            if leftx[2] < rightx[1]:
                for i in range(len(player.hand)-2):
                    if position[0] > leftx[i] and position[0] < leftx[i+1]:
                        if position[1] < downy and position[1] > upy:
                            player.unclick(player.hand, self.barracks)
                            player.hand[i].clicked = True
                last = len(player.hand) - 2
                if position[0] > leftx[last] and position[0] < rightx[last]:
                    if position[1] < downy and position[1] > upy:   
                        player.unclick(player.hand, self.barracks)
                        player.hand[i+1].clicked = True         
            else:
                for i in range(len(player.hand)-1):
                    if position[0] > leftx[i] and position[0] < rightx[i]:
                        if position[1] < downy and position[1] > upy:
                            player.unclick(player.hand, self.barracks)
                            player.hand[i].clicked = True
        else:
            for i in range(len(player.hand)-1):
                if position[0] > leftx[i] and position[0] < rightx[i]:
                    if position[1] < downy and position[1] > upy:
                        player.unclick(player.hand, self.barracks)
                        player.hand[i].clicked = True

    def was_clicked_in_barracks(self, position, player):
        for i in range(10):
            if position[0] > left_x_of_card[i] and position[0] < right_x_of_card[i]:
                if position[1] < down_barrack_down_y and position[1] > down_barrack_up_y:
                    if self.barracks[i] != None:
                        if self.barracks[i].frozen_time < 1:
                            player.unclick(player.hand, self.barracks)
                            self.barracks[i].clicked = True
                        elif self.barracks[i].frozen_time > 0:
                            print("This minion should training more!")
                            player.unclick(player.hand, self.barracks)
    
    def move_from_barracks_to_attacks(self, position, player):
        for i in range(10):
            if self.barracks[i] != None:
                print("XDU")
                if self.barracks[i].clicked:
                    print("Mypciu")
                    for ii in range(10):
                        print("EE")
                        if position[0] > left_x_of_card[ii] and position[0] < right_x_of_card[ii]:
                            print("XD")
                            if position[1] < down_attack_down_y and position[1] > down_attack_up_y:
                                print("Coś")
                                if self.attacks[ii] == None:
                                    print("Ok")
                                    self.barracks[i].clicked = False
                                    self.attacks[ii] = self.barracks[i]
                                    self.barracks[i] = None

                        
                    
    def place_card(self, position, player, was_put_in_frozen):
        for i in range(len(player.hand)-1):
            if player.hand[i].clicked:
                for ii in range(10):
                    if position[0] > left_x_of_card[ii] and position[0] < right_x_of_card[ii]:
                        if position[1] < down_attack_down_y and position[1] > down_attack_up_y:
                            if self.attacks[ii] == None and player.hand[i].frozen_time < 1:
                                player.hand[i].clicked = False
                                self.attacks[ii] = player.hand[i]
                                player.hand.pop(i)
                        elif position[1] < down_defense_down_y and position[1] > down_defense_up_y:
                            if self.defense[ii] == None:
                                player.hand[i].clicked = False
                                self.defense[ii] = player.hand[i]
                                player.hand.pop(i)
                        elif position[1] < down_barrack_down_y and position[1] > down_barrack_up_y:
                            if self.barracks[ii] == None and was_put_in_frozen != 1:
                                player.hand[i].clicked = False
                                self.barracks[ii] = player.hand[i]
                                player.hand.pop(i)
                                was_put_in_frozen = 1
        return was_put_in_frozen